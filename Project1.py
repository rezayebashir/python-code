import tkinter as tk

root = tk.Tk()
root.title("Bouncing Ball Physics")
canvas = tk.Canvas(root, width=500, height=400, bg="#1e1e2e")
canvas.pack()

ball = canvas.create_oval(230, 50, 270, 90, fill="#ff6b6b", outline="")
vx, vy = 4, 0
gravity = 0.5
bounce = 0.85

def animate():
    global vx, vy
    vy += gravity
    canvas.move(ball, vx, vy)
    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= 500:
        vx = -vx
    if y2 >= 400:
        vy = -vy * bounce
        canvas.coords(ball, x1, 360, x2, 400)

    root.after(16, animate)

animate()
root.mainloop()
