import pygame
import os
import time
import logging
from sprites_obj.tick import Tick
from sprites_obj.grass import Grass
import sys
img_assets_dir = "image_assets/"
screen_width = 500
screen_height = 300
step_x = 10
step_y = 10

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
    screen.fill((200,100,100))
    all_sprites = pygame.sprite.Group()
    tick_sprite = Tick()
    all_sprites.add(tick_sprite)
    running = True
    pygame.key.set_repeat(10, 100)
    all_sprites.draw(screen)
    pygame.display.flip()
    refresh_rects = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 103:
                    logger.info("Grow some grass")
                    grass = Grass(tick_sprite.rect.x, tick_sprite.rect.y)
                    all_sprites.add(grass)
                for sprite in all_sprites:
                    sprite.move(event.key)
                    if (sprite.dirty):
                        refresh_rects.append(sprite.source_rec)
                        refresh_rects.append(sprite.image.get_rect())
                screen.fill((200,100,100))
                all_sprites.update()
                all_sprites.draw(screen)
                pygame.display.update(refresh_rects)
                pygame.display.flip()
                
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    main()
