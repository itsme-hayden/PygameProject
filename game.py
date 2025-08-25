import pygame
import random #AI imported random but never used it
import sys




# Ground
ground_y = HEIGHT - 50

# Load images


# Player setup
player_x = 100
player_y = ground_y - player_img.get_height()
player_vel_y = 0
gravity = 0.8
jump_strength = -15
on_ground = True

# Obstacles
obstacle_list = []
obstacle_timer = 0
spawn_rate = 1500  # milliseconds

# Font
font = pygame.font.SysFont(None, 36) 
score = 0
start_time = pygame.time.get_ticks()

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_obstacles(obstacles):
    for obs in obstacles:
        screen.blit(obstacle_img, (obs.x, obs.y))

def check_collision(player_rect, obstacles):
    for obs in obstacles:
        if player_rect.colliderect(obs):
            return True
    return False

# Game loop
running = True
while running:
    dt = clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_vel_y = jump_strength
                on_ground = False

    # Player physics
    player_y += player_vel_y
    player_vel_y += gravity

    if player_y + player_img.get_height() >= ground_y:
        player_y = ground_y - player_img.get_height()
        on_ground = True

    # Spawn obstacles
    obstacle_timer += dt 
    if obstacle_timer >= spawn_rate:
        obstacle_timer = 0
        obstacle_x = WIDTH
        obstacle_y = ground_y - obstacle_img.get_height()
        obstacle_list.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_img.get_width(), obstacle_img.get_height()))

    # Move obstacles
    for obs in obstacle_list:
        obs.x -= 6
    obstacle_list = [obs for obs in obstacle_list if obs.x + obs.width > 0]

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, ground_y), (WIDTH, ground_y), 2)

    # Draw player and obstacles
    draw_player(player_x, player_y)
    draw_obstacles(obstacle_list)

    # Check collision
    player_rect = pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())
    if check_collision(player_rect, obstacle_list):
        text = font.render("Game Over!", True, BLACK)
        screen.blit(text, (WIDTH//2 - 80, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Score
    score = (pygame.time.get_ticks() - start_time) // 100
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
