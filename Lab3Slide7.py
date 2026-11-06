import tkinter as tk
from tkinter import messagebox


class PersonalInformationForm:
    """Personal Information Form using Tkinter."""

    def __init__(self, root):
        self.root = root

        # ----------------------------------------------------
        # WINDOW SETTINGS
        # ----------------------------------------------------
        self.root.title("Personal Information Form")
        self.root.geometry("650x520")
        self.root.resizable(True, True)

        # ----------------------------------------------------
        # COLORS
        # ----------------------------------------------------
        self.bg_color = "#f4f6f8"
        self.header_color = "#1f4e78"
        self.button_color = "#2e75b6"
        self.text_color = "#1f2937"

        self.root.configure(bg=self.bg_color)

        # ----------------------------------------------------
        # HEADER FRAME
        # pack() is used here as required by the assignment.
        # ----------------------------------------------------
        self.create_header()

        # ----------------------------------------------------
        # MAIN FORM FRAME
        # ----------------------------------------------------
        self.create_form()

        # ----------------------------------------------------
        # FOOTER FRAME
        # pack() is also used for the footer.
        # ----------------------------------------------------
        self.create_footer()

    # ========================================================
    # HEADER
    # ========================================================

    def create_header(self):
        self.header_frame = tk.Frame(
            self.root,
            bg=self.header_color,
            height=80
        )

        self.header_frame.pack(
            fill="x",
            side="top"
        )

        title_label = tk.Label(
            self.header_frame,
            text="Personal Information Form",
            font=("Arial", 22, "bold"),
            bg=self.header_color,
            fg="white"
        )

        title_label.pack(pady=(15, 0))

        subtitle_label = tk.Label(
            self.header_frame,
            text="Please enter your student information",
            font=("Arial", 10),
            bg=self.header_color,
            fg="#dbeafe"
        )

        subtitle_label.pack(pady=(3, 10))

    # ========================================================
    # MAIN FORM
    # ========================================================

    def create_form(self):

        self.form_frame = tk.Frame(
            self.root,
            bg=self.bg_color,
            padx=40,
            pady=25
        )

        self.form_frame.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # Make column 1 responsive
        # ----------------------------------------------------

        self.form_frame.columnconfigure(
            1,
            weight=1
        )

        # ----------------------------------------------------
        # Labels and Entry widgets
        # ----------------------------------------------------

        # Full Name
        tk.Label(
            self.form_frame,
            text="Full Name:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=10
        )

        self.name_entry = tk.Entry(
            self.form_frame,
            font=("Arial", 11)
        )

        self.name_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=10
        )

        # Student ID
        tk.Label(
            self.form_frame,
            text="Student ID:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=10
        )

        self.student_id_entry = tk.Entry(
            self.form_frame,
            font=("Arial", 11)
        )

        self.student_id_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            pady=10
        )

        # Email
        tk.Label(
            self.form_frame,
            text="Email:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=10
        )

        self.email_entry = tk.Entry(
            self.form_frame,
            font=("Arial", 11)
        )

        self.email_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=10
        )

        # Department
        tk.Label(
            self.form_frame,
            text="Department:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=10
        )

        self.department_entry = tk.Entry(
            self.form_frame,
            font=("Arial", 11)
        )

        self.department_entry.grid(
            row=3,
            column=1,
            sticky="ew",
            pady=10
        )

        # Semester
        tk.Label(
            self.form_frame,
            text="Semester:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=10
        )

        self.semester_entry = tk.Entry(
            self.form_frame,
            font=("Arial", 11)
        )

        self.semester_entry.grid(
            row=4,
            column=1,
            sticky="ew",
            pady=10
        )

        # Phone
        tk.Label(
            self.form_frame,
            text="Phone:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=10
        )

        self.phone_entry = tk.Entry(
            self.form_frame,
            font=("Arial", 11)
        )

        self.phone_entry.grid(
            row=5,
            column=1,
            sticky="ew",
            pady=10
        )

    # ========================================================
    # FOOTER / BUTTONS
    # ========================================================

    def create_footer(self):

        self.footer_frame = tk.Frame(
            self.root,
            bg="#e5e7eb",
            height=70
        )

        # pack() used for footer
        self.footer_frame.pack(
            fill="x",
            side="bottom"
        )

        # Save Button
        save_button = tk.Button(
            self.footer_frame,
            text="Save",
            command=self.save_information,
            bg="#2563eb",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            cursor="hand2"
        )

        save_button.pack(
            side="left",
            padx=(120, 10),
            pady=15
        )

        # Clear Button
        clear_button = tk.Button(
            self.footer_frame,
            text="Clear",
            command=self.clear_form,
            bg="#f59e0b",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            cursor="hand2"
        )

        clear_button.pack(
            side="left",
            padx=10,
            pady=15
        )

        # Exit Button
        exit_button = tk.Button(
            self.footer_frame,
            text="Exit",
            command=self.exit_application,
            bg="#dc2626",
            fg="white",
            font=("Arial", 11, "bold"),
            width=10,
            cursor="hand2"
        )

        exit_button.pack(
            side="left",
            padx=10,
            pady=15
        )

    # ========================================================
    # GET FORM DATA
    # ========================================================

    def get_form_data(self):
        """Collect all information from Entry widgets."""

        return {
            "Full Name": self.name_entry.get().strip(),
            "Student ID": self.student_id_entry.get().strip(),
            "Email": self.email_entry.get().strip(),
            "Department": self.department_entry.get().strip(),
            "Semester": self.semester_entry.get().strip(),
            "Phone": self.phone_entry.get().strip()
        }

    # ========================================================
    # VALIDATE FORM
    # ========================================================

    def validate_form(self, data):
        """Check that all fields contain information."""

        for field, value in data.items():

            if not value:
                messagebox.showwarning(
                    "Missing Information",
                    f"Please enter your {field}."
                )

                return False

        # Basic email validation
        if "@" not in data["Email"]:
            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return False

        return True

    # ========================================================
    # SAVE
    # ========================================================

    def save_information(self):
        """Validate and display the entered information."""

        data = self.get_form_data()

        if not self.validate_form(data):
            return

        # Print information to console
        print("\n" + "=" * 45)
        print("       PERSONAL INFORMATION")
        print("=" * 45)

        for field, value in data.items():
            print(f"{field}: {value}")

        print("=" * 45)

        # Also display information in a message box
        information = (
            f"Full Name: {data['Full Name']}\n"
            f"Student ID: {data['Student ID']}\n"
            f"Email: {data['Email']}\n"
            f"Department: {data['Department']}\n"
            f"Semester: {data['Semester']}\n"
            f"Phone: {data['Phone']}"
        )

        messagebox.showinfo(
            "Information Saved",
            information
        )

    # ========================================================
    # CLEAR
    # ========================================================

    def clear_form(self):
        """Remove all values from Entry widgets."""

        entries = [
            self.name_entry,
            self.student_id_entry,
            self.email_entry,
            self.department_entry,
            self.semester_entry,
            self.phone_entry
        ]

        for entry in entries:
            entry.delete(0, tk.END)

        # Put cursor back in first field
        self.name_entry.focus()

    # ========================================================
    # EXIT
    # ========================================================

    def exit_application(self):
        """Close the application."""

        answer = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if answer:
            self.root.destroy()


# ============================================================
# PROGRAM START
# ============================================================

def main():
    root = tk.Tk()

    app = PersonalInformationForm(root)

    root.mainloop()


if __name__ == "__main__":
    main()
