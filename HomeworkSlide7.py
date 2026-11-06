import tkinter as tk


class MouseEventTracker:

    def __init__(self, root):
        self.root = root
        self.root.title("Practical Lab 1 — Mouse Event Tracker")
        self.root.geometry("500x400")

        # Initialize double click counter
        self.double_click_count = 0

        # 1. Create a status Label at the bottom
        self.status_label = tk.Label(
            self.root,
            text="Status: Outside Frame",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Arial", 10),
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

        # Labels to display feedback inside the GUI
        self.coord_label = tk.Label(
            self.root, text="Coordinates: X: 0, Y: 0", font=("Arial", 12)
        )
        self.coord_label.pack(pady=5)

        self.click_label = tk.Label(
            self.root, text="Last Action: None", font=("Arial", 12)
        )
        self.click_label.pack(pady=5)

        self.counter_label = tk.Label(
            self.root, text="Double Clicks: 0", font=("Arial", 12)
        )
        self.counter_label.pack(pady=5)

        # 2. Create a window with a large Frame
        self.frame = tk.Frame(
            self.root, bg="lightgray", width=450, height=250, relief=tk.RAISED
        )
        self.frame.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        # Bind all required mouse events to the Frame
        self.frame.bind("<Motion>", self.track_motion)
        self.frame.bind("<Button-1>", self.track_left_click)
        self.frame.bind("<Double-Button-1>", self.track_double_click)
        self.frame.bind("<Enter>", self.track_enter)
        self.frame.bind("<Leave>", self.track_leave)

    # 3. Bind <Motion> to show current x/y coordinates
    def track_motion(self, event):
        self.coord_label.config(text=f"Coordinates: X: {event.x}, Y: {event.y}")

    # 4. Bind <Button-1> to display 'Left Click'
    def track_left_click(self, event):
        self.click_label.config(text="Last Action: Left Click")

    # 5. Bind <Double-Button-1> to count double clicks
    def track_double_click(self, event):
        self.double_click_count += 1
        self.counter_label.config(
            text=f"Double Clicks: {self.double_click_count}"
        )
        self.click_label.config(text="Last Action: Double Click")

    # 6. Bind <Enter> and <Leave> to update a status Label
    def track_enter(self, event):
        self.status_label.config(text="Status: Inside Frame")

    def track_leave(self, event):
        self.status_label.config(text="Status: Outside Frame")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MouseEventTracker(root)
    root.mainloop()
