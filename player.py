import pygame
import block


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 500
        self.dir = pygame.Vector2(0, 0)
        self.loadsprite = pygame.image.load(
            "gimg/heart.png"
        ).convert_alpha()
        self.sprite = pygame.transform.scale_by(self.loadsprite, 0.02)
        self.hp = 20
        self.hb = pygame.Rect(self.x, self.y, 36, 36)

    def draw(self, screen):
        screen.blit(self.sprite, pygame.Vector2(self.x, self.y))

    def update(self, keys, deltatime, objList, arena):

        self.inputcheck(keys)
        self.moveX(self.dir.x, deltatime, arena)
        self.collision("x", objList)
        self.moveY(self.dir.y, deltatime, arena)
        self.collision("y", objList)

        

    def moveX(self, xdir, deltatime, arena):
         self.x += xdir * self.speed * deltatime
         self.hb.x = self.x

         self.hb.clamp_ip(arena.rect)

         self.x = self.hb.x


    def moveY(self, ydir, deltatime, arena):
        self.y += ydir * self.speed * deltatime
        self.hb.y = self.y

        self.hb.clamp_ip(arena.rect)

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

        
