import tkinter as tk


class EventDrivenLoginForm:

    def __init__(self, root):
        self.root = root
        self.root.title("Practical Lab 3 — Event-Driven Login Form")
        self.root.geometry("400x320")
        self.root.resizable(False, False)

        # Main Layout Title
        title_label = tk.Label(
            self.root, text="Account Login", font=("Arial", 16, "bold")
        )
        title_label.pack(pady=15)

        # --- Form Fields Container ---
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        # Username Widget Setup
        tk.Label(form_frame, text="Username:", font=("Arial", 11)).grid(
            row=0, column=0, sticky=tk.W, pady=8, padx=5
        )
        self.username_entry = tk.Entry(
            form_frame, font=("Arial", 11), width=25, bd=2
        )
        self.username_entry.grid(row=0, column=1, pady=8, padx=5)

        # Password Widget Setup
        tk.Label(form_frame, text="Password:", font=("Arial", 11)).grid(
            row=1, column=0, sticky=tk.W, pady=8, padx=5
        )
        self.password_entry = tk.Entry(
            form_frame, font=("Arial", 11), width=25, bd=2, show="*"
        )
        self.password_entry.grid(row=1, column=1, pady=8, padx=5)

        # --- Login Action Button ---
        # Bound command directly triggers the primary handler
        self.login_button = tk.Button(
            self.root,
            text="Login",
            command=self.handle_login,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            width=12,
        )
        self.login_button.pack(pady=15)

        # --- Validation Status Message Strip ---
        self.status_label = tk.Label(
            self.root,
            text="Ready to authenticating...",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Arial", 10),
            bg="#f0f0f0",
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Event Binding Framework ---
        # 1. Pressing Enter dynamically routes to the exact same logic handler
        self.username_entry.bind("<Return>", self.handle_login)
        self.password_entry.bind("<Return>", self.handle_login)

        # 2. FocusIn / FocusOut tracking to highlight active field outlines
        self.username_entry.bind("<FocusIn>", self.on_focus_in)
        self.username_entry.bind("<FocusOut>", self.on_focus_out)
        self.password_entry.bind("<FocusIn>", self.on_focus_in)
        self.password_entry.bind("<FocusOut>", self.on_focus_out)

        # 3. Escape hotkey mapping to instantly wipe out text
        self.root.bind("<Escape>", self.clear_form)

    # --- Event Handler & Clean Helper Functions ---

    def handle_login(self, event=None):
        """Unified validator handler triggered by button press or Return key."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Clean verification workflow
        if not username or not password:
            self.status_label.config(
                text="Validation Error: All fields are required!", bg="#FFCDD2"
            )
        elif username == "admin" and password == "12345":
            self.status_label.config(
                text="Success: Login verified successfully.", bg="#C8E6C9"
            )
        else:
            self.status_label.config(
                text="Authentication Failed: Invalid credentials.", bg="#FFCDD2"
            )

    def clear_form(self, event=None):
        """Clean helper layout function to wipe form values instantly."""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.focus()  # Return active focus back to initial start box
        self.status_label.config(
            text="Form cleared via Escape shortcut.", bg="#E0E0E0"
        )

    def on_focus_in(self, event):
        """Gives an active light blue highlight frame to the selected input field."""
        event.widget.config(highlightbackground="#2196F3", highlightcolor="#2196F3", highlightthickness=2)

    def on_focus_out(self, event):
        """Removes the highlight border when focus is lost."""
        event.widget.config(highlightthickness=0)


if __name__ == "__main__":
    root = tk.Tk()
    app = EventDrivenLoginForm(root)
    root.mainloop()
