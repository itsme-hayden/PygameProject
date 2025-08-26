import pygame
import random #AI imported random but never used it, i could utilize to spawn obsticals
import sys
import settings
import player
import obstacle


#screen set up
screen = settings.set_screen()
clock = pygame.time.Clock()

# Player setup
user = player.Player(settings.PLAYER_XPOS, 
                     settings.GROUND_HEIGHT 
                     - settings.PLAYER_ICON.get_height(),
                     settings.JUMP_STRENGTH)



gravity = settings.GRAVITY


# Obstacles
 # milliseconds

# Font
font = settings.load_font()
score = 0
start_time = pygame.time.get_ticks() #TODO CHECK THIS

def draw_player(player, x, y):
    screen.blit(player.get_img(), (x, y))

def draw_obstacles(obstacles):
    for obs in obstacles:
        screen.blit(obs.get_img(), (obs.get_x(), obs.get_y()))

def check_collision(player_rect, obstacles):
    for obs in obstacles:
        if player_rect.colliderect(obs.get_hitbox()):
            return True
    return False

def display_score(screen):
    score = (pygame.time.get_ticks() - start_time) // 100
    score_text = font.render(f"Score: {score}", True, settings.BLACK)
    screen.blit(score_text, (10, 10))

def game_over(screen):
    text = font.render("Game Over!", True, settings.BLACK)
    screen.blit(text, (screen.WIDTH//2 - 80, screen.HEIGHT//2))
    pygame.time.wait(2000)

def game_loop():
    running = True
    obstacle_list = []
    obstacle_timer = 0
    obstacle_speed = -1
    spawn_rate = 1500 
    while running:
        dt = clock.tick(settings.FPS)
        screen.fill(settings.WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.K_SPACE and on_ground:
                user.jump()

        # Player physics
        user.update_y(user.get_y_vel())
        user.update_y_vel(gravity)

        
        on_ground = user.is_on_ground(settings.GROUND_HEIGHT)

        # Spawn obstacles
        obstacle_timer += dt 
        if obstacle_timer >= spawn_rate:
            obstacle_timer = 0
            new_obstacle = obstacle.Obstacle(settings.WIDTH, 
                                             settings.GROUND_HEIGHT)
            obstacle_list.append(new_obstacle)

        # Move obstacles
        for obs in obstacle_list:
            obs.update_x(obstacle_speed)
        obstacle_list = [obs for obs in obstacle_list if obs.get_x() + obs.get_width() > 0]
        
        if dt // 1000 % 3 == 0: #every 3 seconds
            obstacle_speed -= 1


        # Draw ground
        settings.draw_ground(screen)

        # Draw player and obstacles
        draw_player(user, user.get_x(), user.get_y())
        draw_obstacles(obstacle_list)

        # Check collision
        if check_collision(user.hitbox, obstacle_list):
            game_over(screen)
            running = False

        display_score(screen)

        pygame.display.flip()
        

    pygame.display.flip()
    


