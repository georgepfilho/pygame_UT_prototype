import pygame
from src.globals import screen
class Arena:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x+20, y+20, 600, 600)
        self.loadsprite = pygame.image.load('img/battle_box.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.loadsprite, 5)

    def draw (self):
        screen.blit(self.sprite, pygame.Vector2(self.x, self.y))
