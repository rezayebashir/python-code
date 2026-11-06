import tkinter as tk

# 1. Create a root window
root = tk.Tk()

# 2. Set the window title
root.title('Advanced Programming Lab')

# 3. Set an initial size (Width x Height) and minimum size
root.geometry('400x350')
root.minsize(300, 250)

# 4. Add a heading Label
heading_label = tk.Label(
    root,
    text="Welcome to the Lab",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
# 5 & 6. Use pack() with padding, and make this region fill horizontally (fill=tk.X)
heading_label.pack(fill=tk.X, padx=10, pady=15)

# 7. Add three Buttons
button1 = tk.Button(root, text="Action 1", font=("Arial", 11))
button1.pack(pady=10)

button2 = tk.Button(root, text="Action 2", font=("Arial", 11))
button2.pack(pady=10)

button3 = tk.Button(root, text="Action 3", font=("Arial", 11))
button3.pack(pady=10)

# 8. Start the main event loop to allow normal closing using window controls
root.mainloop()
