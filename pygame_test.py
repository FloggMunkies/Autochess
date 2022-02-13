# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:23:21 2022

@author: mrkno

pg basic form
"""

# %% Imports
import pygame as pg
import colors
import os
import random
from debug import print_error

# %% Initialize
pg.init()

# Clock
clock = pg.time.Clock()

# Settings and Defaults
TILESIZE = 96

# fonts
small_font = pg.font.Font(None, 32)
large_font = pg.font.Font(None, 64)

#  Filepaths
GAME_PATH = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(GAME_PATH, "images")

# card type lists
card_names = ["Villager", "Toxotes", "Prodromos", "Petrobolos", "Peltast",
              "Pegasus", "NemeanLion", "Myrmidon", "Minotaur", "Medusa",
              "Manticore", "Hypaspist", "Hydra", "Hoplite", "Hippocampus",
              "Hippikon", "Hetairoi", "Helepolis", "Gastraphetes", "Cyclops",
              "Colossus", "Chimera", "Centaur", "Caravan"]

deck = []

# Set up the drawing window
WIDTH, HEIGHT = 640, 480
screen = pg.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
running = True

# %% Functions


def load_image(image_name, filetype=".jpg", image_path=IMAGE_PATH):
    try:
        image = pg.image.load(os.path.join(image_path,
                                           image_name+filetype)).convert()
        return image
    except FileNotFoundError:
        try:
            image = pg.image.load(os.path.join(image_path,
                                               image_name +
                                               "-icon" +
                                               filetype)).convert()
            return image
        except Exception as ex:
            print_error(ex)

# %% Classes


class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board()
        self.surf = self.create_board_surf()
        self.sprites = pg.sprite.Group()
        self.cards = {}

    def create_board_surf(self):
        # Create surface for board
        board_surf = pg.Surface((TILESIZE*self.rows, TILESIZE*self.cols))

        # Iterate over grid drawing rects
        for y in range(self.cols):
            for x in range(self.rows):
                rect = pg.Rect(x*TILESIZE+1, y*TILESIZE+1,
                               TILESIZE-2, TILESIZE-2)
                pg.draw.rect(board_surf, pg.Color('darkgrey'), rect)
        return board_surf

    def get_square_under_mouse(self, board=None):
        if board is None:
            board = self.board
        # Get mouse position, in terms of gridsize, and x/y
        mouse_pos = pg.Vector2(pg.mouse.get_pos())
        x, y = [int(v // TILESIZE) for v in mouse_pos]
        try:
            if x >= 0 and y >= 0:
                return (board[y][x], x, y)
        except IndexError:
            pass
        return None, None, None

    def create_board(self):
        board = []
        # create list of list for board
        for y in range(self.cols):
            board.append([])
            for x in range(self.rows):
                board[y].append(None)
        # populate the board
        # for x in range(0, 8):
        #     board[1][x] = ('black', 'pawn')
        # for x in range(0, 8):
        #     board[6][x] = ('white', 'pawn')
        return board

    def populate_board(self, board=None):
        if board is None:
            board = self.board
        for y in range(self.cols):
            for x in range(self.rows):
                board[y][x] = random.choice(card_names)
        print(board)
        return board

    def draw_board(self, board=None, update=False):
        if board is None:
            board = self.board
        # for card in board
        # TODO make more abstract/general
        for y in range(len(board)):
            for x in range(len(board[y])):
                if not update:
                    unit = Unit(name=board[y][x])
                    self.sprites.add(unit)
                    self.cards[board[y][x]] = unit
                else:
                    print(x, y, board[y][x])
                    try:
                        unit = self.cards[board[y][x]]
                    except KeyError:
                        continue
                unit.rect.center = (TILESIZE*(x+1/2),
                                    TILESIZE*(y+1/2))
        print("cards:", self.cards)
        # cards = {name: Unit(name=name) for name in board[0]}
        # for i, key in enumerate(cards.keys()):
        #     unit = cards[key]
        #     self.sprites.add(unit)
        #     unit.rect.center = (TILESIZE*(i+1/2),
        #                         TILESIZE/2)


class CardHolder():
    def __init__(self):
        pass


class Player(pg.sprite.Sprite):
    def __init__(self, image_name):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(image_name)
        self.image.set_colorkey(colors.KEYPINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - self.rect.width/2,
                            HEIGHT-self.rect.height/2)

    def update(self):
        pass


class Card(pg.sprite.Sprite):
    def __init__(self, name="default"):
        pg.sprite.Sprite.__init__(self)
        self.image = load_image(name)
        self.image.set_colorkey(colors.KEYPINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - self.rect.width/2,
                            HEIGHT-self.rect.height/2)

    def update(self):
        pass


class Unit(Card):
    def __init__(self, name="Default Unit", stats=[1, 1], text="Default Text"):
        super().__init__(name)
        self.stats = stats
        self.text = text

    def update(self):
        super().update()


class Villager(Unit):
    def __init__(self, name="Villager", stats=[1, 1], text="Prostagma",
                 position=0):
        super().__init__(name, stats, text)

        self.position = position

    def update(self):
        super().update()

# %% Instance Init / Sprites


all_sprites = pg.sprite.Group()
# player = Player("index-zeus")
# testcard = Villager()
# # testcard.load_image()
# all_sprites.add(player)
# all_sprites.add(testcard)
shop = Board(4, 2)
shop.populate_board()
shop.draw_board()

# %% Main Loop
while running:

    # Track Mouse
    mouse = pg.mouse.get_pos()
    card, x, y = shop.get_square_under_mouse()
    drop_pos = [x, y]

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if card is not None:
                selected_card = card, x, y
        if event.type == pg.MOUSEBUTTONUP:
            print("card:", card)
            print("selected card:", selected_card)
            if (selected_card is not None) & (drop_pos is not None):
                card, old_x, old_y = selected_card
                shop.board[old_y][old_x] = 0
                new_x, new_y = drop_pos
                shop.board[new_y][new_x] = card
                shop.draw_board(update=True)
                print(shop.board)
            selected_card = None
            drop_pos = None

    # Clock
    clock.tick(60)

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(colors.BLACK)
    screen.blit(shop.surf, [0, 0])
    all_sprites.draw(screen)
    shop.sprites.draw(screen)

    # Flip the display
    pg.display.flip()


pg.quit()
