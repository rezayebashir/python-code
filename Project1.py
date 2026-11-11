import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Tactical Radar Scanner")
canvas = tk.Canvas(root, width=500, height=500, bg="#020d06")
canvas.pack()

cx, cy, radius = 250, 250, 220
angle = 0
targets = [[random.uniform(40, 200), random.uniform(0, 360), 0] for _ in range(7)]

def scan():
    global angle
    canvas.delete("all")

    for r in range(55, 225, 55):
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#0a4d22", width=2)
    canvas.create_line(cx-radius, cy, cx+radius, cy, fill="#0a4d22")
    canvas.create_line(cx, cy-radius, cx, cy+radius, fill="#0a4d22")

    # Sweep trail
    for i in range(15):
        a = math.radians(angle - i * 1.5)
        shade = f"#00{max(20, 240 - i*15):02x}44"
        canvas.create_line(cx, cy, cx + radius * math.cos(a), cy + radius * math.sin(a), fill=shade, width=3)

    # Targets
    for t in targets:
        diff = abs((angle % 360) - t[1])
        if diff < 5: t[2] = 255
        if t[2] > 10:
            rad = math.radians(t[1])
            tx, ty = cx + t[0] * math.cos(rad), cy + t[0] * math.sin(rad)
            col = f"#{t[2]:02x}2222"
            canvas.create_oval(tx-6, ty-6, tx+6, ty+6, fill=col, outline="")
            t[2] = max(0, t[2] - 4)

    angle = (angle + 3) % 360
    root.after(20, scan)

scan()
root.mainloop()
