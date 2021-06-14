import pygame
import os
import time
import logging
from sprites_obj.tick import Tick
from sprites_obj.vegetation import Wildflowers, Grass
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_ASSETS_DIR
import sys

_sound_library = {}


def snap_to_grid(rect):
    new_rect = rect.copy()
    new_rect.x = rect.x+15
    for row in range(15):
        for column in range(30):
            if new_rect.colliderect(get_grid_rect(column, row)):
                return get_grid_rect(column, row)


def get_grid_rect(column, row):
    rect = pygame.Rect((2 + 30) * column + 2,
                       (2 + 30) * row + 2,
                        30,
                        30)
    return rect


def check_garden_sprite_collision(new_sprite, garden_sprites):
    for sprite in garden_sprites:
        if sprite.rect.colliderect(new_sprite.rect):
            sprite.logger.info(f"{sprite.name} already here")
            return False
    return True


def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = os.path.join("sounds/", path +".wav")
    print(canonicalized_path)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

