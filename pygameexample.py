# Example file showing a circle moving on screen
import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
hit_ceil = False

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    pygame.draw.line(screen, "black", (0, screen.get_height() / 2), (screen.get_width(),screen.get_height() / 2))
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not hit_ceil:
        player_pos.y -= 300 * dt
    elif player_pos.y <= screen.get_height() / 2:
        player_pos.y += 300 * dt

    if player_pos.y <= screen.get_height() / 4:
        hit_ceil = True
    elif player_pos.y >= screen.get_height() / 2:
        hit_ceil = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()