import tkinter as tk
import random

root = tk.Tk()
root.title("Matrix Rain")
canvas = tk.Canvas(root, width=500, height=400, bg="black")
canvas.pack()

cols = 25
drops = [random.randint(-20, 0) for _ in range(cols)]
chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%"

def rain():
    canvas.delete("all")
    for i in range(cols):
        char = random.choice(chars)
        x = i * 20 + 10
        y = drops[i] * 20
        canvas.create_text(x, y, text=char, fill="#00ff41", font=("Courier", 14, "bold"))
        if y > 400 and random.random() > 0.95:
            drops[i] = 0
        drops[i] += 1
    root.after(50, rain)

rain()
root.mainloop()
