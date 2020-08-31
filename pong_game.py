import pygame
pygame.init()

def move_bat_with_mouse(current_mouse_pos, last_mouse_pos):
    global BAT_WIDTH, BAT_HEIGHT, bat_pos_x, bat_pos_y
    pygame.draw.rect(screen, BACK_GRD_COLOR, pygame.Rect((bat_pos_x, bat_pos_y), (BAT_WIDTH, BAT_HEIGHT)))  # bat background reset, before moving it
    pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect((0, 0), (SCREEN_WIDTH, BORDER_WIDTH)))
    pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect((0, SCREEN_HEIGHT - BORDER_WIDTH), (SCREEN_WIDTH, BORDER_WIDTH)))
    if current_mouse_pos[1] > last_mouse_pos[1] and bat_pos_y < (SCREEN_HEIGHT - BORDER_WIDTH - BAT_HEIGHT):
        bat_pos_y += BAT_SPEED
    elif current_mouse_pos[1] < last_mouse_pos[1] and bat_pos_y > BORDER_WIDTH:
        bat_pos_y -= BAT_SPEED
    pygame.draw.rect(screen, BAT_COLOR, pygame.Rect((bat_pos_x, bat_pos_y), (BAT_WIDTH, BAT_HEIGHT)))

def move_bat_with_key(keystroke):
    global BORDER_WIDTH, SCREEN_HEIGHT, BAT_HEIGHT, BAT_WIDTH, BAT_SPEED, BAT_SPEED_WITH_KEY, bat_pos_x, bat_pos_y
    pygame.draw.rect(screen, BACK_GRD_COLOR, pygame.Rect((bat_pos_x, bat_pos_y), (BAT_WIDTH, BAT_HEIGHT)))   # bat background reset, before moving it to new position
    if keystroke == pygame.K_UP:
        if bat_pos_y > BORDER_WIDTH:
            bat_pos_y -= BAT_SPEED_WITH_KEY
    if keystroke == pygame.K_DOWN:
        if bat_pos_y < (SCREEN_HEIGHT - BORDER_WIDTH - BAT_HEIGHT):
            bat_pos_y += BAT_SPEED_WITH_KEY
    pygame.draw.rect(screen, BAT_COLOR, pygame.Rect((bat_pos_x, bat_pos_y), (BAT_WIDTH, BAT_HEIGHT)))

def move_ball():
    global BAT_WIDTH, BAT_HEIGHT, BALL_RADIUS, BALL_SPEED, BAT_HEIGHT, GAME_SPEED, curr_score, gameover_flag,  ball_pos_x, ball_pos_y, ball_direction_x, ball_direction_y, bat_pos_y, bat_pos_x, last_mouse_pos
    pygame.draw.circle(screen, BACK_GRD_COLOR, (ball_pos_x, ball_pos_y), BALL_RADIUS)   # ball background reset, before moving it to new position
    if ball_pos_x <= (BORDER_WIDTH + BALL_RADIUS):
        ball_direction_x = "west"
    elif ball_pos_x == (SCREEN_WIDTH - BAT_WIDTH - BALL_RADIUS):
        if (ball_pos_y < bat_pos_y-BALL_RADIUS) or (ball_pos_y > (bat_pos_y + BAT_HEIGHT+BALL_RADIUS)):
            ball_direction_x = "west"
        else:
            ball_direction_x = "east"
            curr_score += 1
            GAME_SPEED += 100
            inplay_score("Score: ", 16, BORDER_WIDTH, BORDER_WIDTH, True)
    elif ball_pos_x > (SCREEN_WIDTH + BALL_RADIUS):
        gameover_flag = True

    if ball_pos_y <= (BORDER_WIDTH + BALL_RADIUS):
        ball_direction_y = "south"
    elif ball_pos_y >= (SCREEN_HEIGHT - BORDER_WIDTH - BALL_RADIUS):
        ball_direction_y = "north"

    if ball_direction_x == "west":
        ball_pos_x += BALL_SPEED
    elif ball_direction_x == "east":
        ball_pos_x -= BALL_SPEED

    if ball_direction_y == "south":
        ball_pos_y += BALL_SPEED
    elif ball_direction_y == "north":
        ball_pos_y -= BALL_SPEED

    pygame.draw.circle(screen, BALL_COLOR, (ball_pos_x, ball_pos_y), BALL_RADIUS)

