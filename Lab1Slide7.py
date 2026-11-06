import tkinter as tk
from tkinter import ttk, messagebox


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f2f2f2")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#1f4e78",
            fg="white",
            pady=15
        )
        title.pack(fill="x")

        # Main container
        main_frame = tk.Frame(self.root, bg="#f2f2f2")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # =========================
        # 1. Student Information
        # =========================
        student_frame = tk.LabelFrame(
            main_frame,
            text="1. Student Information",
            font=("Arial", 12, "bold"),
            bg="#f2f2f2",
            padx=10,
            pady=10
        )
        student_frame.pack(fill="x", pady=5)

        tk.Label(student_frame, text="Student ID:", bg="#f2f2f2").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.student_id = tk.Entry(student_frame, width=25)
        self.student_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(student_frame, text="Student Name:", bg="#f2f2f2").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )
        self.student_name = tk.Entry(student_frame, width=25)
        self.student_name.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(student_frame, text="Gender:", bg="#f2f2f2").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        self.gender = ttk.Combobox(
            student_frame,
            values=["Male", "Female", "Other"],
            width=22,
            state="readonly"
        )
        self.gender.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(student_frame, text="Date of Birth:", bg="#f2f2f2").grid(
            row=1, column=2, sticky="w", padx=5, pady=5
        )
        self.dob = tk.Entry(student_frame, width=25)
        self.dob.grid(row=1, column=3, padx=5, pady=5)

        # =========================
        # 2. Academic Information
        # =========================
        academic_frame = tk.LabelFrame(
            main_frame,
            text="2. Academic Information",
            font=("Arial", 12, "bold"),
            bg="#f2f2f2",
            padx=10,
            pady=10
        )
        academic_frame.pack(fill="x", pady=5)

        tk.Label(academic_frame, text="Department:", bg="#f2f2f2").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.department = ttk.Combobox(
            academic_frame,
            values=[
                "Computer Science",
                "Information Technology",
                "Business",
                "Engineering",
                "Medicine"
            ],
            width=22
        )
        self.department.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(academic_frame, text="Class/Grade:", bg="#f2f2f2").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )
        self.grade = tk.Entry(academic_frame, width=25)
        self.grade.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(academic_frame, text="Semester:", bg="#f2f2f2").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        self.semester = ttk.Combobox(
            academic_frame,
            values=["1", "2", "3", "4", "5", "6", "7", "8"],
            width=22
        )
        self.semester.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(academic_frame, text="GPA:", bg="#f2f2f2").grid(
            row=1, column=2, sticky="w", padx=5, pady=5
        )
        self.gpa = tk.Entry(academic_frame, width=25)
        self.gpa.grid(row=1, column=3, padx=5, pady=5)

        # =========================
        # 3. Contact Information
        # =========================
        contact_frame = tk.LabelFrame(
            main_frame,
            text="3. Contact Information",
            font=("Arial", 12, "bold"),
            bg="#f2f2f2",
            padx=10,
            pady=10
        )
        contact_frame.pack(fill="x", pady=5)

        tk.Label(contact_frame, text="Phone:", bg="#f2f2f2").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.phone = tk.Entry(contact_frame, width=25)
        self.phone.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(contact_frame, text="Email:", bg="#f2f2f2").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )
        self.email = tk.Entry(contact_frame, width=25)
        self.email.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(contact_frame, text="Address:", bg="#f2f2f2").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        self.address = tk.Entry(contact_frame, width=25)
        self.address.grid(row=1, column=1, padx=5, pady=5)

        # =========================
        # Buttons
        # =========================
        button_frame = tk.Frame(main_frame, bg="#f2f2f2")
        button_frame.pack(pady=10)

        tk.Button(
            button_frame, text="Add Student",
            command=self.add_student,
            bg="#28a745", fg="white",
            width=15
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame, text="Update",
            command=self.update_student,
            bg="#007bff", fg="white",
            width=15
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame, text="Delete",
            command=self.delete_student,
            bg="#dc3545", fg="white",
            width=15
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame, text="Clear",
            command=self.clear_fields,
            bg="#6c757d", fg="white",
            width=15
        ).grid(row=0, column=3, padx=5)

        # =========================
        # Student Table
        # =========================
        table_frame = tk.Frame(main_frame)
        table_frame.pack(fill="both", expand=True)

        columns = (
            "ID", "Name", "Gender", "DOB",
            "Department", "Grade", "Semester",
            "GPA", "Phone", "Email", "Address"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:
            self.table.heading(column, text=column)
            self.table.column(column, width=100)

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )
        scrollbar.pack(side="right", fill="y")

        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.bind(
            "<ButtonRelease-1>",
            self.select_student
        )

    def get_data(self):
        return (
            self.student_id.get(),
            self.student_name.get(),
            self.gender.get(),
            self.dob.get(),
            self.department.get(),
            self.grade.get(),
            self.semester.get(),
            self.gpa.get(),
            self.phone.get(),
            self.email.get(),
            self.address.get()
        )

    def add_student(self):
        data = self.get_data()

        if not data[0] or not data[1]:
            messagebox.showwarning(
                "Warning",
                "Student ID and Student Name are required."
            )
            return

        self.table.insert("", "end", values=data)
        messagebox.showinfo(
            "Success",
            "Student added successfully."
        )
        self.clear_fields()

    def update_student(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a student first."
            )
            return

        self.table.item(
            selected[0],
            values=self.get_data()
        )

        messagebox.showinfo(
            "Success",
            "Student updated successfully."
        )

    def delete_student(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a student first."
            )
            return

        answer = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete this student?"
        )

        if answer:
            self.table.delete(selected[0])
            self.clear_fields()

    def select_student(self, event):
        selected = self.table.selection()

        if not selected:
            return

        values = self.table.item(
            selected[0],
            "values"
        )

        entries = [
            self.student_id,
            self.student_name,
            self.gender,
            self.dob,
            self.department,
            self.grade,
            self.semester,
            self.gpa,
            self.phone,
            self.email,
            self.address
        ]

        for entry, value in zip(entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def clear_fields(self):
        entries = [
            self.student_id,
            self.student_name,
            self.dob,
            self.grade,
            self.gpa,
            self.phone,
            self.email,
            self.address
        ]

        for entry in entries:
            entry.delete(0, tk.END)

        self.gender.set("")
        self.department.set("")
        self.semester.set("")


# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
