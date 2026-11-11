import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Plexus Constellation Network")
canvas = tk.Canvas(root, width=600, height=450, bg="#0a0e17")
canvas.pack()

nodes = [[random.uniform(0, 600), random.uniform(0, 450),
          random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5)] for _ in range(45)]
mouse = [-100, -100]

canvas.bind("<Motion>", lambda e: mouse.__setitem__(slice(None), [e.x, e.y]))

def update():
    canvas.delete("all")
    all_pts = nodes + [[mouse[0], mouse[1], 0, 0]]

    for n in nodes:
        n[0] += n[2]
        n[1] += n[3]
        if n[0] <= 0 or n[0] >= 600: n[2] *= -1
        if n[1] <= 0 or n[1] >= 450: n[3] *= -1
        canvas.create_oval(n[0]-3, n[1]-3, n[0]+3, n[1]+3, fill="#00f5d4", outline="")

    for i in range(len(all_pts)):
        for j in range(i + 1, len(all_pts)):
            dist = math.hypot(all_pts[i][0] - all_pts[j][0], all_pts[i][1] - all_pts[j][1])
            if dist < 105:
                intensity = int((1 - dist / 105) * 200)
                col = f"#00{intensity:02x}{min(255, intensity+40):02x}"
                canvas.create_line(all_pts[i][0], all_pts[i][1], all_pts[j][0], all_pts[j][1], fill=col, width=1)

    root.after(20, update)

update()
root.mainloop()
