import logging
import pygame
import os

img_assets_dir = "image_assets/"
class Vegetation(pygame.sprite.DirtySprite):
    def __init__(self, xpos, ypos, vegetation_type):
        super().__init__()
        self.image = pygame.image.load(os.path.join(img_assets_dir, f"{vegetation_type}.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (xpos, ypos)
        self.logger = logging.getLogger("sds")
        self.dirty = 1
        self.source_rec = self.image.get_rect()
        self.name = vegetation_type
    

    def move(self, direction):
        self.dirty = 0
        self.source_rec = self.image.get_rect()
        return



class Wildflowers(Vegetation):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, "wildflowers")