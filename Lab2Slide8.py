import tkinter as tk
from tkinter import filedialog, messagebox


class NotesEditor(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Practical Lab 2 - Notes Editor")
        self.geometry("600x500")
        self.minsize(450, 350)

        # Track state for the Disable/Enable toggle feature
        self.editor_enabled = True

        self._build_layout()

    def _build_layout(self):
        # ----------------------------------------------------
        # 1. HEADER FRAME
        # ----------------------------------------------------
        self.header_frame = tk.Frame(self, bg="#2980B9", pady=10)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.title_label = tk.Label(
            self.header_frame,
            text="Interactive Notes Editor",
            font=("Helvetica", 14, "bold"),
            fg="white",
            bg="#2980B9"
        )
        self.title_label.pack()

        # ----------------------------------------------------
        # 2. MAIN EDITOR TEXT AREA (Configured to expand dynamically)
        # ----------------------------------------------------
        # Use an outer layout containment wrapper frame to support fluid growth properties
        self.editor_frame = tk.Frame(self, padx=10, pady=5)
        self.editor_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add a scrollbar component for robust multi-page editing safety loops
        self.scrollbar = tk.Scrollbar(self.editor_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text Widget creation (Bound to scrollbar actions)
        self.text_editor = tk.Text(
            self.editor_frame,
            font=("Consolas", 11),
            wrap=tk.WORD,
            bd=2,
            relief=tk.SUNKEN,
            yscrollcommand=self.scrollbar.set
        )
        # expand=True ensures the Text area expands vertically/horizontally during resize
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_editor.yview)

        # ----------------------------------------------------
        # 3. ACTION BUTTONS FRAME
        # ----------------------------------------------------
        self.action_frame = tk.Frame(self, pady=8)
        self.action_frame.pack(side=tk.TOP, fill=tk.X, padx=10)

        # Basic action buttons
        self.btn_sample = tk.Button(self.action_frame, text="Insert Sample Text", command=self.insert_sample)
        self.btn_sample.pack(side=tk.LEFT, padx=4)

        self.btn_toggle = tk.Button(self.action_frame, text="Disable Editor", bg="#E67E22", fg="white",
                                    command=self.toggle_state)
        self.btn_toggle.pack(side=tk.LEFT, padx=4)

        self.btn_clear = tk.Button(self.action_frame, text="Clear Canvas", command=self.clear_canvas)
        self.btn_clear.pack(side=tk.LEFT, padx=4)

        # Optional File Handling Action Buttons
        self.btn_save = tk.Button(self.action_frame, text="Save File", bg="#2ECC71", fg="white",
                                  command=self.save_to_file)
        self.btn_save.pack(side=tk.RIGHT, padx=4)

        self.btn_load = tk.Button(self.action_frame, text="Load File", bg="#34495E", fg="white",
                                  command=self.load_from_file)
        self.btn_load.pack(side=tk.RIGHT, padx=4)

        # ----------------------------------------------------
        # 4. STATUS INDICATOR LABEL
        # ----------------------------------------------------
        self.status_label = tk.Label(
            self, text="Status: Ready", font=("Arial", 9, "italic"), bd=1, relief=tk.SUNKEN, anchor="w", padx=10, pady=4
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    # --- Feature Operation Methods ---

    def update_status(self, message):
        """Helper matrix updating status information logs instantly."""
        self.status_label.config(text=f"Status: {message}")

    def clear_canvas(self):
        """Wipes text workspace clear safely considering text state constraint triggers."""
        if not self.editor_enabled:
            messagebox.showwarning("Blocked", "Cannot clear data while the editor workspace is Disabled.")
            return
        self.text_editor.delete("1.0", tk.END)
        self.update_status("Editor canvas wiped clear.")

    def insert_sample(self):
        """Appends sample raw text block data directly into the active editor interface."""
        if not self.editor_enabled:
            messagebox.showwarning("Blocked",
                                   "Cannot input sample content data while the editor workspace is Disabled.")
            return
        sample_string = (
            "--- Practical Lab 2 Sample Notes Entry ---\n"
            "• Tkinter handles layout components seamlessly.\n"
            "• The text widget expands to fit changing workspace viewport scales.\n"
            "• State validation routes block anomalies from breaking runtime behaviors.\n"
        )
        self.text_editor.insert(tk.END, sample_string)
        self.update_status("Sample informational baseline data blocks inserted successfully.")

    def toggle_state(self):
        """Toggles the Text widget state between state options using normal/disabled values."""
        if self.editor_enabled:
            self.text_editor.config(state=tk.DISABLED)
            self.btn_toggle.config(text="Enable Editor", bg="#2980B9")
            self.editor_enabled = False
            self.update_status("Editor workspace Locked (Read-Only).")
        else:
            self.text_editor.config(state=tk.NORMAL)
            self.btn_toggle.config(text="Disable Editor", bg="#E67E22")
            self.editor_enabled = True
            self.update_status("Editor workspace Unlocked (Interactive).")

    # --- Optional File Handling System Routines ---

    def save_to_file(self):
        """Exports content directly into an external plain text text data sheet format."""
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
            )
            if not file_path:  # User cancelled dialogue window tracking
                return

            with open(file_path, "w", encoding="utf-8") as file_stream:
                content = self.text_editor.get("1.0", tk.END)
                file_stream.write(content)

            self.update_status(f"File saved successfully to path directory location.")
            messagebox.showinfo("Success", "Notes archived without script exceptions.")
        except Exception as err:
            messagebox.showerror("IO Write Failure", f"Could not archive data target stream logs: {err}")

    def load_from_file(self):
        """Reads plain text file logs and targets content elements back inside the editor matrix."""
        if not self.editor_enabled:
            messagebox.showwarning("Blocked", "Cannot inject raw external streams while your canvas is disabled.")
            return
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
            )
            if not file_path:  # User cancelled window select routes
                return

            with open(file_path, "r", encoding="utf-8") as file_stream:
                content = file_stream.read()

            self.text_editor.delete("1.0", tk.END)
            self.text_editor.insert(tk.END, content)
            self.update_status("File loaded successfully into the interactive interface.")
        except Exception as err:
            messagebox.showerror("IO Read Failure", f"Could not map target documentation files: {err}")


if __name__ == "__main__":
    app = NotesEditor()
    app.mainloop()
