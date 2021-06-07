import pygame
import os
import time
import logging
from sprites_obj.tick import Tick
from sprites_obj.grass import Grass
from sprites_obj.vegetation import Wildflowers
import sys
img_assets_dir = "image_assets/"
screen_width = 642
screen_height = 322
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

    logo = pygame.image.load(os.path.join(img_assets_dir, "icon.png"))
    grass = pygame.image.load(os.path.join(img_assets_dir, "grass.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal tickyote")

    screen = pygame.display.set_mode((screen_width,screen_height))
    make_grid(screen)
    all_sprites = pygame.sprite.Group()
    garden_sprites = pygame.sprite.Group()
    tick_sprite = Tick(screen_width, screen_height)
    all_sprites.add(tick_sprite)
    running = True
    pygame.key.set_repeat(10, 100)
    all_sprites.draw(screen)
    pygame.display.flip()
    refresh_rects = []
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 103: # G
                    grass_rect = snap_to_grid(tick_sprite.rect)
                    grass = Grass(grass_rect.x+15, grass_rect.y+15)
                    if check_garden_sprite_collision(grass, garden_sprites):
                        logger.info("Grow some grass")
                        garden_sprites.add(grass)
                        play_sound("thud")
                if event.key == 105: ## i
                    grass_rect = snap_to_grid(tick_sprite.rect)
                    vegetation = Wildflowers(grass_rect.x+15, grass_rect.y+15)
                    if check_garden_sprite_collision(vegetation, garden_sprites):
                        logger.info(f"Grow some {vegetation.name}")
                        garden_sprites.add(vegetation)
                        play_sound("thud")
                if event.key==104: # h
                    dirt_rect = snap_to_grid(tick_sprite.rect)
                    for sprite in garden_sprites:
                        if sprite.rect.colliderect(dirt_rect):
                            logger.info("removing plant life")
                            garden_sprites.remove(sprite)
                            play_sound("pop")
                for sprite in all_sprites:
                    sprite.move(event.key)
                    if (sprite.dirty):
                        refresh_rects.append(sprite.source_rec)
                        refresh_rects.append(sprite.image.get_rect())
                make_grid(screen)
                garden_sprites.update()
                garden_sprites.draw(screen)
                all_sprites.update()
                all_sprites.draw(screen)
                pygame.display.update(refresh_rects)
                pygame.display.flip()
                
            if event.type == pygame.QUIT:
                running = False


def check_garden_sprite_collision(new_sprite, garden_sprites):
    for sprite in garden_sprites:
        if sprite.rect.colliderect(new_sprite.rect):
            sprite.logger.info(f"{sprite.name} already here")
            return False
    return True


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
