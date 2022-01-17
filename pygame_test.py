# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:23:21 2022

@author: mrkno

pg basic form
"""

#%% Imports
import pygame as pg
import colors
import os

#%% Initialize
pg.init()

# Filepaths
game_path = os.path.dirname(__file__)
image_path = os.path.join(game_path, "images")

# Clock
clock = pg.time.Clock()


# Set up the drawing window
WIDTH, HEIGHT = 640, 480
screen = pg.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True

class Player(pg.sprite.Sprite):
    def __init__(self, image_name):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(image_path, image_name)).convert()
        self.image.set_colorkey(colors.KEYPINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
    def update(self):
        self.rect.x += 1

# Sprites
all_sprites = pg.sprite.Group()
player = Player("billblaster.png")
all_sprites.add(player)

#%% Main Loop
while running:

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Clock
    clock.tick(60)
    
    # Update
    all_sprites.update()
    
    # Draw / render
    screen.fill(colors.BLACK)
    all_sprites.draw(screen)

    # Flip the display
    pg.display.flip()

pg.quit()