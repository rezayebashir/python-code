import tkinter as tk
import random

root = tk.Tk()
root.title("Snake Game")
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

snake = [(100, 100), (80, 100), (60, 100)]
direction = "Right"
food = (200, 200)

def change_dir(new_dir):
    global direction
    opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if new_dir != opposites.get(direction):
        direction = new_dir

root.bind("<Up>", lambda e: change_dir("Up"))
root.bind("<Down>", lambda e: change_dir("Down"))
root.bind("<Left>", lambda e: change_dir("Left"))
root.bind("<Right>", lambda e: change_dir("Right"))

def game_loop():
    global food
    hx, hy = snake[0]
    moves = {"Up": (0, -20), "Down": (0, 20), "Left": (-20, 0), "Right": (20, 0)}
    dx, dy = moves[direction]
    new_head = (hx + dx, hy + dy)

    if new_head in snake or not (0 <= new_head[0] < 400 and 0 <= new_head[1] < 400):
        canvas.create_text(200, 200, text="GAME OVER", fill="red", font=("Arial", 24, "bold"))
        return

    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randrange(0, 400, 20), random.randrange(0, 400, 20))
    else:
        snake.pop()

    canvas.delete("all")
    canvas.create_oval(food[0], food[1], food[0]+20, food[1]+20, fill="red")
    for x, y in snake:
        canvas.create_rectangle(x, y, x+20, y+20, fill="lime", outline="black")

    root.after(120, game_loop)

game_loop()
root.mainloop()
