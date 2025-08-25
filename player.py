import pygame
import settings
import main
import game

class Player:

    def __init__(self, image: pygame.image, xpos, ypos, jump_strength):
        self.image = image
        self.xpos = xpos
        self.ypos = ypos
        self.jump_strength = jump_strength
        self.y_vel = 0
        self.on_ground = True
    
    def jump(self):
        self.y_vel = self.jump_strength 
        self.on_ground = False
    
    def get_x(self):
        return self.xpos

    def get_y(self):
        return self.ypos
    
    def get_width(self):
        return self.image.get_width()
    
    def get_height(self):
        return self.image.get_height()

    def update_y(self, change):
        self.ypos += change

    def get_y_vel(self):
        return self.y_vel
    
    def update_y_vel(self, change):
        self.y_vel += change 