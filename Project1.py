import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=f"Count: {count}")

def reset():
    global count
    count = 0
    label.config(text="Count: 0")

root = tk.Tk()
root.title("Click Counter")
root.geometry("250x180")

label = tk.Label(root, text="Count: 0", font=("Arial", 20))
label.pack(pady=20)

btn_click = tk.Button(root, text="Click Me", command=increase, width=15)
btn_click.pack(pady=5)

btn_reset = tk.Button(root, text="Reset", command=reset, width=15)
btn_reset.pack(pady=5)

root.mainloop()
