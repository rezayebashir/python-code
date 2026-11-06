import tkinter as tk
from tkinter import ttk


class DynamicPreferencesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("In-Class Challenge — Dynamic Preferences")
        self.root.geometry("450x480")

        # --- 1. Control Variables ---
        self.notif_enabled_var = tk.BooleanVar(value=True)
        self.frequency_var = tk.StringVar(value="Daily")
        self.volume_var = tk.IntVar(value=50)

        # --- 2. Main Checkbutton Setup ---
        toggle_frame = ttk.LabelFrame(root, text=" Master Settings ", padding=10)
        toggle_frame.pack(fill=tk.X, padx=15, pady=5)

        # Maps named handler 'toggle_notification_widgets' via command
        self.master_check = ttk.Checkbutton(
            toggle_frame,
            text="Enable Notifications",
            variable=self.notif_enabled_var,
            command=self.toggle_notification_widgets
        )
        self.master_check.pack(anchor=tk.W)

        # --- 3. Dependent Controls Frame (Combobox & Scale) ---
        self.controls_frame = ttk.LabelFrame(root, text=" Notification Preferences ", padding=10)
        self.controls_frame.pack(fill=tk.X, padx=15, pady=5)

        # Frequency Label & Combobox
        self.freq_label = ttk.Label(self.controls_frame, text="Update Frequency:")
        self.freq_label.pack(anchor=tk.W, pady=(2, 0))

        self.freq_box = ttk.Combobox(
            self.controls_frame,
            textvariable=self.frequency_var,
            values=["Hourly", "Daily", "Weekly", "Monthly"],
            state="readonly"
        )
        self.freq_box.pack(fill=tk.X, pady=(0, 10))
        # Bind change event to update the status panel immediately
        self.freq_box.bind("<<ComboboxSelected>>", lambda e: self.update_status_display())

        # Volume Label & Scale Slider
        # Changed to a standard tk.Label to safely support coloring custom live feedback loops without TclErrors
        self.vol_label = tk.Label(self.controls_frame, text=f"Alert Volume: {self.volume_var.get()}%", fg="#2c3e50")
        self.vol_label.pack(anchor=tk.W)

        self.vol_scale = ttk.Scale(
            self.controls_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.volume_var,
            command=self.handle_scale_movement
        )
        self.vol_scale.pack(fill=tk.X, pady=(0, 5))

        # --- 4. System Action Buttons ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill=tk.X, padx=15, pady=10)

        self.reset_btn = ttk.Button(btn_frame, text="Reset to Defaults", command=self.reset_to_defaults)
        self.reset_btn.pack(side=tk.LEFT)

        # --- 5. Status Overview Panel ---
        status_frame = ttk.LabelFrame(root, text=" Live Configuration Status ", padding=10)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        self.status_display = tk.Text(status_frame, wrap=tk.WORD, height=6, bg="#f5f6fa", font=("Courier", 10))
        self.status_display.pack(fill=tk.BOTH, expand=True)
        self.status_display.config(state=tk.DISABLED)

        # Initialize initial widget interaction state configurations and text printout outputs
        self.toggle_notification_widgets()

    # --- 6. Named Event Handlers & Core Methods ---
    def toggle_notification_widgets(self):
        """Named handler that shifts interactive widget states dynamically based on master checkbox variable state."""
        if self.notif_enabled_var.get():
            # Enable controls
            self.freq_box.config(state="readonly")
            self.vol_scale.config(state="normal")
            self.vol_label.config(fg="#2c3e50")  # Restore visual contrast on label text
        else:
            # Disable dependent input layout channels completely
            self.freq_box.config(state="disabled")
            self.vol_scale.config(state="disabled")
            self.vol_label.config(fg="#7f8c8d")  # Dim text color out lightly indicating disabled mode

        self.update_status_display()

    def handle_scale_movement(self, value):
        """Named handler updating volume metric integer indicators synchronously during slider slides."""
        self.vol_label.config(text=f"Alert Volume: {int(float(value))}%")
        self.update_status_display()

    def update_status_display(self):
        """Builds a formatted summary visualization stream block inside the protected status panel text box."""
        status_text = "ENABLED" if self.notif_enabled_var.get() else "DISABLED"
        freq_text = self.frequency_var.get() if self.notif_enabled_var.get() else "N/A (Disabled)"
        vol_text = f"{self.volume_var.get()}%" if self.notif_enabled_var.get() else "N/A (Disabled)"

        report = (
            f"========================================\n"
            f"       LIVE SYSTEM PREFERENCES         \n"
            f"========================================\n"
            f"• Notifications Status : {status_text}\n"
            f"• Schedule Interval    : {freq_text}\n"
            f"• Audio Output Volume  : {vol_text}\n"
            f"========================================"
        )

        # Refresh read-only tracking summary panel content fields securely
        self.status_display.config(state=tk.NORMAL)
        self.status_display.delete("1.0", tk.END)
        self.status_display.insert(tk.END, report)
        self.status_display.config(state=tk.DISABLED)

    def reset_to_defaults(self):
        """Named button handler that cleanly forces configuration metrics back to pristine system defaults."""
        self.notif_enabled_var.set(True)
        self.frequency_var.set("Daily")
        self.volume_var.set(50)
        self.vol_label.config(text="Alert Volume: 50%")

        # Sync view framework layouts and state updates explicitly
        self.toggle_notification_widgets()


if __name__ == "__main__":
    window = tk.Tk()
    app = DynamicPreferencesApp(window)
    window.mainloop()
