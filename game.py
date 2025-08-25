import pygame
import random #AI imported random but never used it, i could utilize to spawn obsticals
import sys
import main
import settings
import player
import obstacle




# Player setup
user = player.Player(main.player_img, 
                     settings.PLAYER_XPOS, 
                     settings.GROUND_HEIGHT - main.player_img.get_height(),
                     settings.JUMP_STRENGTH)



gravity = settings.GRAVITY


# Obstacles
obstacle_list = []
obstacle_timer = 0
spawn_rate = 1500  # milliseconds

# Font
font = settings.FONT
score = 0
start_time = pygame.time.get_ticks() #TODO CHECK THIS

def draw_player(x, y):
    main.screen.blit(main.player_img, (x, y))

def draw_obstacles(obstacles):
    for obs in obstacles:
        main.screen.blit(main.obstacle_img, (obs.x, obs.y))

def check_collision(player_rect, obstacles):
    for obs in obstacles:
        if player_rect.colliderect(obs):
            return True
    return False

def display_score(screen):
    score = (pygame.time.get_ticks() - start_time) // 100
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def game_over(screen):
    text = font.render("Game Over!", True, BLACK)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(2000)

def game_loop():
    running = True
    while running:
        dt = main.clock.tick(settings.FPS) # can this be moved out of loop, as a constant?
        main.screen.fill(settings.WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.key == pygame.K_SPACE and on_ground:
                user.jump()

        # Player physics
        user.update_y(user.get_y_vel())
        user.update_y_vel(gravity)

        if user.get_y() + player_img.get_height() >= ground_y: #this seems to keep rev on ground, i think class can do that
            player_y = ground_y - player_img.get_height()
            on_ground = True

        # Spawn obstacles
        obstacle_timer += dt 
        if obstacle_timer >= spawn_rate:
            obstacle_timer = 0
            new_obstacle = obstacle.Obstacle(main.obstacle_img, 
                                             settings.WIDTH, 
                                             settings.GROUND_HEIGHT)
            obstacle_list.append(new_obstacle)

        # Move obstacles
        for obs in obstacle_list:
            obs.update_x(-6)
        obstacle_list = [obs for obs in obstacle_list if obs.get_x() + obs.get_width() > 0]

        # Draw ground
        settings.draw_ground(main.screen)

        # Draw player and obstacles
        draw_player(user.get_x(), user.get_y())
        draw_obstacles(obstacle_list)

        # Check collision
        player_rect = pygame.Rect(user.get_x, user.get_y, user.get_width(), user.get_height())
        if check_collision(player_rect, obstacle_list):
            game_over(main.screen)
            running = False

        display_score(main.screen)
        

    pygame.display.flip()

pygame.quit()
