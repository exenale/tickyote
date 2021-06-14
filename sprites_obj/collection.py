import logging
import pygame
import os
from sprites_obj.tick import Tick
from constants import IMAGE_ASSETS_DIR, SCREEN_WIDTH, SCREEN_HEIGHT


class GameSprites():
    def __init__(self):
        self.tick = Tick(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.garden = pygame.sprite.Group()
        self.all = pygame.sprite.Group()
        self.all.add(self.tick)