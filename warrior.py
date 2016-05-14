import pygame
import random

class Warrior(pygame.sprite.Sprite):
    def __init__(self):
        super(Warrior, self).__init__()
        #self.display = pygame.display.getsurface()
        sprite = pygame.image.load("warrior.png").convert()
        self.image = pygame.transform.scale(sprite, (65 * 3, 52 * 3))
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

    
