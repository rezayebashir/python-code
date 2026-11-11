import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Analog Clock")
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

cx, cy, r = 150, 150, 120
canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=4, outline="#333")

def draw_hand(angle_deg, length, width, color):
    rad = math.radians(angle_deg - 90)
    x = cx + length * math.cos(rad)
    y = cy + length * math.sin(rad)
    canvas.create_line(cx, cy, x, y, width=width, fill=color, tags="hands")

def update_clock():
    canvas.delete("hands")
    t = time.localtime()
    sec_angle = t.tm_sec * 6
    min_angle = t.tm_min * 6 + t.tm_sec * 0.1
    hr_angle = (t.tm_hour % 12) * 30 + t.tm_min * 0.5

    draw_hand(hr_angle, 60, 6, "#222")
    draw_hand(min_angle, 90, 4, "#444")
    draw_hand(sec_angle, 105, 2, "red")
    root.after(200, update_clock)

update_clock()
root.mainloop()
