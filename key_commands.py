import pygame
import os
import time
import logging
from sprites_obj.tick import Tick
from sprites_obj.vegetation import Wildflowers, Grass
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, IMAGE_ASSETS_DIR
import sys
from sprite_utils import check_garden_sprite_collision, snap_to_grid, play_sound


def press_down(event, game_sprites):
    if event.key == 113: # Q
        grass_rect = snap_to_grid(game_sprites.tick.rect)
        vegetation = Grass(grass_rect.x+15, grass_rect.y+15)
        plop_vegetation(game_sprites, vegetation)
    if event.key == 119: ## w
        grass_rect = snap_to_grid(game_sprites.tick.rect)
        vegetation = Wildflowers(grass_rect.x+15, grass_rect.y+15)
        plop_vegetation(game_sprites, vegetation)
    if event.key==104: # h
        dirt_rect = snap_to_grid(game_sprites.tick.rect)
        for sprite in game_sprites.garden:
            if sprite.rect.colliderect(dirt_rect):
                game_sprites.tick.logger.info("removing plant life")
                game_sprites.garden.remove(sprite)
                play_sound("pop")


def plop_vegetation(game_sprites, vegetation):
    if check_garden_sprite_collision(vegetation, game_sprites.garden):
        game_sprites.tick.logger.info(f"Grow some {vegetation.name}")
        game_sprites.garden.add(vegetation)
        play_sound("thud")

def deplop_vegetation(game_sprites):
    dirt_rect = snap_to_grid(game_sprites.tick.rect)
    for sprite in game_sprites.garden:
        if sprite.rect.colliderect(dirt_rect):
            game_sprites.tick.logger.info("removing plant life")
            game_sprites.garden.remove(sprite)
            play_sound("pop")