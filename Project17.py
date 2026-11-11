import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Apex Neon GT - Supercar Racer")
root.geometry("540x650")
root.resizable(False, False)
root.configure(bg="#090a0f")

player_name = "Driver"

# ==========================================
# 1. SHOWROOM LOGIN PAGE WITH CAR GRAPHIC
# ==========================================
login_frame = tk.Frame(root, bg="#090a0f", width=540, height=650)
login_frame.pack(fill="both", expand=True)

banner = tk.Canvas(login_frame, width=540, height=220, bg="#090a0f", highlightthickness=0)
banner.pack(pady=(10, 0))

# Night City Skyline & Grid Floor
banner.create_rectangle(0, 175, 540, 220, fill="#111827", outline="")
banner.create_line(0, 175, 540, 175, fill="#00f5d4", width=2)
for bx in range(20, 520, 45):
    bh = random.randint(40, 110)
    banner.create_rectangle(bx, 175 - bh, bx + 32, 175, fill="#131722", outline="#1e293b")

# Title Text
banner.create_text(270, 32, text="APEX NEON GT", font=("Consolas", 28, "bold"), fill="#00f5d4")
banner.create_text(270, 58, text="SUPERCAR HIGHWAY EDITION", font=("Consolas", 11, "bold"), fill="#ff2a6d")

# Side-Profile Supercar Illustration
banner.create_oval(125, 166, 415, 178, fill="#00f5d4", outline="")
banner.create_polygon(130, 128, 148, 128, 152, 142, 136, 142, fill="#ff2a6d", outline="white")
banner.create_polygon(
    135, 158, 138, 138, 190, 134, 235, 112,
    315, 114, 365, 136, 412, 146, 415, 160,
    fill="#0284c7", outline="#38bdf8", width=2
)
banner.create_polygon(202, 134, 238, 116, 310, 118, 352, 136, fill="#0f172a", outline="#7dd3fc", width=1)
banner.create_polygon(245, 142, 285, 142, 275, 155, 240, 155, fill="#090a0f", outline="#38bdf8")
banner.create_polygon(412, 148, 520, 130, 520, 172, 414, 156, fill="#fef08a", stipple="gray25", outline="")
banner.create_oval(404, 145, 415, 153, fill="#ffffff", outline="#fef08a")
banner.create_rectangle(135, 140, 141, 148, fill="#ff2a6d", outline="")

# Alloy Wheels
for wx in (185, 360):
    banner.create_oval(wx - 22, 142, wx + 22, 186, fill="#050505", outline="#94a3b8", width=3)
    banner.create_oval(wx - 13, 151, wx + 13, 177, fill="#1e293b", outline="#38bdf8", width=2)
    banner.create_oval(wx - 4, 160, wx + 4, 168, fill="#ff2a6d", outline="")

# Login Input Area
tk.Label(
    login_frame, text="DRIVER REGISTRATION",
    font=("Consolas", 13, "bold"), fg="#94a3b8", bg="#090a0f"
).pack(pady=(15, 5))

tk.Label(
    login_frame, text="Enter Your Name:",
    font=("Consolas", 14), fg="white", bg="#090a0f"
).pack(pady=(5, 8))

name_entry = tk.Entry(
    login_frame, font=("Consolas", 16, "bold"),
    bg="#1e1e26", fg="#00ffcc", insertbackground="white",
    justify="center", width=22, relief="flat", highlightthickness=2,
    highlightbackground="#00f5d4", highlightcolor="#ff2a6d"
)
name_entry.pack(pady=5, ipady=7)
name_entry.focus()

confirm_frame = tk.Frame(login_frame, bg="#090a0f")

question_label = tk.Label(
    confirm_frame, text="",
    font=("Consolas", 13, "bold"), fg="#ffd700", bg="#090a0f", wraplength=460
)
question_label.pack(pady=(20, 15))

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
    question_label.config(text=f"Welcome, {player_name}!\nDo you want to play this game?")
    confirm_frame.pack(pady=5)

def start_game():
    login_frame.destroy()
    canvas.pack()
    loop()

def exit_app():
    root.destroy()

continue_btn = tk.Button(
    login_frame, text="CONTINUE", command=ask_to_play,
    font=("Consolas", 13, "bold"), bg="#00f5d4", fg="#090a0f",
    activebackground="#00ffcc", width=18, relief="flat", cursor="hand2"
)
continue_btn.pack(pady=20, ipady=5)

yes_btn = tk.Button(
    btn_row, text="YES, RACE!", command=start_game,
    font=("Consolas", 13, "bold"), bg="#10b981", fg="white",
    activebackground="#059669", width=12, relief="flat", cursor="hand2"
)
yes_btn.pack(side="left", padx=12, ipady=5)

no_btn = tk.Button(
    btn_row, text="NO, EXIT", command=exit_app,
    font=("Consolas", 13, "bold"), bg="#e11d48", fg="white",
    activebackground="#be123c", width=12, relief="flat", cursor="hand2"
)
no_btn.pack(side="left", padx=12, ipady=5)

name_entry.bind("<Return>", ask_to_play)

# ==========================================
# 2. REALISTIC TOP-DOWN HIGHWAY RACING GAME
# ==========================================
canvas = tk.Canvas(root, width=540, height=650, bg="#0b1f14", highlightthickness=0)

car_x = 270
car_y = 545
lasers = []
enemy_cars = []
coins = []
explosions = []
road_lines = [y for y in range(0, 680, 85)]
trees = [{"x": 38, "y": y} for y in range(40, 650, 150)] + [{"x": 502, "y": y} for y in range(110, 650, 150)]
score = 0
cars_spawned = 0
game_over = False

