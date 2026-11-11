import tkinter as tk
import math

root = tk.Tk()
root.title("Solar System Orbit")
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

cx, cy = 250, 250
canvas.create_oval(cx-25, cy-25, cx+25, cy+25, fill="gold", outline="")

planets = [
    {"dist": 60, "size": 6, "speed": 0.05, "angle": 0, "color": "gray"},
    {"dist": 100, "size": 10, "speed": 0.03, "angle": 1, "color": "deepskyblue"},
    {"dist": 150, "size": 8, "speed": 0.02, "angle": 2, "color": "tomato"},
    {"dist": 210, "size": 16, "speed": 0.01, "angle": 3, "color": "orange"},
]

for p in planets:
    d = p["dist"]
    canvas.create_oval(cx-d, cy-d, cx+d, cy+d, outline="#222")
    p["id"] = canvas.create_oval(0, 0, 0, 0, fill=p["color"])

def animate():
    for p in planets:
        p["angle"] += p["speed"]
        x = cx + p["dist"] * math.cos(p["angle"])
        y = cy + p["dist"] * math.sin(p["angle"])
        s = p["size"]
        canvas.coords(p["id"], x-s, y-s, x+s, y+s)
    root.after(20, animate)

animate()
root.mainloop()
