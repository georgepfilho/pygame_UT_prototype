import pygame
import random
from src.player import *
from src.block import *
from src.arena import *

pygame.init()

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
running = True
arena = Arena(150, 75)
player = Player(450, 350)

blocks = []

pellets = []


while running:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    screen.fill("black")
    arena.draw(screen)

    player.draw(screen)
    
    player.update(keys, delta_time, blocks,arena)

    
    
    pygame.display.flip()


pygame.quit()
