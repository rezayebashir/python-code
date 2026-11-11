import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Neon Highway Car Racer")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#090a0f")

player_name = "Player"

# ==========================================
# 1. LOGIN & CONFIRMATION PAGE
# ==========================================
login_frame = tk.Frame(root, bg="#090a0f", width=500, height=600)
login_frame.pack(fill="both", expand=True)

tk.Label(
    login_frame, text="NEON HIGHWAY",
    font=("Consolas", 30, "bold"), fg="#00f5d4", bg="#090a0f"
).pack(pady=(90, 5))

tk.Label(
    login_frame, text="R A C E R",
    font=("Consolas", 18, "bold"), fg="#ff2a6d", bg="#090a0f"
).pack(pady=(0, 40))

tk.Label(
    login_frame, text="Enter Your Name:",
    font=("Consolas", 14), fg="white", bg="#090a0f"
).pack(pady=(0, 10))

name_entry = tk.Entry(
    login_frame, font=("Consolas", 16, "bold"),
    bg="#1e1e26", fg="#00ffcc", insertbackground="white",
    justify="center", width=20, relief="flat", highlightthickness=2,
    highlightbackground="#00f5d4", highlightcolor="#ff2a6d"
)
name_entry.pack(pady=5, ipady=6)
name_entry.focus()

# Hidden confirmation section (appears after entering name)
confirm_frame = tk.Frame(login_frame, bg="#090a0f")

question_label = tk.Label(
    confirm_frame, text="",
    font=("Consolas", 13, "bold"), fg="#ffd700", bg="#090a0f", wraplength=420
)
question_label.pack(pady=(25, 15))

btn_row = tk.Frame(confirm_frame, bg="#090a0f")
btn_row.pack()

def ask_to_play(event=None):
    global player_name
    entered = name_entry.get().strip()
    if not entered:
        messagebox.showwarning("Name Required", "Please enter your name first!")
        return
    player_name = entered
    continue_btn.pack_forget()
    name_entry.config(state="disabled")
    question_label.config(text=f"Hello {player_name}!\nDo you want to play this game?")
    confirm_frame.pack(pady=10)

def start_game():
    login_frame.destroy()
    canvas.pack()
    loop()

def exit_app():
    root.destroy()

continue_btn = tk.Button(
    login_frame, text="CONTINUE", command=ask_to_play,
    font=("Consolas", 13, "bold"), bg="#00f5d4", fg="#090a0f",
    activebackground="#00ffcc", width=16, relief="flat", cursor="hand2"
)
continue_btn.pack(pady=20, ipady=4)

yes_btn = tk.Button(
    btn_row, text="YES", command=start_game,
    font=("Consolas", 13, "bold"), bg="#10b981", fg="white",
    activebackground="#059669", width=10, relief="flat", cursor="hand2"
)
yes_btn.pack(side="left", padx=12, ipady=4)

no_btn = tk.Button(
    btn_row, text="NO", command=exit_app,
    font=("Consolas", 13, "bold"), bg="#e11d48", fg="white",
    activebackground="#be123c", width=10, relief="flat", cursor="hand2"
)
no_btn.pack(side="left", padx=12, ipady=4)

name_entry.bind("<Return>", ask_to_play)

# ==========================================
# 2. MAIN GAME CANVAS & LOGIC
# ==========================================
canvas = tk.Canvas(root, width=500, height=600, bg="#111118", highlightthickness=0)

car_x = 250
car_y = 510
lasers = []
enemy_cars = []
coins = []
explosions = []
road_lines = [y for y in range(0, 600, 80)]
score = 0
cars_spawned = 0
game_over = False

def move_car(event):
    global car_x
    car_x = max(95, min(405, event.x))

def shoot(event=None):
    if not game_over:
        lasers.append({"x": car_x - 14, "y": car_y - 35})
        lasers.append({"x": car_x + 14, "y": car_y - 35})

def restart(event=None):
    global score, cars_spawned, game_over
    if game_over:
        score = 0
        cars_spawned = 0
        game_over = False
        lasers.clear()
        enemy_cars.clear()
        coins.clear()
        explosions.clear()
        loop()

canvas.bind("<Motion>", move_car)
canvas.bind("<Button-1>", shoot)
root.bind("<space>", shoot)
root.bind("<r>", restart)
root.bind("<R>", restart)

def draw_car(x, y, body_color, stripe_color, is_player=True):
    # 4 Tires
    canvas.create_rectangle(x - 24, y - 28, x - 18, y - 12, fill="#050505", outline="gray")
    canvas.create_rectangle(x + 18, y - 28, x + 24, y - 12, fill="#050505", outline="gray")
    canvas.create_rectangle(x - 24, y + 12, x - 18, y + 28, fill="#050505", outline="gray")
    canvas.create_rectangle(x + 18, y + 12, x + 24, y + 28, fill="#050505", outline="gray")

    # Main Car Body
    canvas.create_rectangle(x - 20, y - 35, x + 20, y + 35, fill=body_color, outline="white", width=2)
    # Racing Stripe
    canvas.create_rectangle(x - 4, y - 35, x + 4, y + 35, fill=stripe_color, outline="")
    # Windshield & Cabin Roof
    canvas.create_rectangle(x - 15, y - 15, x + 15, y + 15, fill="#1e293b", outline="#94a3b8")

    # Headlights / Taillights
    if is_player:
        canvas.create_rectangle(x - 16, y - 37, x - 8, y - 33, fill="#fef08a", outline="")
        canvas.create_rectangle(x + 8, y - 37, x + 16, y - 33, fill="#fef08a", outline="")
    else:
        canvas.create_rectangle(x - 16, y + 33, x - 8, y + 37, fill="#ff4d4d", outline="")
        canvas.create_rectangle(x + 8, y + 33, x + 16, y + 37, fill="#ff4d4d", outline="")

