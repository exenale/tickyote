import pygame
import os
import time
import logging
from sprites_obj.tick import Tick
from sprites_obj.vegetation import Wildflowers, Grass
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_ASSETS_DIR
from sprites_obj.collection import GameSprites
import sys
from key_commands import press_down
from sprite_utils import get_grid_rect

_sound_library = {}

def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = os.path.join("sounds/", path +".wav")
    print(canonicalized_path)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()


def main():
    # create logger
    logger = logging.getLogger("sds")
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # add ch to logger
    logger.addHandler(ch)
    pygame.init()

    logo = pygame.image.load(os.path.join(IMAGE_ASSETS_DIR, "icon.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal tickyote")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    make_grid(screen)
    game_sprites = GameSprites()
  
    running = True
    pygame.key.set_repeat(10, 100)
    game_sprites.all.draw(screen)
    pygame.display.flip()
    refresh_rects = []
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                press_down(event, game_sprites)
                for sprite in game_sprites.all:
                    sprite.move(event.key)
                    if (sprite.dirty):
                        refresh_rects.append(sprite.source_rec)
                        refresh_rects.append(sprite.image.get_rect())
                make_grid(screen)
                game_sprites.garden.update()
                game_sprites.garden.draw(screen)
                game_sprites.all.update()
                game_sprites.all.draw(screen)
                pygame.display.update(refresh_rects)
                pygame.display.flip()
                
            if event.type == pygame.QUIT:
                running = False


def make_grid(screen):
    screen.fill((168,148,125))
    for row in range(15):
        for column in range(30):
            color = (180, 222, 138)
            pygame.draw.rect(screen,
                            color,
                            get_grid_rect(column, row))


if __name__=="__main__":
    main()
