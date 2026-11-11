import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Neon Spectrum Equalizer")
canvas = tk.Canvas(root, width=640, height=360, bg="#09090b")
canvas.pack()

bars = 32
heights = [20] * bars
peaks = [20] * bars
t = 0

def animate():
    global t
    canvas.delete("all")
    t += 0.15
    bar_w = 16

    for i in range(bars):
        wave = (math.sin(i * 0.3 + t) + 1) * 90 + (math.cos(i * 0.7 - t * 1.5) + 1) * 50
        target_h = wave + random.randint(0, 35)
        heights[i] += (target_h - heights[i]) * 0.3

        if heights[i] > peaks[i]:
            peaks[i] = heights[i]
        else:
            peaks[i] = max(10, peaks[i] - 2.5)

        x = 20 + i * 19
        y = 330 - heights[i]
        py = 330 - peaks[i]

        r = min(255, int(heights[i]))
        g = max(50, 255 - int(heights[i] * 0.8))
        canvas.create_rectangle(x, y, x + bar_w, 330, fill=f"#{r:02x}{g:02x}ff", outline="")
        canvas.create_rectangle(x, py - 4, x + bar_w, py, fill="#ffffff", outline="")

    root.after(25, animate)

animate()
root.mainloop()
