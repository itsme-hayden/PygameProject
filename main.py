import pygame
import settings
import game

pygame.init()

screen = settings.set_screen()
clock = pygame.time.Clock()
player_img, obstacle_img = settings.load_images()


