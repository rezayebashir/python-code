import tkinter as tk
import math

root = tk.Tk()
root.title("Neon Kaleidoscope Studio (Drag Mouse to Draw)")
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

cx, cy = 300, 300
last_pos = None
hue = 0

def get_rainbow(h):
    r = int((math.sin(h) + 1) * 127.5)
    g = int((math.sin(h + 2) + 1) * 127.5)
    b = int((math.sin(h + 4) + 1) * 127.5)
    return f"#{r:02x}{g:02x}{b:02x}"

def draw(event):
    global last_pos, hue
    if last_pos:
        x1, y1 = last_pos[0] - cx, last_pos[1] - cy
        x2, y2 = event.x - cx, event.y - cy
        color = get_rainbow(hue)
        hue += 0.08
        for i in range(8):
            ang = i * (math.pi / 4)
            ca, sa = math.cos(ang), math.sin(ang)
            rx1, ry1 = x1 * ca - y1 * sa, x1 * sa + y1 * ca
            rx2, ry2 = x2 * ca - y2 * sa, x2 * sa + y2 * ca
            canvas.create_line(cx + rx1, cy + ry1, cx + rx2, cy + ry2, fill=color, width=3, capstyle=tk.ROUND)
            canvas.create_line(cx - rx1, cy + ry1, cx - rx2, cy + ry2, fill=color, width=3, capstyle=tk.ROUND)
    last_pos = (event.x, event.y)

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", lambda e: globals().update(last_pos=None))
root.bind("<c>", lambda e: canvas.delete("all"))
root.mainloop()
