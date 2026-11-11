import tkinter as tk

def convert():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        result_label.config(text="Enter a valid number")

root = tk.Tk()
root.title("Temp Converter")
root.geometry("300x180")

tk.Label(root, text="Enter Celsius:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

root.mainloop()
