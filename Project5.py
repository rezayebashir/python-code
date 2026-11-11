import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        chars = string.ascii_letters + string.digits + "!@#$%"
        password = "".join(random.choice(chars) for _ in range(length))
        pass_entry.delete(0, tk.END)
        pass_entry.insert(0, password)
    except ValueError:
        pass_entry.delete(0, tk.END)
        pass_entry.insert(0, "Invalid length")

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=10)

pass_entry = tk.Entry(root, width=28, justify="center", font=("Arial", 11))
pass_entry.pack(pady=5)

root.mainloop()
