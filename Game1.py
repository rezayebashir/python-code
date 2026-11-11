
import pygame
import random
import json
import os
import math
import sys

# ==========================================
# INITIALIZATION
# ==========================================

pygame.init()

WIDTH, HEIGHT = 1000, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ENDLESS RUNNER")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 25, 40)
DARK = (20, 30, 55)
BLUE = (65, 150, 230)
GREEN = (60, 190, 120)
RED = (230, 75, 75)
YELLOW = (255, 210, 70)
GREY = (120, 130, 145)

# Fonts
font = pygame.font.SysFont("arial", 25, bold=True)
big_font = pygame.font.SysFont("arial", 65, bold=True)
small_font = pygame.font.SysFont("arial", 18)

# Game settings
GROUND_Y = 490
PLAYER_X = 150
GRAVITY = 2200
JUMP_POWER = -850

# Game states
MENU = "menu"
PLAYING = "playing"
PAUSED = "paused"
GAME_OVER = "game_over"

state = MENU

# High score
SAVE_FILE = "highscore.json"

def load_highscore():
    try:
        with open(SAVE_FILE, "r") as file:
            return json.load(file).get("highscore", 0)
    except (OSError, ValueError, TypeError):
        return 0

def save_highscore(score):
    try:
        with open(SAVE_FILE, "w") as file:
            json.dump({"highscore": score}, file)
    except OSError:
        pass

highscore = load_highscore()

# ==========================================
# PLAYER CLASS
# ==========================================

class Player:

    def __init__(self):
        self.reset()

    def reset(self):
        self.y = GROUND_Y - 70
        self.velocity = 0
        self.width = 48
        self.height = 70
        self.on_ground = True
        self.animation = 0

    def jump(self):
        if self.on_ground:
            self.velocity = JUMP_POWER
            self.on_ground = False

    def update(self, dt):
        self.velocity += GRAVITY * dt
        self.y += self.velocity * dt

        if self.y + self.height >= GROUND_Y:
            self.y = GROUND_Y - self.height
            self.velocity = 0
            self.on_ground = True

        self.animation += dt * 12

    def get_rect(self):
        return pygame.Rect(
            PLAYER_X + 5,
            int(self.y) + 5,
            self.width - 10,
            self.height - 8
        )

    def draw(self, surface):

        x = PLAYER_X
        y = int(self.y)

        # Body
        pygame.draw.rect(
            surface, BLUE,
            (x + 5, y + 20, 38, 42),
            border_radius=10
        )

        # Head
        pygame.draw.circle(
            surface, (245, 190, 145),
            (x + 24, y + 13), 15
        )

        # Hair
        pygame.draw.arc(
            surface, BLACK,
            (x + 9, y - 2, 30, 25),
            0, math.pi, 5
        )

        # Eye
        pygame.draw.circle(
            surface, BLACK,
            (x + 30, y + 12), 2
        )

        # Arms and legs animation
        movement = math.sin(self.animation) * 9

        if not self.on_ground:
            movement = -5

        pygame.draw.line(
            surface, BLACK,
            (x + 12, y + 35),
            (x + 3, y + 45 + movement), 6
        )

        pygame.draw.line(
            surface, BLACK,
            (x + 35, y + 35),
            (x + 45, y + 45 - movement), 6
        )

        pygame.draw.line(
            surface, BLACK,
            (x + 15, y + 60),
            (x + 10, y + 70 + movement), 6
        )

        pygame.draw.line(
            surface, BLACK,
            (x + 34, y + 60),
            (x + 39, y + 70 - movement), 6
        )

# ==========================================
# OBSTACLE CLASS
# ==========================================

class Obstacle:

    def __init__(self, speed):
        self.width = random.randint(30, 48)
        self.height = random.randint(45, 85)

        self.x = WIDTH + 20
        self.y = GROUND_Y - self.height

        self.speed = speed

    def update(self, dt):
        self.x -= self.speed * dt

    def get_rect(self):
        return pygame.Rect(
            int(self.x) + 4,
            self.y + 4,
            self.width - 8,
            self.height - 4
        )

    def draw(self, surface):

        rect = pygame.Rect(
            int(self.x), self.y,
            self.width, self.height
        )

        pygame.draw.rect(
            surface, GREEN,
            rect, border_radius=7
        )

        pygame.draw.rect(
            surface, (35, 120, 80),
            rect, 3, border_radius=7
        )

        # Decorative spikes
        pygame.draw.circle(
            surface, (120, 220, 150),
            (int(self.x) + 10, self.y + 12), 4
        )

