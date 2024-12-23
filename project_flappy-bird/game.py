import pygame, sys, random

# tạo hàm


def draw_floor():
    screen.blit(floor, (floor_x_pos, 590))
    screen.blit(floor, (floor_x_pos + 432, 590))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(450, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(450, random_pipe_pos - 650))
    return bottom_pipe, top_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 590:
            screen.blit(pipe_surface, pipe)
        else:
            plip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(plip_pipe, pipe)
    return pipes


def check_colission(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 590:
        return False
    return True


def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement * 3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_state):
    if game_state == "main game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 100))
        screen.blit(score_surface, score_rect)
    if game_state == "game over":
        score_surface = game_font.render(f"Score: {int(score)}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 70))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(
            f"High Score: {int(high_score)}", True, (255, 255, 255)
        )
        high_score_rect = high_score_surface.get_rect(center=(216, 560))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pygame.init()
screen = pygame.display.set_mode((432, 700))
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.TTF", 40)
# tạo các biến
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
# chèn backgound
bg = pygame.transform.scale2x(
    pygame.image.load("assets/background-night.png").convert()
)
# chèn sàn
floor = pygame.transform.scale2x(pygame.image.load("assets/floor.png").convert())
# chèn bird
bird_down = pygame.transform.scale2x(
    pygame.image.load("assets/yellowbird-downflap.png").convert_alpha()
)
bird_mid = pygame.transform.scale2x(
    pygame.image.load("assets/yellowbird-midflap.png").convert_alpha()
)
bird_up = pygame.transform.scale2x(
    pygame.image.load("assets/yellowbird-upflap.png").convert_alpha()
)
bird_list = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_list[bird_index]

bird_rect = bird.get_rect(center=(100, 350))

# Tạo timer cho bird
bird_flap = pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap, 200)
# Tạo ống
pipe_surface = pygame.transform.scale2x(
    pygame.image.load("assets/pipe-green.png").convert()
)
pipe_list = []

# tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200, 300, 400]
floor_x_pos = 0
# tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(
    pygame.image.load("assets/message.png ").convert_alpha()
)
game_over_rect = game_over_surface.get_rect(center=(216, 320))

# chèn âm thanh
flap_sound = pygame.mixer.Sound("sound/sfx_wing.wav")
hit_sound = pygame.mixer.Sound("sound/sfx_hit.wav")
score_sound = pygame.mixer.Sound("sound/sfx_point.wav")
score_sound_countdown = 100
# while loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -10
                flap_sound.play()
            if event.key == pygame.K_SPACE and not game_active:

                pipe_list.clear()
                bird_rect.center = (100, 350)
                bird_movement = 0
                score = 0
                game_active = True
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == bird_flap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
    screen.blit(bg, (0, 0))
    if game_active:
        # chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_colission(pipe_list)
        # ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display("main game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display("game over")
    # sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(80)
