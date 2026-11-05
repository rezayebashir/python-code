import tkinter as tk
from tkinter import messagebox


class PersonalInfoForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Information Form")
        self.root.geometry("450x400")
        self.root.minsize(350, 350)

        # --- Frame 1: Header (Managed with pack) ---
        self.header_frame = tk.Frame(self.root, bg="#3b5998", height=50)
        self.header_frame.pack(fill=tk.X, side=tk.TOP)

        self.lbl_title = tk.Label(
            self.header_frame,
            text="Personal Information Form",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#3b5998"
        )
        self.lbl_title.pack(pady=10)

        # --- Frame 2: Main Form Body (Managed with pack, elements inside use grid) ---
        self.form_frame = tk.Frame(self.root, padx=20, pady=15)
        self.form_frame.pack(fill=tk.BOTH, expand=True)

        # Make the Entry column (column 1) responsive
        self.form_frame.grid_columnconfigure(1, weight=1)

        # Define fields and create widgets dynamically
        self.fields = ["Full Name", "Student ID", "Email", "Department", "Semester", "Phone"]
        self.entries = {}

        for idx, field in enumerate(self.fields):
            # Create and place Label
            lbl = tk.Label(self.form_frame, text=f"{field}:", font=("Arial", 10))
            lbl.grid(row=idx, column=0, sticky="w", pady=6, padx=(0, 10))

            # Create and place Entry
            entry = tk.Entry(self.form_frame, font=("Arial", 10))
            entry.grid(row=idx, column=1, sticky="ew", pady=6)

            # Store references using lowercase snake_case keys
            dict_key = field.lower().replace(" ", "_")
            self.entries[dict_key] = entry

        # --- Frame 3: Action Buttons Footer (Managed with pack) ---
        self.footer_frame = tk.Frame(self.root, pady=15)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        # Action Buttons
        self.btn_save = tk.Button(self.footer_frame, text="Save", command=self.save_info, width=10, bg="#4caf50",
                                  fg="white")
        self.btn_save.pack(side=tk.LEFT, padx=15, expand=True)

        self.btn_clear = tk.Button(self.footer_frame, text="Clear", command=self.clear_fields, width=10, bg="#f44336",
                                   fg="white")
        self.btn_clear.pack(side=tk.LEFT, padx=15, expand=True)

        self.btn_exit = tk.Button(self.footer_frame, text="Exit", command=self.root.quit, width=10, bg="#9e9e9e",
                                  fg="white")
        self.btn_exit.pack(side=tk.LEFT, padx=15, expand=True)

    def save_info(self):
        """Displays collected information to the console terminal."""
        print("=========================================")
        print("       SUBMITTED STUDENT INFO            ")
        print("=========================================")
        for field in self.fields:
            dict_key = field.lower().replace(" ", "_")
            value = self.entries[dict_key].get()
            print(f"{field:15}: {value}")
        print("=========================================\n")

        messagebox.showinfo("Success", "Information saved and logged to console successfully!")

    def clear_fields(self):
        """Clears all input fields."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)


# Main program execution
if __name__ == "__main__":
    window = tk.Tk()
    app = PersonalInfoForm(window)
    window.mainloop()
