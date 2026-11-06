import tkinter as tk

# Create the root window
root = tk.Tk()
root.title('Responsive Layout Lab')
root.geometry('400x300')
root.minsize(300, 200)

# 1 & 2. Create and arrange the three main regions using pack()
# Header Frame
header_frame = tk.Frame(root, bg="lightblue", height=50)
header_frame.pack(fill=tk.X, side=tk.TOP)

header_label = tk.Label(header_frame, text="Header Region", bg="lightblue", font=("Arial", 12, "bold"))
header_label.pack(pady=10)

# Content Frame (Allowed to expand to fill empty vertical space)
content_frame = tk.Frame(root, bg="lightgray")
content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Footer Frame
footer_frame = tk.Frame(root, bg="darkgray", height=40)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

footer_label = tk.Label(footer_frame, text="Footer Region © 2026", bg="darkgray", fg="white")
footer_label.pack(pady=5)


# 3. Use grid() inside the content Frame
label_input = tk.Label(content_frame, text="Search:", bg="lightgray")
label_input.grid(row=0, column=0, padx=5, pady=20, sticky="w")

# 5. Use sticky='ew' so the Entry expands horizontally when the window grows
entry_input = tk.Entry(content_frame)
entry_input.grid(row=0, column=1, padx=5, pady=20, sticky="ew")


# 4. Configure grid column 1 (the Entry column) with weight=1
# This lets the column absorb extra horizontal space when resized
content_frame.columnconfigure(1, weight=1)

# Start the main loop
root.mainloop()
