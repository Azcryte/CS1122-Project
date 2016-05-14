# credit to pygame wiki for spritesheet class
# with some changes to function as needed for this project

import pygame
 
class spritesheet(object):
    def __init__(self, filename):
        # file not found exception
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Failed to load: ', filename
            raise SystemExit, message
        
    # loading an image from a rect
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    # multiple images and return as list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    
    # load a strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
