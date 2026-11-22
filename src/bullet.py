import pygame
from src import globals
class Bullet:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.speed = 100
        self.dir = direction
        self.hb = pygame.Rect(x, y, 0, 0)
        self.dmg = None
        self.sprite = None

    def update(self, player):
        self.movement()
        self.draw()
        self.collide(player)

    def movement(self):
            self.x += self.dir.x * self.speed * globals.dt
            self.y += self.dir.y * self.speed * globals.dt
            self.hb.x = self.x
            self.hb.y = self.y      
    def draw(self):
        globals.screen.blit(self.sprite, pygame.Vector2(self.x, self.y))

    def collide(self, player):
         if self.hb.colliderect(player.hb):
              player.take_dmg(self.dmg)
              print("hp =", player.hp)
        
        

#to-do