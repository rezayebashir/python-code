import tkinter as tk


class ProfessionalCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator Layout")
        self.root.geometry("350x450")
        self.root.minsize(300, 400)

        # Configure grid distribution weights for the main window
        self.root.rowconfigure(0, weight=1)  # Display row
        self.root.rowconfigure(1, weight=5)  # Keypad frame row
        self.root.columnconfigure(0, weight=1)

        self._create_display()
        self._create_keypad()

    def _create_display(self):
        """Creates the calculation display entry box at the top."""
        # Use an entry widget with custom font sizes, padding, and alignment
        self.display = tk.Entry(
            self.root,
            font=("Consolas", 24),
            justify="right",
            bd=5,
            relief=tk.FLAT,
            bg="#f4f4f4"
        )
        # Position display at the top, spanning all 4 theoretical columns
        self.display.grid(row=0, column=0, sticky="nsew", padx=10, pady=15)
        self.display.insert(0, "0")  # Placeholder string

    def _create_keypad(self):
        """Creates the grid container and populates all functional buttons."""
        # Dedicated frame container for the grid keypad layout
        keypad_frame = tk.Frame(self.root)
        keypad_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Define the layout blueprint matrix (4x4 layout containing optional C and = keys)
        buttons_layout = [
            ['C', '/', '*', '-'],
            ['7', '8', '9', '+'],
            ['4', '5', '6', '='],
            ['1', '2', '3', '0']
        ]

        # Configure grid configuration weights to make keys expand evenly
        for i in range(4):
            keypad_frame.columnconfigure(i, weight=1)
            keypad_frame.rowconfigure(i, weight=1)

        # Dynamically build and place the buttons based on the grid layout
        for row_idx, row_content in enumerate(buttons_layout):
            for col_idx, char in enumerate(row_content):
                # Stylize buttons depending on whether they are operators or numbers
                btn_color = "#e1e1e1" if char.isdigit() else "#d4d4d4"
                if char == '=': btn_color = "#4CAF50"  # Accent green for equals
                fg_color = "#ffffff" if char == '=' else "#000000"

                btn = tk.Button(
                    keypad_frame,
                    text=char,
                    font=("Arial", 14, "bold"),
                    bg=btn_color,
                    fg=fg_color,
                    relief=tk.GROOVE,
                    activebackground="#bbbbbb"
                )

                # Position button perfectly inside its respective cell grid coordinates
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=3, pady=3)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessionalCalculatorApp(root)
    root.mainloop()
