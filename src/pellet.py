from src.bullet import Bullet
from src import globals
import pygame
class Pellet (Bullet):
    def __init__(self, x, y, dir):
        super().__init__(x, y, dir)
        self.hb = pygame.Rect(x, y, 32, 32)
        self.speed = 300                        
        self.dmg = 1
        self.loadsprite = pygame.image.load('img/square.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.loadsprite, 0.0625)

    #def update(self, player):
       # self.movement()
    def movement(self):
            self.x += self.dir.x * self.speed * globals.dt
            self.y += self.dir.y * self.speed * globals.dt
            self.hb.x = self.x
            self.hb.y = self.y        
