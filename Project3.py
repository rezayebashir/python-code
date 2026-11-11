import tkinter as tk

root = tk.Tk()
root.title("Brick Breaker")
canvas = tk.Canvas(root, width=480, height=400, bg="#1a1a2e")
canvas.pack()

paddle = canvas.create_rectangle(190, 360, 290, 375, fill="cyan", outline="")
ball = canvas.create_oval(230, 300, 246, 316, fill="white", outline="")
vx, vy = 4, -4

bricks = []
for row in range(4):
    for col in range(8):
        x1, y1 = col * 60 + 4, row * 25 + 30
        b = canvas.create_rectangle(x1, y1, x1+52, y1+18, fill="#e94560", outline="")
        bricks.append(b)

canvas.bind("<Motion>", lambda e: canvas.coords(paddle, e.x-50, 360, e.x+50, 375))

def play():
    global vx, vy
    canvas.move(ball, vx, vy)
    bx1, by1, bx2, by2 = canvas.coords(ball)
    px1, py1, px2, py2 = canvas.coords(paddle)

    if bx1 <= 0 or bx2 >= 480: vx = -vx
    if by1 <= 0: vy = -vy
    if by2 >= py1 and px1 <= (bx1+bx2)/2 <= px2: vy = -abs(vy)

    for b in bricks[:]:
        x1, y1, x2, y2 = canvas.coords(b)
        if x1 < bx2 and x2 > bx1 and y1 < by2 and y2 > by1:
            canvas.delete(b)
            bricks.remove(b)
            vy = -vy
            break

    if by2 < 400 and bricks:
        root.after(16, play)
    else:
        msg = "YOU WIN!" if not bricks else "GAME OVER"
        canvas.create_text(240, 200, text=msg, fill="yellow", font=("Arial", 24, "bold"))

play()
root.mainloop()
