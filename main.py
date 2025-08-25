import pygame
import settings

pygame.init()

screen = settings.set_screen()
clock = pygame.time.Clock()
settings.load_images()
