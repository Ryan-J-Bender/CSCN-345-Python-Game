import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

def getImageBoy(sheet, frame, width, height, color, scale):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image 

def getImageGirl(sheet, frame, width, height, color, scale):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)

    return image 