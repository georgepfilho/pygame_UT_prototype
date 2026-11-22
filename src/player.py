import pygame
from src import globals



class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 500
        self.dir = pygame.Vector2(0, 0)
        self.loadsprite = pygame.image.load(
            "img/heart.png"
        ).convert_alpha()
        self.sprite = pygame.transform.scale_by(self.loadsprite, 0.02)
        self.hp = 3
        self.hb = pygame.Rect(self.x, self.y, 32, 32)
        self.isInvulnerable = False
        self.invulnerableTimer = 0.0

    def draw(self):
        globals.screen.blit(self.sprite, pygame.Vector2(self.x, self.y))

    def update(self, keys, objList):

        self.inputcheck(keys)
        self.moveX(self.dir.x)
        self.collision("x", objList)
        self.moveY(self.dir.y)
        self.collision("y", objList)

        if self.isInvulnerable:
            self.invulnerableTimer += globals.dt
        if self.invulnerableTimer > 1.0:
            self.isInvulnerable = False
            self.invulnerableTimer = 0.0

        if self.hp < 1:
            print("se fodeu!")
            globals.running = False

        

    def moveX(self, xdir):
         self.x += xdir * self.speed * globals.dt
         self.hb.x = self.x

         self.hb.clamp_ip(globals.arena.rect)

         self.x = self.hb.x


    def moveY(self, ydir):
        self.y += ydir * self.speed * globals.dt
        self.hb.y = self.y

        self.hb.clamp_ip(globals.arena.rect)

        self.y = self.hb.y


    def inputcheck(self, keys):
        if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_d] and not keys[pygame.K_a]:
            self.dir.x = 0
            self.dir.y = 0
        if keys[pygame.K_w]:
            self.dir.y = -1

        if keys[pygame.K_s]:
            self.dir.y = 1

        if keys[pygame.K_d]:
            self.dir.x = 1

        if keys[pygame.K_a]:
            self.dir.x = -1

        if self.dir.length() > 0:
            self.dir = self.dir.normalize()

    def collision(self, axis, objList):

        for obj in objList:
            if self.hb.colliderect(obj.hb):

                if obj.type == "block":
                    if axis == "x":
                        if self.dir.x > 0:
                            self.x = obj.hb.left - 36
                            self.hb.x = self.x 
                        if self.dir.x < 0:
                            self.x = obj.hb.right
                            self.hb.x = self.x   
                    elif axis == "y":
                        if self.dir.y > 0:
                            self.y = obj.hb.top - 36
                            self.hb.y = self.y 
                        if self.dir.y < 0:
                            self.y = obj.hb.bottom
                            self.hb.y = self.y

    def take_dmg(self, damage):
        if not self.isInvulnerable:
            self.hp -= damage
            self.isInvulnerable = True
        else:
            pass
            


    
        

        
