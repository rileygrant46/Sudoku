# import standard Pygame libraries
import os
import pygame as pg
from pygame.compat import geterror

# import modules from project
from SudokuFiles.Tile import*
from SudokuFiles.Board import*

# class for Utils
class Util(object):
    """A util class for generic methods"""

    # constructor for a util
    def __init__(self):
        """init method to construct a Util object"""
        # really this does nothing, UTILs are only important for their methods
        pass


    # consolidates repetitive code, places the text on the given surface
    def placeTextOnBackground(self, surf, fSize, string, color, locx, locy):
        """A util method to place text on the given surface"""
        if pg.font:
            font = pg.font.Font(None, fSize)
            text = font.render(string, True, color)
            textpos = text.get_rect(centerx = locx, centery = locy)
            surf.blit(text, textpos)
