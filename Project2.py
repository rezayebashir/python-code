import tkinter as tk
import math

root = tk.Tk()
root.title("Sine Wave Visualizer")
canvas = tk.Canvas(root, width=500, height=300, bg="#0f172a")
canvas.pack()

phase = 0

def draw_wave():
    global phase
    canvas.delete("all")
    points = []
    for x in range(0, 505, 5):
        y = 150 + 60 * math.sin(x * 0.03 + phase)
        points.extend([x, y])
    canvas.create_line(points, fill="#38bdf8", width=4, smooth=True)
    phase += 0.15
    root.after(20, draw_wave)

draw_wave()
root.mainloop()
