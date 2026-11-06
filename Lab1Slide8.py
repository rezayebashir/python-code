import tkinter as tk
from tkinter import messagebox


class ProfileForm(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Practical Lab 1 - Profile Form")
        self.geometry("450x500")
        self.minsize(400, 450)

        self._build_ui()

    def _build_ui(self):
        # ----------------------------------------------------
        # 1. HEADER FRAME (Using pack() for root-level)
        # ----------------------------------------------------
        self.header_frame = tk.Frame(self, bg="#34495E", pady=15)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(
            self.header_frame,
            text="Student Profile Registration",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#34495E"
        )
        self.title_label.pack()

        # ----------------------------------------------------
        # 2. FORM FRAME (Using pack() for root-level)
        # ----------------------------------------------------
        self.form_frame = tk.LabelFrame(self, text=" Personal Details ", padx=15, pady=15)
        self.form_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Configure internal grid responsiveness for form fields
        self.form_frame.columnconfigure(0, weight=0)  # Labels stay compact
        self.form_frame.columnconfigure(1, weight=1)  # Entry fields expand horizontally

        # Required single-line Entry fields
        fields = ["Full Name", "Student ID", "Email", "Phone"]
        self.entries = {}

        # Place single-line fields using grid() as required
        for idx, field_name in enumerate(fields):
            lbl = tk.Label(self.form_frame, text=f"{field_name}:", font=("Arial", 10, "bold"))
            lbl.grid(row=idx, column=0, sticky="w", padx=5, pady=6)

            entry = tk.Entry(self.form_frame, font=("Arial", 10), bd=2, relief=tk.SUNKEN)
            entry.grid(row=idx, column=1, sticky="ew", padx=5, pady=6)
            self.entries[field_name] = entry

        # Multi-line Text widget row for Address
        lbl_address = tk.Label(self.form_frame, text="Address:", font=("Arial", 10, "bold"))
        lbl_address.grid(row=4, column=0, sticky="nw", padx=5, pady=6)

        self.txt_address = tk.Text(self.form_frame, font=("Arial", 10), height=4, bd=2, relief=tk.SUNKEN)
        self.txt_address.grid(row=4, column=1, sticky="ew", padx=5, pady=6)

        # ----------------------------------------------------
        # 3. ACTIONS FRAME (Using pack() for root-level)
        # ----------------------------------------------------
        self.actions_frame = tk.Frame(self, pady=5)
        self.actions_frame.pack(side=tk.TOP, fill=tk.X, padx=15)

        self.btn_save = tk.Button(
            self.actions_frame, text="Save", width=12, bg="#2E7D32", fg="white", font=("Arial", 10, "bold"), command=self.save_profile
        )
        self.btn_save.pack(side=tk.LEFT, padx=10, expand=True)

        self.btn_clear = tk.Button(
            self.actions_frame, text="Clear", width=12, bg="#D84315", fg="white", font=("Arial", 10, "bold"), command=self.clear_form
        )
        self.btn_clear.pack(side=tk.RIGHT, padx=10, expand=True)

        # ----------------------------------------------------
        # 4. STATUS BAR SECTION
        # ----------------------------------------------------
        self.status_label = tk.Label(
            self, text="Ready", font=("Arial", 9, "italic"), bd=1, relief=tk.SUNKEN, anchor="w", padx=10, pady=3
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def save_profile(self):
        """Validates inputs and displays a status feedback message."""
        profile_data = {name: entry.get().strip() for name, entry in self.entries.items()}
        profile_data["Address"] = self.txt_address.get("1.0", tk.END).strip()

        # Check for empty mandatory values
        empty_fields = [key for key, val in profile_data.items() if not val]

        if empty_fields:
            # Display failing message status feedback
            self.status_label.config(text="⚠️ Error: Missing required information fields.", fg="#C62828")
            messagebox.showwarning("Incomplete Form", f"Please fill out all fields.\nMissing: {', '.join(empty_fields)}")
            return

        # Display successful completion message status feedback
        success_message = f"Profile successfully updated for ID: {profile_data['Student ID']}"
        self.status_label.config(text=f"✅ {success_message}", fg="#2E7D32")
        messagebox.showinfo("Success", "Profile Information Saved Successfully!")

    def clear_form(self):
        """Wipes out all fields completely."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.txt_address.delete("1.0", tk.END)
        self.status_label.config(text="Form cleared. Ready for new input.", fg="#555555")


if __name__ == "__main__":
    app = ProfileForm()
    app.mainloop()
