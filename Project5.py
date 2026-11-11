
import tkinter as tk
import math

root = tk.Tk()
root.title("Double Pendulum Chaos")
canvas = tk.Canvas(root, width=600, height=500, bg="#0d1117")
canvas.pack()

r1, r2 = 120, 120
m1, m2 = 15, 15
a1, a2 = math.pi / 1.5, math.pi / 1.2
v1, v2 = 0, 0
g = 0.8
trail = []

def step():
    global a1, a2, v1, v2
    canvas.delete("all")

    num1 = -g * (2 * m1 + m2) * math.sin(a1) - m2 * g * math.sin(a1 - 2 * a2)
    num2 = -2 * math.sin(a1 - a2) * m2 * (v2**2 * r2 + v1**2 * r1 * math.cos(a1 - a2))
    den = r1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    acc1 = (num1 + num2) / den

    num3 = 2 * math.sin(a1 - a2) * (v1**2 * r1 * (m1 + m2) + g * (m1 + m2) * math.cos(a1) + v2**2 * r2 * m2 * math.cos(a1 - a2))
    den2 = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    acc2 = num3 / den2

    v1 = (v1 + acc1) * 0.999
    v2 = (v2 + acc2) * 0.999
    a1 += v1
    a2 += v2

    x1 = 300 + r1 * math.sin(a1)
    y1 = 160 + r1 * math.cos(a1)
    x2 = x1 + r2 * math.sin(a2)
    y2 = y1 + r2 * math.cos(a2)

    trail.append((x2, y2))
    if len(trail) > 120: trail.pop(0)
    if len(trail) > 1:
        canvas.create_line(trail, fill="#ff007f", width=2, smooth=True)

    canvas.create_line(300, 160, x1, y1, fill="white", width=3)
    canvas.create_line(x1, y1, x2, y2, fill="white", width=3)
    canvas.create_oval(x1-8, y1-8, x1+8, y1+8, fill="#00e5ff", outline="")
    canvas.create_oval(x2-8, y2-8, x2+8, y2+8, fill="#ff007f", outline="")

    root.after(16, step)

step()
root.mainloop()
