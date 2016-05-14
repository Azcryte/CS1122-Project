import pygame

BLACK = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        super(Sprite,self).__init__()
        self.display = pygame.display.getsurface()
        self.sprite = pygame.image.load(filename).convert()
        
        #self.image = pygame.transform.scale(sprite, (100,100))
        self.sprite.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.sprite.get_rect()
