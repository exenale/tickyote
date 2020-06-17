import pygame
import os
import time
import logging
img_assets_dir = "image_assets/"
screen_width = 500
screen_height = 300
step_x = 10
step_y = 10

def main():
    pygame.init()

    logo = pygame.image.load(os.path.join(img_assets_dir, "icon.png"))
    image = pygame.image.load(os.path.join(img_assets_dir, "tick.png"))
    grass = pygame.image.load(os.path.join(img_assets_dir, "grass.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal tickyote")
    screen = pygame.display.set_mode((screen_width,screen_height))
    xpos = 50
    ypos = 50
    screen.fill((200,100,100))
    running = True
    g_ypos = -1
    g_xpos = -1
    pygame.key.set_repeat(10, 100)
    rect = screen.blit(image, (xpos,ypos))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                screen.fill((200,100,100))
                xpos, ypos = tick_pos(xpos, ypos, event.key)
                old_rect = rect
                rect = screen.blit(grass, (g_xpos, g_ypos))
                rect = screen.blit(image, (xpos,ypos))
                pygame.display.update([rect, old_rect])
                pygame.time.set_timer ( pygame.USEREVENT , 0 )
                if event.key == 103:
                    if g_xpos == -1:
                        g_xpos = xpos
                        g_ypos = ypos
                    print("grass")
                    rect = screen.blit(grass, (g_xpos, g_ypos))
                    rect = screen.blit(image, (xpos,ypos))
                    pygame.display.update([rect, old_rect])
            if event.type == pygame.QUIT:
                running = False

def tick_pos(xpos: int,ypos: int, direction: int):
    step_length = 10
    if xpos>screen_width-32 and direction == 275:
        step_length = 0
    if xpos<0 and direction == 276:
        step_length = 0
    if ypos>screen_height-32 and direction == 274: 
        step_length = 0
    if ypos<0 and direction == 273:
        step_length = 0
    if (direction==274):
        ypos += step_length
    if (direction==273):
        ypos += -step_length
    if (direction==275):
        xpos += step_length
    if (direction==276):
        xpos += -step_length
    return xpos, ypos


if __name__=="__main__":
    main()
