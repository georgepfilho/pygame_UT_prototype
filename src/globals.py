import pygame
screen = pygame.display.set_mode((1600, 900))
running = True
dt = 0.0

from src import arena
arena = arena.Arena(500, 75)