def run_game():
    global last_mouse_pos, bat_pos_x, bat_pos_y, ball_pos_x, ball_pos_y, ball_direction_x, ball_direction_y, gameover_flag
    screen.fill(BACK_GRD_COLOR)
    pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect((0,0),(SCREEN_WIDTH, BORDER_WIDTH)))     # top border
    pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect((0,SCREEN_HEIGHT-BORDER_WIDTH),(SCREEN_WIDTH, BORDER_WIDTH)))     # bottom border
    pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect((0,0),(BORDER_WIDTH, SCREEN_HEIGHT)))     # left border
    pygame.draw.rect(screen, BAT_COLOR,pygame.Rect((bat_pos_x, bat_pos_y),(BAT_WIDTH, BAT_HEIGHT)))     # bat
    pygame.draw.circle(screen, BALL_COLOR, (ball_pos_x, ball_pos_y), BALL_RADIUS)     # ball
    while True:
        move_ball()
        current_mouse_pos = pygame.mouse.get_pos()
        move_bat_with_mouse(current_mouse_pos, last_mouse_pos)
        last_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "close"
            if event.type == pygame.KEYDOWN:
                move_bat_with_key(event.key)
        if gameover_flag:
            return "gameover"
        clock.tick(GAME_SPEED)
        pygame.display.flip()

def welcome_screen():
    global last_mouse_pos
    welcome_display = pygame.image.load('welcome.png')
    display_rect = welcome_display.get_rect()
    screen.blit(welcome_display,display_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "close"
        last_mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] == 1:
            if last_mouse_pos[0] > 242 and last_mouse_pos[0] < 459 and last_mouse_pos[1] > 296 and last_mouse_pos[1] < 386:
                return "play"
            elif last_mouse_pos[0] > 543 and last_mouse_pos[0] < 758 and last_mouse_pos[1] > 296 and last_mouse_pos[1] < 386:
                return "close"
        clock.tick(GAME_SPEED)
        pygame.display.flip()

def gameover_screen():
    global last_mouse_pos, curr_score
    go_display = pygame.image.load('gameover.png')
    display_rect = go_display.get_rect()
    screen.blit(go_display, display_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "close"
        last_mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] == 1:
            if last_mouse_pos[0] > 343 and last_mouse_pos[0] < 464 and last_mouse_pos[1] > 430 and last_mouse_pos[1] < 486:
                return "yes"
            elif last_mouse_pos[0] > 565 and last_mouse_pos[0] < 661 and last_mouse_pos[1] > 424 and last_mouse_pos[1] < 480:
                return "close"
        inplay_score("You Scored: ", 48, SCREEN_WIDTH // 2, BORDER_WIDTH*2, False)
        clock.tick(GAME_SPEED)
        pygame.display.flip()

def reset():
    global last_mouse_pos, bat_pos_x, bat_pos_y, ball_pos_x, ball_pos_y, ball_direction_x, ball_direction_y, gameover_flag, curr_score, GAME_SPEED
    last_mouse_pos = (0, (SCREEN_HEIGHT // 2))
    bat_pos_x = SCREEN_WIDTH - BAT_WIDTH
    bat_pos_y = (SCREEN_HEIGHT // 2) - (BAT_HEIGHT // 2)
    ball_pos_x = SCREEN_WIDTH // 2
    ball_pos_y = SCREEN_HEIGHT // 2
    ball_direction_x = "east"
    ball_direction_y = "north"
    gameover_flag = False
    curr_score = 0
    GAME_SPEED = 500

def inplay_score(message, font_size, X, Y, bul):
    global curr_score, blue
    font = pygame.font.Font('freesansbold.ttf', font_size)
    score_text = font.render(f'{message}{curr_score}', True, (0,0,0), blue)
    textRect = score_text.get_rect()
    if bul:
        textRect.topleft = (X, Y)
    else:
        textRect.center = (X, Y)
    screen.blit(score_text, textRect)
    clock.tick(GAME_SPEED)
    pygame.display.flip()

GAME_SPEED = 500
BALL_SPEED = 1
BAT_SPEED = 4
BAT_SPEED_WITH_KEY = 20

#colors
maroon = (146,43,33)
orange = (220,118,51)
blue = (214,234,248)
black = (23,32,42)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BORDER_WIDTH = 20
BAT_WIDTH = 20
BAT_HEIGHT = 120
BALL_RADIUS = 16
BORDER_COLOR = maroon
BAT_COLOR = orange
BALL_COLOR = black
BACK_GRD_COLOR = blue

last_mouse_pos = (0,(SCREEN_HEIGHT // 2))
clock = pygame.time.Clock()
gameover_flag = False
bat_pos_x = SCREEN_WIDTH - BAT_WIDTH
bat_pos_y = (SCREEN_HEIGHT // 2) - (BAT_HEIGHT // 2)
ball_pos_x = SCREEN_WIDTH // 2
ball_pos_y = SCREEN_HEIGHT // 2
ball_direction_x = "east"
ball_direction_y = "north"
close_flag = False
curr_score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PONG GAME *Developed by Saurabh*')

wel_return = welcome_screen()
if wel_return == "close":
    close_flag = True

while not close_flag:
    run_return = run_game()
    if run_return == "close":
        close_flag = True
        break
    elif run_return == "gameover":
        go_return = gameover_screen()
        if go_return == "close":
            close_flag = True
            break
        elif go_return == "yes":
            reset()
