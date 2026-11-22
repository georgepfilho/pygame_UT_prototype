import pygame
pygame.init()

import random
from src import globals
from src.player import *
from src.block import *
from src.arena import *
from src.pellet import Pellet
from src.bulletManager import BulletManager


clock = pygame.time.Clock()
arena = globals.arena
player = Player(800, 375)

blocks = []

bManager = BulletManager()
pellets = []

for i in range(3):
    blocks.append(Block(random.randint(600, 700) + 10, random.randint(100, 300) + 10))





while globals.running:

    globals.dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.running = False

    keys = pygame.key.get_pressed()

    globals.screen.fill("black")
    arena.draw()
    player.draw()
    bManager.draw()

    for block in blocks:
        block.draw()

    bManager.update(player)
    player.update(keys, blocks)

    
    
    pygame.display.flip()


pygame.quit()
