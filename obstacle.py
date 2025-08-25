import pygame

class Obstacle:
    def __init__(self, image: pygame.image, xpos, ypos):
        self.image = image
        self.xpos = xpos
        self.ypos = ypos - self.image.get_height()
        self.hitbox = pygame.Rect(self.xpos, self.ypos, self.image.get_width(), self.image.get_height())

    def get_width(self):
        return self.image.get_width

    def update_x(self,change):
        self.xpos += change
        self.hitbox = self.hitbox.move(change,0)