# ==========================================
# BACKGROUND
# ==========================================

clouds = [
    [100, 100, 1],
    [400, 150, 0.7],
    [750, 90, 1.2],
    [1100, 170, 0.8]
]

background_offset = 0

def draw_background(dt, moving=True):

    global background_offset

    screen.fill((135, 205, 245))

    # Sun
    pygame.draw.circle(
        screen, (255, 225, 130),
        (820, 100), 48
    )

    # Clouds
    for cloud in clouds:

        cloud[0] -= 35 * cloud[2] * dt if moving else 0

        if cloud[0] < -100:
            cloud[0] = WIDTH + 100

        x, y = int(cloud[0]), int(cloud[1])

        pygame.draw.circle(screen, WHITE, (x, y), 25)
        pygame.draw.circle(screen, WHITE, (x + 25, y - 10), 30)
        pygame.draw.circle(screen, WHITE, (x + 55, y), 25)

    # Mountains
    pygame.draw.polygon(
        screen, (110, 175, 190),
        [(0, 390), (180, 210), (370, 390)]
    )

    pygame.draw.polygon(
        screen, (90, 155, 180),
        [(300, 390), (550, 230), (780, 390)]
    )

    pygame.draw.polygon(
        screen, (110, 175, 190),
        [(650, 390), (850, 240), (1100, 390)]
    )

    # Ground
    pygame.draw.rect(
        screen, (90, 190, 110),
        (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
    )

    pygame.draw.line(
        screen, (40, 130, 80),
        (0, GROUND_Y), (WIDTH, GROUND_Y), 5
    )

    # Moving ground details
    if moving:
        background_offset += 250 * dt

    for i in range(15):
        x = int((i * 85 - background_offset) % WIDTH)

        pygame.draw.line(
            screen, (55, 150, 85),
            (x, GROUND_Y + 35),
            (x - 15, GROUND_Y + 35), 3
        )

# ==========================================
# GAME OBJECTS
# ==========================================

player = Player()

obstacles = []

score = 0
game_speed = 390
spawn_timer = 0
spawn_delay = 1.5

# ==========================================
# RESET GAME
# ==========================================

def reset_game():

    global obstacles, score
    global game_speed, spawn_timer, spawn_delay

    player.reset()

    obstacles = []

    score = 0
    game_speed = 390

    spawn_timer = 0
    spawn_delay = 1.5

# ==========================================
# USER INTERFACE
# ==========================================

def draw_text(text, font_type, color, x, y, center=True):

    image = font_type.render(text, True, color)

    rect = image.get_rect()

    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    screen.blit(image, rect)

def draw_button(text, x, y, width, height):

    rect = pygame.Rect(x, y, width, height)

    mouse = pygame.mouse.get_pos()

    color = BLUE if rect.collidepoint(mouse) else DARK

    pygame.draw.rect(
        screen, color, rect,
        border_radius=12
    )

    pygame.draw.rect(
        screen, WHITE, rect,
        2, border_radius=12
    )

    draw_text(
        text, font, WHITE,
        x + width // 2,
        y + height // 2
    )

    return rect

def draw_hud():

    draw_text(
        f"SCORE: {int(score)}",
        font, WHITE, 25, 25, False
    )

    draw_text(
        f"BEST: {highscore}",
        font, YELLOW, 25, 60, False
    )

    draw_text(
        f"SPEED: {int(game_speed)}",
        small_font, WHITE, 25, 100, False
    )

# ==========================================
# MAIN GAME LOOP
# ==========================================

running = True

while running:

    dt = min(clock.tick(FPS) / 1000, 0.033)

    # ======================================
    # EVENTS
    # ======================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                if state == PLAYING:
                    state = PAUSED

                elif state == PAUSED:
                    state = PLAYING

                elif state == MENU:
                    running = False

            if event.key in (pygame.K_SPACE, pygame.K_UP):

                if state == PLAYING:
                    player.jump()

                elif state == MENU:
                    reset_game()
                    state = PLAYING

                elif state == GAME_OVER:
                    reset_game()
                    state = PLAYING

            if event.key == pygame.K_r and state == GAME_OVER:
                reset_game()
                state = PLAYING

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if state == MENU:

                    if start_button.collidepoint(event.pos):
                        reset_game()
                        state = PLAYING

                    elif exit_button.collidepoint(event.pos):
                        running = False

                elif state == GAME_OVER:

                    if restart_button.collidepoint(event.pos):
                        reset_game()
                        state = PLAYING

                    elif menu_button.collidepoint(event.pos):
                        state = MENU

    # ======================================
    # MENU SCREEN
    # ======================================

    if state == MENU:

        draw_background(dt, False)

        draw_text(
            "ENDLESS RUNNER",
            big_font, DARK,
            WIDTH // 2, 190
        )

        draw_text(
            "A PYTHON + PYGAME ADVENTURE",
            small_font, DARK,
            WIDTH // 2, 245
        )

        start_button = draw_button(
            "START GAME", 370, 320, 260, 60
        )

        exit_button = draw_button(
            "EXIT", 370, 400, 260, 60
        )

        draw_text(
            "Press SPACE to start",
            small_font, DARK,
            WIDTH // 2, 510
        )

    # ======================================
    # PLAYING SCREEN
    # ======================================

    elif state == PLAYING:

        draw_background(dt)

        # Update player
        player.update(dt)
        player.draw(screen)

        # Increase difficulty
        game_speed += 9 * dt

        # Score
        score += dt * 10

        # Spawn obstacles
        spawn_timer += dt

        if spawn_timer >= spawn_delay:

            obstacles.append(
                Obstacle(game_speed)
            )

            spawn_timer = 0

            spawn_delay = random.uniform(1.1, 1.8)

        # Update obstacles
        for obstacle in obstacles:

            obstacle.speed = game_speed
            obstacle.update(dt)
            obstacle.draw(screen)

            # Collision detection
            if player.get_rect().colliderect(
                obstacle.get_rect()
            ):

                state = GAME_OVER

                if int(score) > highscore:
                    highscore = int(score)
                    save_highscore(highscore)

        # Remove obstacles outside screen
        obstacles = [
            obstacle for obstacle in obstacles
            if obstacle.x + obstacle.width > 0
        ]

        draw_hud()

        draw_text(
            "SPACE: JUMP   |   ESC: PAUSE",
            small_font, WHITE,
            WIDTH - 20, 25, False
        )

    # ======================================
    # PAUSE SCREEN
    # ======================================

    elif state == PAUSED:

        draw_background(0, False)

        for obstacle in obstacles:
            obstacle.draw(screen)

        player.draw(screen)

        overlay = pygame.Surface(
            (WIDTH, HEIGHT), pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        draw_text(
            "GAME PAUSED",
            big_font, WHITE,
            WIDTH // 2, 250
        )

        draw_text(
            "Press ESC to continue",
            font, YELLOW,
            WIDTH // 2, 330
        )

    # ======================================
    # GAME OVER SCREEN
    # ======================================

    elif state == GAME_OVER:

        draw_background(0, False)

        for obstacle in obstacles:
            obstacle.draw(screen)

        player.draw(screen)

        overlay = pygame.Surface(
            (WIDTH, HEIGHT), pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))

        draw_text(
            "GAME OVER",
            big_font, RED,
            WIDTH // 2, 190
        )

        draw_text(
            f"YOUR SCORE: {int(score)}",
            font, WHITE,
            WIDTH // 2, 270
        )

        draw_text(
            f"BEST SCORE: {highscore}",
            font, YELLOW,
            WIDTH // 2, 315
        )

        restart_button = draw_button(
            "PLAY AGAIN", 350, 370, 300, 55
        )

        menu_button = draw_button(
            "MAIN MENU", 350, 440, 300, 55
        )

        draw_text(
            "Press R to restart",
            small_font, WHITE,
            WIDTH // 2, 525
        )

    # ======================================
    # DISPLAY
    # ======================================

    pygame.display.flip()

# ==========================================
# EXIT
# ==========================================

pygame.quit()
sys.exit()
