import tkinter as tk
import math

root = tk.Tk()
root.title("Inverse Kinematics Tentacle")
canvas = tk.Canvas(root, width=600, height=500, bg="#0b0c10")
canvas.pack()

num_segments = 25
seg_len = 16
segments = [[300, 250] for _ in range(num_segments)]
target = [300, 250]

canvas.bind("<Motion>", lambda e: target.__setitem__(slice(None), [e.x, e.y]))

def follow(seg, tx, ty):
    dx = tx - seg[0]
    dy = ty - seg[1]
    angle = math.atan2(dy, dx)
    seg[0] = tx - math.cos(angle) * seg_len
    seg[1] = ty - math.sin(angle) * seg_len

def animate():
    canvas.delete("all")
    follow(segments[0], target[0], target[1])
    for i in range(1, num_segments):
        follow(segments[i], segments[i-1][0], segments[i-1][1])

    for i in range(num_segments - 1):
        width = max(2, 16 - i * 0.5)
        color = f"#00{min(255, 120 + i*5):02x}ff"
        canvas.create_line(segments[i][0], segments[i][1], segments[i+1][0], segments[i+1][1],
                           fill=color, width=width, capstyle=tk.ROUND)

    root.after(16, animate)

animate()
root.mainloop()
