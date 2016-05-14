import pygame
import random

class Rogue(pygame.sprite.Sprite):
    def __init__(self):
        super(Rogue, self).__init__()
        #self.display = pygame.display.getsurface()
        sprite = pygame.image.load("rogue.png").convert()
        self.image = pygame.transform.scale(sprite, (49 * 3, 50 * 3))
        self.rect = pygame.Rect((0,0), (self.image.get_width(), self.image.get_height()))

        self.xPos = 0
        self.yPos = 200

        self.maxHealth = 200
        self.health = 200
        self.attack = 6
        self.special = 25
        self.cooldown = 5
        self.potionsUsed = 0
        self.lastSpecial = 0
        self.alive = True

    def update(self):
        self.lastSpecial += 1
        print "rogue special in {0} turns".format(self.cooldown - self.lastSpecial)
        
    def subtractHealth(self, int):
        self.health -= int
        if self.health <= 0:
            self.alive = False
        print "rogue has {0} health".format(self.health)

    def usePotion(self):
        self.health += random.randint(100, 125)
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        self.potionsUsed += 1
        print "rogue has {0} health".format(self.health)

