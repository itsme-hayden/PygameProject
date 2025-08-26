import pygame


class Player:

    def __init__(self, xpos, ypos, jump_strength):
        self.image = pygame.image.load(r"revzoomieasset\rev_run1.png")
        self.xpos = xpos
        self.ypos = ypos
        self.jump_strength = jump_strength
        self.y_vel = 0
        self.on_ground = True
        self.hitbox = pygame.Rect(self.xpos, self.ypos, self.image.get_width(), self.image.get_height())
    
    def jump(self):
        self.y_vel = self.jump_strength 
        self.on_ground = False
    
    def get_img(self):
        return self.image

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
        self.hitbox = self.hitbox.move(0,change)

    def get_y_vel(self):
        return self.y_vel
    
    def update_y_vel(self, change):
        self.y_vel += change 

    def is_on_ground(self, groundHeight):
        if self.ypos + self.image.get_height() >= groundHeight:
            self.ypos = groundHeight
            return True
        return False