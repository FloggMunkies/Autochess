# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:17:08 2022

@author: mrkno
"""
import pygame as pg
import os
from debug import print_error


class Card(pg.sprite.Sprite):
    def __init__(self, name, card_type=0,):
        pg.sprite.Sprite.__init__(self)
        self.image = None
        self.card_type = card_type
        self.name = name

    def load_image(self, image_name=0):
        if image_name:
            try: # Try to load from IMAGE_PATH constant and image_name
                path = os.path.join(IMAGE_PATH, image_name)
            except NameError as ex: # if no IMAGE_PATH just use image_name
                print_error(ex)
                path = image_name
            try: # Load the image and get a rect
                self.image = pg.image.load(path).convert()
                self.rect = self.image.get_rect()
            except Exception as ex:
                print_error(ex)
        else:
            try:
                self.image = pg.image.load(os.path.join(IMAGE_PATH,
                                                        self.name.lower() +
                                                        "-icon.jpg")).convert()
                self.rect = self.image.get_rect()
            except Exception as ex:
                print_error(ex)

# %% Debugging


def debug():
    card = Card("card_name")
    card.load_image()


if __name__ == "__main__":
    debug()
