import logging
import pygame
import os

img_assets_dir = "image_assets/"
class Tick(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen_height = 300
        self.screen_width = 500
        self.image = pygame.image.load(os.path.join(img_assets_dir, "tick.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (500 / 2, 300 / 2)
        self.logger = logging.getLogger("sds")
    
    def moveRight(self, step_length):
        if self.rect.x >self.screen_width-32:
            step_length = 0
        self.rect.x  += step_length

    def moveLeft(self, step_length):
        if self.rect.x <0:
            step_length = 0
        self.rect.x  += -step_length

    def moveUp(self, step_length):
        if self.rect.y <0:
            step_length = 0
        self.rect.y  += -step_length

    def moveDown(self, step_length):
        if self.rect.y >self.screen_height-32:
            step_length = 0
        self.rect.y  += step_length

    def move(self, direction):
        self.logger.info(f"direction {direction}")
        self.source_rec = self.image.get_rect()
        step_length = 10
        switcher = {
            275: self.moveRight,
            276: self.moveLeft,
            274: self.moveDown,
            273: self.moveUp
        }
        func = switcher.get(direction)
        self.dirty = 1
        if func:
            func(step_length)
