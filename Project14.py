
import tkinter as tk
import random

root = tk.Tk()
root.title("Procedural Fire Engine")
canvas = tk.Canvas(root, width=500, height=450, bg="#050505")
canvas.pack()

particles = []

def get_fire_color(life):
    if life > 35: return "#ffffff"
    if life > 25: return "#ffea00"
    if life > 15: return "#ff6d00"
    if life > 7:  return "#d50000"
    return "#333333"

def burn():
    canvas.delete("all")
    for _ in range(8):
        particles.append({
            "x": 250 + random.uniform(-35, 35),
            "y": 400,
            "vx": random.uniform(-1.2, 1.2),
            "vy": random.uniform(-5, -2.5),
            "life": random.randint(30, 48)
        })

    for p in particles[:]:
        p["x"] += p["vx"] + random.uniform(-0.8, 0.8)
        p["y"] += p["vy"]
        p["life"] -= 1
        r = max(2, p["life"] * 0.45)
        col = get_fire_color(p["life"])
        canvas.create_oval(p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r, fill=col, outline="")
        if p["life"] <= 0:
            particles.remove(p)

    root.after(20, burn)

burn()
root.mainloop()
