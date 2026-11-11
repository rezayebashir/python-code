import tkinter as tk
import random

root = tk.Tk()
root.title("Flappy Bird")
canvas = tk.Canvas(root, width=400, height=500, bg="#70c5ce")
canvas.pack()

bird_y = 250
vy = 0
pipe_x = 400
gap_y = 200
score = 0

root.bind("<space>", lambda e: globals().update(vy=-8))

def loop():
    global bird_y, vy, pipe_x, gap_y, score
    vy += 0.5
    bird_y += vy
    pipe_x -= 4

    if pipe_x < -50:
        pipe_x = 400
        gap_y = random.randint(120, 350)
        score += 1

    canvas.delete("all")
    canvas.create_rectangle(pipe_x, 0, pipe_x+50, gap_y-70, fill="#2ecc71")
    canvas.create_rectangle(pipe_x, gap_y+70, pipe_x+50, 500, fill="#2ecc71")
    canvas.create_oval(80, bird_y-15, 110, bird_y+15, fill="#f1c40f")
    canvas.create_text(200, 40, text=str(score), fill="white", font=("Arial", 28, "bold"))

    hit_pipe = (pipe_x < 110 and pipe_x+50 > 80) and (bird_y-15 < gap_y-70 or bird_y+15 > gap_y+70)
    if hit_pipe or bird_y > 500 or bird_y < 0:
        canvas.create_text(200, 250, text="GAME OVER", fill="red", font=("Arial", 26, "bold"))
        return

    root.after(20, loop)

loop()
root.mainloop()
