import tkinter as tk
import random

root = tk.Tk()
root.title("Particle Fountain")
canvas = tk.Canvas(root, width=500, height=400, bg="#111")
canvas.pack()

particles = []
mouse_pos = [250, 200]
colors = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4", "#6a4c93"]

def track_mouse(event):
    mouse_pos[0], mouse_pos[1] = event.x, event.y

canvas.bind("<Motion>", track_mouse)

def update():
    canvas.delete("all")
    for _ in range(3):
        particles.append({
            "x": mouse_pos[0], "y": mouse_pos[1],
            "vx": random.uniform(-3, 3), "vy": random.uniform(-6, -1),
            "life": 30, "color": random.choice(colors)
        })

    for p in particles[:]:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["vy"] += 0.25
        p["life"] -= 1
        r = max(1, p["life"] // 4)
        canvas.create_oval(p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r, fill=p["color"], outline="")
        if p["life"] <= 0:
            particles.remove(p)

    root.after(20, update)

update()
root.mainloop()
