from src.pellet import Pellet
from src.bullet import Bullet
import random
import pygame
from src import globals
class BulletManager():
    def __init__ (self):
        self.spawn_timer = 0.0 
        self.spawn_cooldown = 2.0
        self.patterns = {
            1:self.horizontal,
            2:self.vertical,
            3:self.intersect,
            4:self.spiral
        }
        self.bulletTypes = {
            1:Pellet
        }
        self.bulletList = []

        self.difficulty_tier = 1



    def timerManager(self):
        self.spawn_timer += globals.dt
        if self.spawn_timer >= self.spawn_cooldown:
            attackNum = random.randint(1,2)
            self.patterns[attackNum]()
            self.spawn_timer = 0.0



    def update(self, player):

        self.timerManager()

        for bullet in self.bulletList[:]:
            bullet.update(player)

            if not globals.arena.rect.inflate(5, 5).colliderect(bullet.hb):
                self.bulletList.remove(bullet)



    def draw(self):

        for bullet in self.bulletList:
            bullet.draw()



    def horizontal(self):
        offset = random.randint(0, 30)
        settings = random.choice([[globals.arena.rect.right, -1], [globals.arena.rect.left, 1]])
        for y in range(globals.arena.rect.top + offset, globals.arena.rect.bottom - 20, 81):
            new_bullet = self.bulletTypes[1](settings[0], y, pygame.Vector2(settings[1], 0))
            self.bulletList.append(new_bullet)



    def vertical(self):
        offset = random.randint(0, 30)
        settings = random.choice([[globals.arena.rect.bottom, -1], [globals.arena.rect.top, 1]])
        for x in range(globals.arena.rect.left + offset, globals.arena.rect.right - 20, 81):
            new_bullet = self.bulletTypes[1](x, settings[0], pygame.Vector2(0, settings[1]))
            self.bulletList.append(new_bullet)



    def intersect(): 
        pass
    def spiral():
        pass
        
        