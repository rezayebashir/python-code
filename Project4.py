import tkinter as tk
import random

root = tk.Tk()
root.title("3D Starfield")
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

stars = [[random.uniform(-250, 250), random.uniform(-250, 250), random.uniform(1, 500)] for _ in range(120)]

def warp():
    canvas.delete("all")
    for s in stars:
        s[2] -= 8
        if s[2] <= 1:
            s[0], s[1], s[2] = random.uniform(-250, 250), random.uniform(-250, 250), 500

        sx = 250 + (s[0] / s[2]) * 250
        sy = 250 + (s[1] / s[2]) * 250
        size = max(1, (1 - s[2] / 500) * 5)
        canvas.create_oval(sx, sy, sx+size, sy+size, fill="white", outline="")

    root.after(20, warp)

warp()
root.mainloop()