ENEMY_STYLES = [
    {"body": "#dc2626", "accent": "#fca5a5"},
    {"body": "#d97706", "accent": "#fde68a"},
    {"body": "#7c3aed", "accent": "#ddd6fe"},
    {"body": "#059669", "accent": "#a7f3d0"},
]

def move_car(event):
    global car_x
    car_x = max(112, min(428, event.x))

def shoot(event=None):
    if not game_over:
        lasers.append({"x": car_x - 15, "y": car_y - 42})
        lasers.append({"x": car_x + 15, "y": car_y - 42})

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

def draw_realistic_supercar(x, y, body_col, accent_col, is_player=True):
    canvas.create_oval(x - 26, y - 42, x + 28, y + 46, fill="#090a0f", outline="")

    for wx in (-23, 17):
        canvas.create_rectangle(x + wx, y - 30, x + wx + 6, y - 12, fill="#050505", outline="#475569")
        canvas.create_rectangle(x + wx, y + 12, x + wx + 6, y + 30, fill="#050505", outline="#475569")

    mirror_y = y - 10 if is_player else y + 10
    canvas.create_polygon(x - 21, mirror_y, x - 28, mirror_y + 3, x - 21, mirror_y + 6, fill=body_col, outline="white")
    canvas.create_polygon(x + 21, mirror_y, x + 28, mirror_y + 3, x + 21, mirror_y + 6, fill=body_col, outline="white")

    if is_player:
        canvas.create_polygon(x - 16, y - 40, x - 32, y - 115, x - 4, y - 115, fill="#fef9c3", stipple="gray12", outline="")
        canvas.create_polygon(x + 16, y - 40, x + 4, y - 115, x + 32, y - 115, fill="#fef9c3", stipple="gray12", outline="")
        canvas.create_polygon(
            x - 15, y - 42, x + 15, y - 42,
            x + 22, y - 22, x + 20, y + 25,
            x + 22, y + 40, x - 22, y + 40,
            x - 20, y + 25, x - 22, y - 22,
            fill=body_col, outline="white", width=2
        )
        canvas.create_rectangle(x - 4, y - 41, x + 4, y + 39, fill=accent_col, outline="")
        canvas.create_polygon(x - 9, y - 34, x + 9, y - 34, x + 6, y - 22, x - 6, y - 22, fill="#0f172a", outline="")
        canvas.create_polygon(x - 15, y - 18, x + 15, y - 18, x + 12, y - 2, x - 12, y - 2, fill="#0f172a", outline="#7dd3fc")
        canvas.create_rectangle(x - 12, y - 2, x + 12, y + 16, fill=body_col, outline="#38bdf8")
        canvas.create_polygon(x - 12, y + 16, x + 12, y + 16, x + 14, y + 30, x - 14, y + 30, fill="#0f172a", outline="#475569")
        canvas.create_rectangle(x - 23, y + 35, x + 23, y + 41, fill="#090a0f", outline="#00f5d4", width=1)
        canvas.create_rectangle(x - 17, y - 42, x - 9, y - 38, fill="#ffffff", outline="#fef08a")
        canvas.create_rectangle(x + 9, y - 42, x + 17, y - 38, fill="#ffffff", outline="#fef08a")
        flame_len = random.randint(6, 13)
        canvas.create_oval(x - 11, y + 41, x - 6, y + 41 + flame_len, fill="#00f5d4", outline="")
        canvas.create_oval(x + 6, y + 41, x + 11, y + 41 + flame_len, fill="#00f5d4", outline="")
    else:
        canvas.create_polygon(
            x - 22, y - 40, x + 22, y - 40,
            x + 20, y - 25, x + 22, y + 22,
            x + 15, y + 42, x - 15, y + 42,
            x - 22, y + 22, x - 20, y - 25,
            fill=body_col, outline="white", width=2
        )
        canvas.create_rectangle(x - 4, y - 39, x + 4, y + 41, fill=accent_col, outline="")
        canvas.create_rectangle(x - 23, y - 41, x + 23, y - 35, fill="#090a0f", outline="#fda4af")
        canvas.create_polygon(x - 12, y + 2, x + 12, y + 2, x + 15, y + 18, x - 15, y + 18, fill="#0f172a", outline="#94a3b8")
        canvas.create_polygon(x - 14, y - 30, x + 14, y - 30, x + 12, y - 16, x - 12, y - 16, fill="#0f172a", outline="#475569")
        canvas.create_rectangle(x - 17, y + 38, x - 9, y + 42, fill="#fef08a", outline="")
        canvas.create_rectangle(x + 9, y + 38, x + 17, y + 42, fill="#fef08a", outline="")

def spawn_explosion(x, y, color="#ffbe0b"):
    for _ in range(16):
        explosions.append({
            "x": x,
            "y": y,
            "vx": random.uniform(-4.5, 4.5),
            "vy": random.uniform(-4.5, 4.5),
            "life": 18,
            "color": color
        })

def loop():
    global score, cars_spawned, game_over
    canvas.delete("all")

    canvas.create_rectangle(75, 0, 465, 650, fill="#1c1c24", outline="")
    for i in range(len(road_lines)):
        road_lines[i] = (road_lines[i] + 4.5) % 680
        y = road_lines[i] - 40
        curb_col = "#e11d48" if i % 2 == 0 else "#f8fafc"
        canvas.create_rectangle(70, y, 82, y + 85, fill=curb_col, outline="")
        canvas.create_rectangle(458, y, 470, y + 85, fill=curb_col, outline="")
        canvas.create_rectangle(205, y + 15, 213, y + 60, fill="#e2e8f0", outline="")
