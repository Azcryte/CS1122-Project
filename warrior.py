import pygame
import random

class Warrior(pygame.sprite.Sprite):
    def __init__(self):
        super(Warrior, self).__init__()
        #self.display = pygame.display.getsurface()
        sprite1 = pygame.image.load("warrior.png").convert()
        sprite2 = pygame.image.load("warrior2.png").convert()
        sprite3 = pygame.image.load("warrior3.png").convert()
        sprite4 = pygame.image.load("warrior4.png").convert()
        self.spriteList = [sprite1, sprite2, sprite3, sprite4]
        self.image = pygame.transform.scale(sprite1, (65 * 3, 52 * 3))
        self.rect = pygame.Rect((0,0), (self.image.get_width(), self.image.get_height()))

        self.xPos = 0
        self.yPos = 200

        self.maxHealth = 200
        self.health = 200
        self.attack = 7
        self.special = 27
        self.cooldown = 4
        self.potionsUsed = 0
        self.lastSpecial = 0
        self.alive = True
        self.frame = 1

    def updateFrame(self):
        self.frame += 1
        if self.frame > 60:
            self.frame = 1
        elif self.frame <= 15:
            self.image = pygame.transform.scale(self.spriteList[0], (65 * 3, 52 * 3))
        elif self.frame <= 30:
            self.image = pygame.transform.scale(self.spriteList[1], (65 * 3, 52 * 3))
        elif self.frame <= 45:
            self.image = pygame.transform.scale(self.spriteList[2], (65 * 3, 52 * 3))
        elif self.frame <= 60:
            self.image = pygame.transform.scale(self.spriteList[3], (65 * 3, 52 * 3))
            
    def update(self):
        self.lastSpecial += 1
        print "warrior special in {0} turns".format(self.cooldown - self.lastSpecial)
        
    def subtractHealth(self, int):
        self.health -= int
        if self.health <= 0:
            self.alive = False
        print "warrior has {0} health".format(self.health)

    def usePotion(self):
        self.health += random.randint(100, 125)
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        self.potionsUsed += 1
        print "warrior has {0} health".format(self.health)

    
