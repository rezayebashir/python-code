import tkinter as tk


class KeyboardEventViewer:

    def __init__(self, root):
        self.root = root
        self.root.title("Practical Lab 2 — Keyboard Event Viewer")
        self.root.geometry("500x350")

        # 1. Main Label to display the last key pressed details
        self.header_label = tk.Label(
            self.root, text="Press any key...", font=("Arial", 14, "bold")
        )
        self.header_label.pack(pady=15)

        self.display_label = tk.Label(
            self.root,
            text="Key Symbol: None\nCharacter: None",
            font=("Courier", 12),
            justify=tk.LEFT,
            bg="#f0f0f0",
            padx=10,
            pady=10,
            width=30,
            relief=tk.SUNKEN,
        )
        self.display_label.pack(pady=10)

        # Status strip at the bottom for messages (like Ctrl+S)
        self.status_label = tk.Label(
            self.root,
            text="Status: Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Arial", 10),
            bg="lightyellow",
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        # 6. Add an Entry widget to compare event behaviors when focused
        self.entry_label = tk.Label(
            self.root,
            text="Type below to test events while focused inside an Entry:",
            font=("Arial", 10),
        )
        self.entry_label.pack(pady=(15, 2))

        self.entry_widget = tk.Entry(self.root, font=("Arial", 11), width=35)
        self.entry_widget.pack(pady=5)

        # 2. Bind <KeyPress> globally to the root window
        self.root.bind("<KeyPress>", self.on_key_press)

        # 4. Bind <Escape> specifically to clear the display labels
        self.root.bind("<Escape>", self.clear_display)

        # 5. Bind Ctrl+S (case insensitive handling for 's' and 'S')
        self.root.bind("<Control-s>", self.show_saved_status)
        self.root.bind("<Control-S>", self.show_saved_status)

    # 3. Handle keypress and display event.keysym and event.char
    def on_key_press(self, event):
        # Ignore Escape and Control modifiers to avoid overwriting their dedicated actions
        if event.keysym in ["Escape", "Control_L", "Control_R"]:
            return

        # Handle empty/non-printable characters securely
        char_disp = (
            repr(event.char)
            if event.char and event.char.isprintable()
            else f"'{event.char}'" if event.char else "None"
        )

        self.display_label.config(
            text=f"Key Symbol: {event.keysym}\nCharacter: {char_disp}"
        )
        self.status_label.config(text="Status: Key captured")

    # 4. Function to clear display values
    def clear_display(self, event):
        self.display_label.config(text="Key Symbol: None\nCharacter: None")
        self.status_label.config(text="Status: Display Cleared via Escape")

    # 5. Function to trigger the 'Saved' notification
    def show_saved_status(self, event):
        self.status_label.config(text="Status: File Saved Successfully! (Ctrl+S)")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardEventViewer(root)
    root.mainloop()
