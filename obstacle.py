import pygame

class Obstacle:
    def __init__(self, xpos, ypos):
        self.image = pygame.image.load(r"revzoomieasset\obstacle.png")
        self.xpos = xpos
        self.ypos = ypos - self.image.get_height()
        self.hitbox = pygame.Rect(self.xpos, self.ypos, self.image.get_width(), self.image.get_height())

    def get_width(self):
        return self.image.get_width()

    def update_x(self,change):
        self.xpos += change
        self.hitbox = self.hitbox.move(change,0)

    def get_img(self):
        return self.image
    
    def get_x(self):
        return self.xpos

    def get_y(self):
        return self.ypos
    
    def get_hitbox(self):
        return self.hitbox

