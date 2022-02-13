# -*- coding: utf-8 -*-
"""
Game Board

Created on Sat Feb  5 17:36:43 2022

@author: mrkno
"""

import pygame as pg

TILESIZE = 32
BOARD_POS = (10, 10)


def create_board_surf():
    # Make an 8x8 grid surface
    board_surf = pg.Surface((TILESIZE*8, TILESIZE*8))
    dark = False
    # iterate over 8x8 grid drawing rect of alternating colors
    for y in range(8):
        for x in range(8):
            rect = pg.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(board_surf, pg.Color('darkgrey' if dark else 'beige'), rect)
            dark = not dark
        dark = not dark
    # return surface with 8x8 grid drawn on it
    return board_surf


def get_square_under_mouse(board):
    # Get mouse position, in terms of gridsize, and x/y
    mouse_pos = pg.Vector2(pg.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILESIZE) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0:
            return (board[y][x], x, y)
    except IndexError:
        pass
    return None, None, None


def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)

    for x in range(0, 8):
        board[1][x] = ('black', 'pawn')
    for x in range(0, 8):
        board[6][x] = ('white', 'pawn')
    return board


def draw_pieces(screen, board, font, selected_piece):
    sx, sy = None, None
    if selected_piece:
        piece, sx, sy = selected_piece

    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if piece:
                selected = x == sx and y == sy
                color, type = piece
                s1 = font.render(type[0], True, pg.Color('red' if selected else color))
                s2 = font.render(type[0], True, pg.Color('darkgrey'))
                pos = pg.Rect(BOARD_POS[0] + x * TILESIZE+1, BOARD_POS[1] + y * TILESIZE + 1, TILESIZE, TILESIZE)
                screen.blit(s2, s2.get_rect(center=pos.center).move(1, 1))
                screen.blit(s1, s1.get_rect(center=pos.center))


def draw_selector(screen, piece, x, y):
    if piece is not None:
        rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, (255, 0, 0, 50), rect, 2)


def draw_drag(screen, board, selected_piece, font):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x is not None:
            rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(screen, (0, 255, 0, 50), rect, 2)

        color, type = selected_piece[0]
        s1 = font.render(type[0], True, pg.Color(color))
        s2 = font.render(type[0], True, pg.Color('darkgrey'))
        pos = pg.Vector2(pg.mouse.get_pos())
        screen.blit(s2, s2.get_rect(center=pos + (1, 1)))
        screen.blit(s1, s1.get_rect(center=pos))
        selected_rect = pg.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.line(screen, pg.Color('red'), selected_rect.center, pos)
        return (x, y)


def main():
    pg.init()
    font = pg.font.SysFont('', 32)
    screen = pg.display.set_mode((640, 480))
    board = create_board()
    board_surf = create_board_surf()
    clock = pg.time.Clock()
    selected_piece = None
    drop_pos = None
    while True:
        piece, x, y = get_square_under_mouse(board)
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                return
            if e.type == pg.MOUSEBUTTONDOWN:
                if piece is not None:
                    selected_piece = piece, x, y
            if e.type == pg.MOUSEBUTTONUP:

                if drop_pos:
                    piece, old_x, old_y = selected_piece
                    board[old_y][old_x] = 0
                    new_x, new_y = drop_pos
                    board[new_y][new_x] = piece
                selected_piece = None
                drop_pos = None

        screen.fill(pg.Color('grey'))
        screen.blit(board_surf, BOARD_POS)
        draw_pieces(screen, board, font, selected_piece)
        draw_selector(screen, piece, x, y)
        drop_pos = draw_drag(screen, board, selected_piece, font)

        pg.display.flip()
        clock.tick(60)
        print("P, X, Y:\t", piece, x, y)
        print("Events:\t", events)
        print("Selected Piece:\t", selected_piece)
        print("Drop pos:\t", drop_pos)


if __name__ == '__main__':
    main()
