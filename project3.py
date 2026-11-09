import tkinter as tk
from tkinter import messagebox


class StudentRegistrationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")
        self.root.geometry("450x550")

        # --- 10. Handle the window close protocol ---
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)

        # Title Label
        title = tk.Label(root, text="Student Registration", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Form Container Frame
        form_frame = tk.Frame(root)
        form_frame.pack(pady=10, padx=20, fill="both", expand=True)
        # Change this line:
        form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # To this:
        form_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # --- 2. Create four Entry controls and one Text control ---
        # Field 1: Full Name
        tk.Label(form_frame, text="Full Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(form_frame, font=("Arial", 10), width=30)
        self.entry_name.grid(row=0, column=1, pady=5, padx=5)

        # Field 2: Student ID
        tk.Label(form_frame, text="Student ID:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_id = tk.Entry(form_frame, font=("Arial", 10), width=30)
        self.entry_id.grid(row=1, column=1, pady=5, padx=5)

        # Field 3: Email
        tk.Label(form_frame, text="Email Address:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_email = tk.Entry(form_frame, font=("Arial", 10), width=30)
        self.entry_email.grid(row=2, column=1, pady=5, padx=5)

        # Field 4: Course
        tk.Label(form_frame, text="Course/Major:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
        self.entry_course = tk.Entry(form_frame, font=("Arial", 10), width=30)
        self.entry_course.grid(row=3, column=1, pady=5, padx=5)

        # Field 5: Additional Notes (Text Control)
        tk.Label(form_frame, text="Additional Notes:", font=("Arial", 10)).grid(row=4, column=0, sticky="nw", pady=5)
        self.text_notes = tk.Text(form_frame, font=("Arial", 10), width=30, height=6)
        self.text_notes.grid(row=4, column=1, pady=5, padx=5)

        # Status Message Label
        self.label_status = tk.Label(root, text="", font=("Arial", 10, "italic"), fg="blue")
        self.label_status.pack(pady=5)

        # Action Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        self.btn_save = tk.Button(btn_frame, text="Save (Ctrl+S)", width=10, bg="#4CAF50", fg="white",
                                  command=self.save_data)
        self.btn_save.grid(row=0, column=0, padx=5)

        self.btn_clear = tk.Button(btn_frame, text="Clear (Esc)", width=10, bg="#f44336", fg="white",
                                   command=self.clear_form)
        self.btn_clear.grid(row=0, column=1, padx=5)

        self.btn_exit = tk.Button(btn_frame, text="Exit", width=10, bg="#555555", fg="white",
                                  command=self.exit_application)
        self.btn_exit.grid(row=0, column=2, padx=5)

        # --- 7. Use FocusIn/FocusOut on at least two fields ---
        self.entry_name.bind("<FocusIn>", lambda e: self.on_focus_in(self.entry_name))
        self.entry_name.bind("<FocusOut>", lambda e: self.on_focus_out(self.entry_name))
        self.entry_id.bind("<FocusIn>", lambda e: self.on_focus_in(self.entry_id))
        self.entry_id.bind("<FocusOut>", lambda e: self.on_focus_out(self.entry_id))

        # --- 8. Use a mouse event on one visible widget (Hover effect) ---
        self.btn_save.bind("<Enter>", self.on_mouse_enter)
        self.btn_save.bind("<Leave>", self.on_mouse_leave)

        # --- 4, 5, 6. Keyboard Shortcuts / Bindings ---
        self.root.bind("<Return>", lambda event: self.save_data())
        self.root.bind("<Escape>", lambda event: self.clear_form())
        self.root.bind("<Control-s>", lambda event: self.save_data())
        self.root.bind("<Control-S>", lambda event: self.save_data())

    # --- 11. Handlers Organized as Methods ---

    def on_focus_in(self, widget):
        """Highlights the entry field when it gains focus."""
        widget.config(bg="#e8f0fe")

    def on_focus_out(self, widget):
        """Resets the entry field background when focus is lost."""
        widget.config(bg="white")

    def on_mouse_enter(self, event):
        """Changes Save button color on mouse hover."""
        self.btn_save.config(bg="#45a049")

    def on_mouse_leave(self, event):
        """Restores Save button color when mouse leaves."""
        self.btn_save.config(bg="#4CAF50")

    def reset_status_message(self):
        """Clears the status bar text."""
        self.label_status.config(text="")

    def save_data(self):
        """Validates input, processes the save handler, and updates status."""
        name = self.entry_name.get().strip()
        student_id = self.entry_id.get().strip()

        if not name or not student_id:
            messagebox.showwarning("Validation Error", "Full Name and Student ID are required!")
            return

        # Simulating data submission
        self.label_status.config(text=f"Success: Registration saved for {name}!", fg="green")

        # --- 9. Use after() to reset a status message automatically (after 3 seconds) ---
        self.root.after(3000, self.reset_status_message)

    def clear_form(self):
        """Clears all input controls."""
        self.entry_name.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_course.delete(0, tk.END)
        self.text_notes.delete("1.0", tk.END)

        self.label_status.config(text="Form cleared.", fg="orange")
        self.root.after(3000, self.reset_status_message)

    def exit_application(self):
        """Prompts confirmation before exiting the application."""
        if messagebox.askokcancel("Exit Confirmation", "Are you sure you want to close the application?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRegistrationGUI(root)
    root.mainloop()
