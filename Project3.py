import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x350")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack(pady=2)
tk.Button(root, text="Delete Selected", command=delete_task).pack(pady=2)

listbox = tk.Listbox(root, width=35, height=12)
listbox.pack(pady=10)

root.mainloop()
