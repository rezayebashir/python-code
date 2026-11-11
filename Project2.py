import tkinter as tk
import math

root = tk.Tk()
root.title("Verlet Cloth Simulation")
canvas = tk.Canvas(root, width=600, height=500, bg="#111827")
canvas.pack()

cols, rows, spacing = 18, 12, 22
points = []
sticks = []
mouse = [0, 0]

for r in range(rows):
    for c in range(cols):
        x = 110 + c * spacing
        y = 40 + r * spacing
        points.append({"x": x, "y": y, "ox": x, "oy": y, "pinned": (r == 0 and c % 3 == 0)})

for r in range(rows):
    for c in range(cols):
        idx = r * cols + c
        if c < cols - 1: sticks.append((idx, idx + 1))
        if r < rows - 1: sticks.append((idx, idx + cols))

canvas.bind("<Motion>", lambda e: mouse.__setitem__(slice(None), [e.x, e.y]))

def update():
    canvas.delete("all")
    for p in points:
        if not p["pinned"]:
            vx = (p["x"] - p["ox"]) * 0.98
            vy = (p["y"] - p["oy"]) * 0.98 + 0.35
            p["ox"], p["oy"] = p["x"], p["y"]
            p["x"] += vx
            p["y"] += vy
            # Mouse repulsion
            dx, dy = p["x"] - mouse[0], p["y"] - mouse[1]
            dist = math.hypot(dx, dy)
            if dist < 35 and dist > 0:
                p["x"] += (dx / dist) * 5
                p["y"] += (dy / dist) * 5

    for _ in range(3):
        for i, j in sticks:
            p1, p2 = points[i], points[j]
            dx, dy = p2["x"] - p1["x"], p2["y"] - p1["y"]
            dist = math.hypot(dx, dy) or 1
            diff = (spacing - dist) / dist * 0.5
            if not p1["pinned"]:
                p1["x"] -= dx * diff
                p1["y"] -= dy * diff
            if not p2["pinned"]:
                p2["x"] += dx * diff
                p2["y"] += dy * diff

    for i, j in sticks:
        canvas.create_line(points[i]["x"], points[i]["y"], points[j]["x"], points[j]["y"], fill="#38bdf8", width=2)

    root.after(16, update)

update()
root.mainloop()