def spawn_explosion(x, y, color="#ffbe0b"):
    for _ in range(14):
        explosions.append({
            "x": x, "y": y,
            "vx": random.uniform(-4, 4),
            "vy": random.uniform(-4, 4),
            "life": 16,
            "color": color
        })

def loop():
    global score, cars_spawned, game_over
    canvas.delete("all")

    # 1. Highway Asphalt & Moving Lane Dividers
    canvas.create_rectangle(60, 0, 440, 600, fill="#1e1e26", outline="#00f5d4", width=3)
    for i in range(len(road_lines)):
        road_lines[i] = (road_lines[i] + 4.5) % 600
        y = road_lines[i]
        canvas.create_rectangle(185, y, 193, y + 40, fill="#ffffff", outline="")
        canvas.create_rectangle(307, y, 315, y + 40, fill="#ffffff", outline="")

    # 2. Spawn Enemy Cars & 1 Coin After Every 3 Cars
    if random.random() < 0.022 and (not enemy_cars or enemy_cars[-1]["y"] > 110):
        enemy_cars.append({"x": random.randint(100, 400), "y": -45})
        cars_spawned += 1

        if cars_spawned % 3 == 0:
            coins.append({"x": random.randint(100, 400), "y": -110})

    # 3. Update & Draw Gold Coins
    for c in coins[:]:
        c["y"] += 3.5
        cx, cy = c["x"], c["y"]
        canvas.create_oval(cx - 12, cy - 12, cx + 12, cy + 12, fill="#ffd700", outline="#ffffff", width=2)
        canvas.create_text(cx, cy, text="$", fill="#78350f", font=("Arial", 12, "bold"))

        if abs(car_x - cx) < 30 and abs(car_y - cy) < 42:
            coins.remove(c)
            score += 10
            spawn_explosion(cx, cy, "#ffd700")
            continue

        if cy > 620:
            coins.remove(c)

    # 4. Update & Draw Lasers
    for l in lasers[:]:
        l["y"] -= 11
        canvas.create_rectangle(l["x"] - 2, l["y"] - 12, l["x"] + 2, l["y"], fill="#00ffcc", outline="")
        if l["y"] < 0:
            lasers.remove(l)

    # 5. Update Enemy Cars
    for en in enemy_cars[:]:
        en["y"] += 3.5
        ex, ey = en["x"], en["y"]
        draw_car(ex, ey, "#e11d48", "#fda4af", is_player=False)

        hit = False
        for l in lasers[:]:
            if abs(l["x"] - ex) < 22 and abs(l["y"] - ey) < 35:
                enemy_cars.remove(en)
                lasers.remove(l)
                spawn_explosion(ex, ey, "#ffbe0b")
                score += 20
                hit = True
                break
        if hit:
            continue

        if abs(car_x - ex) < 36 and abs(car_y - ey) < 64:
            spawn_explosion(car_x, car_y, "#ff2a6d")
            game_over = True

        if ey > 640:
            enemy_cars.remove(en)

    # 6. Explosion Particles
    for exp in explosions[:]:
        exp["x"] += exp["vx"]
        exp["y"] += exp["vy"]
        exp["life"] -= 1
        canvas.create_oval(exp["x"] - 3, exp["y"] - 3, exp["x"] + 3, exp["y"] + 3, fill=exp["color"], outline="")
        if exp["life"] <= 0:
            explosions.remove(exp)

    # 7. Draw Player Car, Driver Name & Scoreboard
    if not game_over:
        draw_car(car_x, car_y, "#0284c7", "#38bdf8", is_player=True)
        canvas.create_rectangle(10, 10, 210, 62, fill="#090a0f", outline="#00f5d4")
        canvas.create_text(20, 25, anchor="w", text=f"DRIVER: {player_name[:12]}", fill="#ffd700", font=("Consolas", 11, "bold"))
        canvas.create_text(20, 47, anchor="w", text=f"SCORE : {score}", fill="#00ffcc", font=("Consolas", 13, "bold"))
        root.after(16, loop)
    else:
        canvas.create_rectangle(80, 215, 420, 405, fill="#090a0f", outline="#ff2a6d", width=3)
        canvas.create_text(250, 255, text="CRASHED!", fill="#ff2a6d", font=("Consolas", 28, "bold"))
        canvas.create_text(250, 295, text=f"DRIVER: {player_name}", fill="#ffd700", font=("Consolas", 14, "bold"))
        canvas.create_text(250, 325, text=f"FINAL SCORE: {score}", fill="white", font=("Consolas", 17, "bold"))
        canvas.create_text(250, 370, text="Press 'R' to Drive Again", fill="#00ffcc", font=("Consolas", 12))

root.mainloop()
