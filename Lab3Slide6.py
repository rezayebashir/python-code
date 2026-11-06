import tkinter as tk
from tkinter import messagebox


class PersonalInfoFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Information Form")
        self.root.geometry("450x420")
        self.root.minsize(400, 380)

        # Initialize dictionary to dynamically track all entry widgets
        self.entries = {}

        # --- 1. HEADER CONTAINER (Using pack) ---
        self.header_frame = tk.Frame(self.root, bg="#2C3E50", height=60)
        self.header_frame.pack(fill=tk.X, side=tk.TOP)
        self.header_frame.pack_propagate(False)  # Maintain strict height

        self.header_label = tk.Label(
            self.header_frame,
            text="STUDENT PERSONAL INFORMATION FORM",
            fg="white",
            bg="#2C3E50",
            font=("Arial", 12, "bold")
        )
        self.header_label.pack(expand=True)

        # --- 2. MAIN FORM CONTAINER (Using grid inside nested frame) ---
        self.form_frame = tk.LabelFrame(self.root, text=" Registration Details ", padx=15, pady=15)
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Make the Entry column (Column 1) responsive
        self.form_frame.columnconfigure(1, weight=1)

        # List of required fields to generate dynamically
        fields = ["Full Name", "Student ID", "Email", "Department", "Semester", "Phone"]

        for idx, field_name in enumerate(fields):
            # Create and place descriptive labels
            label = tk.Label(self.form_frame, text=f"{field_name}:", font=("Arial", 10))
            label.grid(row=idx, column=0, sticky="w", pady=6, padx=(0, 10))

            # Create, register, and place structural entries
            entry = tk.Entry(self.form_frame, font=("Arial", 10))
            entry.grid(row=idx, column=1, sticky="ew", pady=6)

            # Use lower_snake_case keys for reference map dictionary
            dict_key = field_name.lower().replace(" ", "_")
            self.entries[dict_key] = entry

        # --- 3. FOOTER ACTION CONTAINER (Using grid inside form frame) ---
        self.button_frame = tk.Frame(self.form_frame)
        self.button_frame.grid(row=len(fields), column=0, columnspan=2, sticky="ew", pady=(20, 0))

        # Configure button frame columns evenly
        for i in range(3):
            self.button_frame.columnconfigure(i, weight=1)

        # Instantiate structural interactive buttons
        self.save_btn = tk.Button(self.button_frame, text="Save", command=self.save_information, bg="#2ECC71",
                                  fg="white", width=10, font=("Arial", 9, "bold"))
        self.save_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = tk.Button(self.button_frame, text="Clear", command=self.clear_entries, bg="#E67E22",
                                   fg="white", width=10, font=("Arial", 9, "bold"))
        self.clear_btn.grid(row=0, column=1, padx=5)

        self.exit_btn = tk.Button(self.button_frame, text="Exit", command=self.root.quit, bg="#E74C3C", fg="white",
                                  width=10, font=("Arial", 9, "bold"))
        self.exit_btn.grid(row=0, column=2, padx=5)

    def save_information(self):
        """Retrieves user inputs, validates presence, and prints them cleanly to terminal console."""
        print("\n======================= SUBMITTED DATA =======================")
        all_valid = True

        for field_key, entry_widget in self.entries.items():
            field_display_name = field_key.replace("_", " ").title()
            value = entry_widget.get().strip()

            if not value:
                all_valid = False

            print(f"{field_display_name:<15}: {value if value else '[EMPTY]'}")
        print("===============================================================")

        if all_valid:
            messagebox.showinfo("Success", "Information saved successfully to terminal console.")
        else:
            messagebox.showwarning("Warning", "Some fields were left blank, but data has been outputted.")

    def clear_entries(self):
        """Resets and purges string literals out of all text entry areas completely."""
        for entry_widget in self.entries.values():
            entry_widget.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalInfoFormApp(root)
    root.mainloop()
