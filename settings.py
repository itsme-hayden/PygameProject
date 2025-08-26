import pygame

GAME_NAME = "REV'S ZOOMIES"
GAME_ICON = pygame.image.load(r"revzoomieasset\Reveille_logo.png")
PLAYER_ICON = pygame.image.load(r"revzoomieasset\rev_run1.png")
WIDTH, HEIGHT = 800, 400
GROUND_HEIGHT = HEIGHT - 50
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY = 0.8
JUMP_STRENGTH = -15
PLAYER_XPOS = 100
SCREEN = None




def set_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_icon(GAME_ICON)
    
    return screen

def load_images():
    player_img = pygame.image.load(r"revzoomieasset\rev_run1.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (60, 50))  # resize if needed

    obstacle_img = pygame.image.load(r"revzoomieasset\obstacle.png").convert_alpha()
    obstacle_img = pygame.transform.scale(obstacle_img, (40, 60))

    return (player_img, obstacle_img)

def load_font():
    pygame.font.init()
    return pygame.font.SysFont(None, 36)

def draw_ground(screen:pygame.display):
    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)