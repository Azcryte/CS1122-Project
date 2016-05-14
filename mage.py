import pygame
import random

class Mage(pygame.sprite.Sprite):
    def __init__(self):
        super(Mage, self).__init__()
        #self.display = pygame.display.getsurface()
        self.sprite1 = pygame.image.load("mage.png").convert()
        self.sprite2 = pygame.image.load("mage2.png").convert()
        self.sprite3 = pygame.image.load("mage3.png").convert()
        self.sprite4 = pygame.image.load("mage4.png").convert()
        self.spriteList = [self.sprite1, self.sprite2, self.sprite3, self.sprite4]
        self.image = pygame.transform.scale(self.sprite1, (58 * 3, 67 * 3))
        self.rect = pygame.Rect((0,0), (self.image.get_width(), self.image.get_height()))

        self.xPos = 0
        self.yPos = 200

        self.maxHealth = 200
        self.health = 200
        self.attack = 4
        self.special = 20
        self.cooldown = 2
        self.potionsUsed = 0
        self.lastSpecial = 0
        self.alive = True
        self.frame = 1

        #self.playerNum = 0

    def flip(self):
        pygame.transform.flip(self.image, True, False)

    def updateFrame(self):
        self.frame += 1
        if self.frame > 60:
            self.frame = 1
        elif self.frame <= 15:
            self.image = pygame.transform.scale(self.spriteList[0], (58 * 3, 67 * 3))
        elif self.frame <= 30:
            self.image = pygame.transform.scale(self.spriteList[1], (58 * 3, 67 * 3))
        elif self.frame <= 45:
            self.image = pygame.transform.scale(self.spriteList[2], (58 * 3, 67 * 3))
        elif self.frame <= 60:
            self.image = pygame.transform.scale(self.spriteList[3], (58 * 3, 67 * 3))

    def update(self):
        self.lastSpecial += 1
        print "mage special in {0} turns".format(self.cooldown - self.lastSpecial)
        
    def subtractHealth(self, int):
        self.health -= int
        if self.health <= 0:
            self.alive = False
        print "mage has {0} health".format(self.health)

    def usePotion(self):
        self.health += random.randint(120, 150)
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        self.potionsUsed += 1
        print "mage has {0} health".format(self.health)

