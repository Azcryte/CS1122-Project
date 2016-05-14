import pygame
import random

class Mage(pygame.sprite.Sprite):
    def __init__(self):
        super(Mage, self).__init__()
        #self.display = pygame.display.getsurface()
        sprite = pygame.image.load("mage.png").convert()
        self.image = pygame.transform.scale(sprite, (58 * 3, 67 * 3))
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

        #self.playerNum = 0

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

