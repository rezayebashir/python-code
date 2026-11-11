import tkinter as tk
import math

root = tk.Tk()
root.title("3D Wireframe Projection Engine")
canvas = tk.Canvas(root, width=600, height=500, bg="#090a0f")
canvas.pack()

vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1),  (1, -1, 1),  (1, 1, 1),  (-1, 1, 1)
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

angle = 0

def project(x, y, z):
    fov = 400
    distance = 4
    factor = fov / (distance + z)
    return 300 + x * factor, 250 + y * factor

def render():
    global angle
    canvas.delete("all")
    projected = []
    for x, y, z in vertices:
        # Rotate Y
        rx = x * math.cos(angle) - z * math.sin(angle)
        rz = x * math.sin(angle) + z * math.cos(angle)
        # Rotate X
        ry = y * math.cos(angle * 0.7) - rz * math.sin(angle * 0.7)
        rz = y * math.sin(angle * 0.7) + rz * math.cos(angle * 0.7)
        px, py = project(rx, ry, rz)
        projected.append((px, py))
        canvas.create_oval(px-4, py-4, px+4, py+4, fill="#00f2fe", outline="")

    for i, j in edges:
        x1, y1 = projected[i]
        x2, y2 = projected[j]
        canvas.create_line(x1, y1, x2, y2, fill="#4facfe", width=3)

    angle += 0.03
    root.after(16, render)

render()
root.mainloop()
