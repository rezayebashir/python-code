import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


class StudentCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System - CRUD GUI")
        self.root.geometry("760x520")
        self.root.resizable(False, False)

        # Track currently selected student ID
        self.selected_id = None

        # Initialize Database
        self.conn = sqlite3.connect("students_gui.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Build UI and Load Data
        self.setup_ui()
        self.load_records()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL,
            semester INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    def setup_ui(self):
        # --- Form Frame ---
        form_frame = tk.LabelFrame(self.root, text="Student Details", padx=15, pady=10)
        form_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
        self.name_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=0, column=2, sticky="w", pady=5)
        self.email_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.email_var, width=30).grid(row=0, column=3, padx=10, pady=5)

        tk.Label(form_frame, text="Department:").grid(row=1, column=0, sticky="w", pady=5)
        self.dept_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.dept_var, width=30).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Semester:").grid(row=1, column=2, sticky="w", pady=5)
        self.semester_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.semester_var, width=30).grid(row=1, column=3, padx=10, pady=5)

        # --- CRUD Buttons Frame ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=15, pady=5)

        tk.Button(btn_frame, text="Save New", bg="#2e7d32", fg="white", width=13, command=self.add_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update Selected", bg="#1565c0", fg="white", width=15, command=self.update_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Selected", bg="#c62828", fg="white", width=15, command=self.delete_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear Form", width=12, command=self.clear_form).pack(side="left", padx=5)

        # --- Search Bar Frame ---
        search_frame = tk.Frame(self.root)
        search_frame.pack(fill="x", padx=15, pady=8)

        tk.Label(search_frame, text="Search by Name:").pack(side="left", padx=(5, 5))
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side="left", padx=5)
        search_entry.bind("<KeyRelease>", lambda event: self.search_students())

        tk.Button(search_frame, text="Show All", width=10, command=self.reset_search).pack(side="left", padx=5)

        # --- Treeview Table Frame ---
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        columns = ("id", "name", "email", "department", "semester")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=11)

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("department", text="Department")
        self.tree.heading("semester", text="Semester")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("name", width=170)
        self.tree.column("email", width=210)
        self.tree.column("department", width=180)
        self.tree.column("semester", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind row click to load record into the form
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    def validate_inputs(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        dept = self.dept_var.get().strip()
        semester = self.semester_var.get().strip()

        if not name or not email or not dept or not semester:
            messagebox.showwarning("Validation Error", "All fields (Name, Email, Department, Semester) are required.")
            return None

        if not semester.isdigit() or int(semester) <= 0:
            messagebox.showwarning("Validation Error", "Semester must be a valid positive number.")
            return None

        return name, email, dept, int(semester)

    def add_student(self):
        data = self.validate_inputs()
        if not data:
            return

        try:
            self.cursor.execute(
                "INSERT INTO students (name, email, department, semester) VALUES (?, ?, ?, ?)",
                data
            )
            self.conn.commit()
            messagebox.showinfo("Success", "Student record saved successfully.")
            self.clear_form()
            self.load_records()
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate Email", f"The email '{data[1]}' already exists in the database.")

    def load_records(self, query="SELECT * FROM students", params=()):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute(query, params)
        for student in self.cursor.fetchall():
            self.tree.insert("", "end", values=student)

    def on_row_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return

        values = self.tree.item(selected, "values")
        if values:
            self.selected_id = values[0]
            self.name_var.set(values[1])
            self.email_var.set(values[2])
            self.dept_var.set(values[3])
            self.semester_var.set(values[4])

    def update_student(self):
        if self.selected_id is None:
            messagebox.showwarning("Selection Required", "Please select a student from the table first.")
            return

        data = self.validate_inputs()
        if not data:
            return

        try:
            self.cursor.execute(
                """UPDATE students
                   SET name = ?, email = ?, department = ?, semester = ?
                   WHERE id = ?""",
                (*data, self.selected_id)
            )
            self.conn.commit()
            messagebox.showinfo("Updated", "Student record updated successfully.")
            self.clear_form()
            self.load_records()
        except sqlite3.IntegrityError:
            messagebox.showerror("Duplicate Email", f"The email '{data[1]}' is already used by another student.")

    def delete_student(self):
        if self.selected_id is None:
            messagebox.showwarning("Selection Required", "Please select a student from the table to delete.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{self.name_var.get()}' (ID: {self.selected_id})?"
        )
        if confirm:
            self.cursor.execute("DELETE FROM students WHERE id = ?", (self.selected_id,))
            self.conn.commit()
            messagebox.showinfo("Deleted", "Student record deleted.")
            self.clear_form()
            self.load_records()

    def search_students(self):
        keyword = self.search_var.get().strip()
        self.load_records(
            "SELECT * FROM students WHERE name LIKE ?",
            (f"%{keyword}%",)
        )

    def reset_search(self):
        self.search_var.set("")
        self.load_records()

    def clear_form(self):
        self.selected_id = None
        self.name_var.set("")
        self.email_var.set("")
        self.dept_var.set("")
        self.semester_var.set("")
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def on_closing(self):
        self.conn.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentCRUDApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
