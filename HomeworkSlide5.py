import tkinter as tk

# Functions for button actions
def save_data():
    # Print entered values to the console
    print("--- Student Registration Data ---")
    print(f"Student ID: {id_entry.get()}")
    print(f"Name:       {name_entry.get()}")
    print(f"Department: {dept_entry.get()}")
    print(f"Semester:   {sem_entry.get()}")
    print("---------------------------------")

def clear_fields():
    # Clear all entry widgets
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    sem_entry.delete(0, tk.END)

# Create the root window
root = tk.Tk()
root.title('Student Registration Form')
root.geometry('350x250')

# Padding configuration for consistency
pad_x = 10
pad_y = 8

# Create Labels and Entry widgets organized in a grid()
# Row 0: Student ID
id_label = tk.Label(root, text="Student ID:")
id_label.grid(row=0, column=0, sticky="w", padx=pad_x, pady=pad_y)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=pad_x, pady=pad_y)

# Row 1: Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0, sticky="w", padx=pad_x, pady=pad_y)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=pad_x, pady=pad_y)

# Row 2: Department
dept_label = tk.Label(root, text="Department:")
dept_label.grid(row=2, column=0, sticky="w", padx=pad_x, pady=pad_y)
dept_entry = tk.Entry(root)
dept_entry.grid(row=2, column=1, padx=pad_x, pady=pad_y)

# Row 3: Semester
sem_label = tk.Label(root, text="Semester:")
sem_label.grid(row=3, column=0, sticky="w", padx=pad_x, pady=pad_y)
sem_entry = tk.Entry(root)
sem_entry.grid(row=3, column=1, padx=pad_x, pady=pad_y)

# Row 4: Save and Clear Buttons
save_button = tk.Button(root, text="Save", command=save_data, width=10)
save_button.grid(row=4, column=0, padx=pad_x, pady=15)

clear_button = tk.Button(root, text="Clear", command=clear_fields, width=10)
clear_button.grid(row=4, column=1, padx=pad_x, pady=15)

# Start the application loop
root.mainloop()
