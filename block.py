import pygame
class Block:

    def __init__(self, x, y):
        self.type = "block"
        self.x = x
        self.y = y
        self.hb = pygame.Rect(self.x, self.y, 36, 36)
        self.loadSprite = pygame.image.load('img/square.png').convert_alpha()
        self.sprite = pygame.transform.scale_by(self.loadSprite, 0.0625)

    def draw(self, screen):
        
        screen.blit(self.sprite, pygame.Vector2(self.x, self.y))

