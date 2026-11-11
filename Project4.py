import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("320x120")

clock_label = tk.Label(root, font=("Arial", 32, "bold"), bg="black", fg="cyan")
clock_label.pack(expand=True, fill="both")

update_time()
root.mainloop()
