# import standard Pygame libraries
import os
import pygame as pg
from pygame.compat import geterror

# import modules from project
from SudokuFiles.Util import*

# a class to represent a Tile
class Tile(pg.sprite.Sprite):
    """A class to represent a sudoku tile
    PARAMETER STUFF
    . tileColor      (tuple)
    . loTileColors   (List of tuples)
    . numColor       (tuple)
    . loNumColors    (List of tuples)
    . num            (int)
    . row            (int)
    . column         (int)
    . guesses        (List of ints)
    . active         (boolean)
    . size           (int)
    . sideBuffer     (int)
    . textSize       (int)
    . textGuessSize  (int)
    """

    # constructor for a Tile
    def __init__(self, row, col, num):
        """requisite constructor"""

        # init sprite through pygame library
        pg.sprite.Sprite.__init__(self)

        # set fields to inputted values
        self.row = row
        self.col = col
        self.num = num

        # set some generic fields
        self.size = 50
        self.sideBuffer = 3
        self.textSize = 36
        self.textGuessSize = 20

        # list of tile and number colors
        self.loTileColors = [ (210, 210, 210), (190, 190, 250)]
        self.tileColor = self.loTileColors[0]
        self.loNumColors = [ (20, 20, 20), (80, 80, 80), (200, 10, 250) ]
        self.numColor  = self.loNumColors[0]

        # initialize the guesses field, and the active field as none
        self.guesses = []
        self.active = False

        # rectangle and image for Pygame
        myRect = pg.Rect( (1, 1), (self.size, self.size) )
        mySurface = pg.Surface( (self.size, self.size) )
        mySurface.fill( self.tileColor )
        self.rect = myRect
        self.image = mySurface


    # update method required for Pygame
    def update(self):
        """draws the object based on rando things"""
        # create the surface to pass to helpers
        mySurface = pg.Surface( (self.size, self.size) )
        # call method to set the color, then actually fill with color
        self.checkAndSetColor(mySurface)
        mySurface.fill(self.tileColor)
        # call method to set the number
        self.checkAndSetNumber(mySurface)
        # update object with edited surface
        self.image = mySurface


    # helper method to check if active and set color if so
    def checkAndSetColor(self, mySurface):
        """Checks to see if the tile is active, accordingly sets color"""
        # if its active set to light blue
        if (self.active):
            self.tileColor = self.loTileColors[1]
        # if its not active set to grey
        elif (not self.active):
            self.tileColor = self.loTileColors[0]


    # helper method to check and draw number if appropriate
    def checkAndSetNumber(self, mySurface):
        # number is zero, don't draw
        if (self.num == 0):
            pass
        # number is nonzero, pass to Util's helper method
        else:
            # instantiate a Util object
            util = Util()
            # setup all variables to use in method
            bg = mySurface
            fSize = self.textSize
            fStr = str(self.num)
            color = self.numColor
            posX = int(self.size / 2)
            posY = int(self.size / 2)
            # call Util's method to place the text
            util.placeTextOnBackground(bg, fSize, fStr, color, posX, posY)


    # helper method to set the color of the font
    def setColorType(self, type):
        """Sets the text color based on inputted string"""
        # color black by default
        tempColor = (0, 0, 0)
        # guesses are dark grey
        if (type == "input"):
            tempColor = (100, 100, 100)
        # output by 'solve' method are purple
        elif (type == "solve"):
            tempColor = (200, 10, 250)
        # call the setter to actually set it
        self.setColor(tempColor)


    # === setters
    def setActive(self):
        """Sets the active parameter to True, and color accordingly"""
        # TODO: FIX SOME SHIT
        self.active = True
        self.tileColor = (190, 190, 190)
        self.image.fill( self.tileColor )


    def setInactive(self):
        """Sets the field 'Active' to False"""
        self.active = False


    def setNumber(self, num):
        """Sets the field 'Number' to the given one"""
        self.num = num


    def setColor(self, color):
        """Sets the field 'color' to the given one"""
        self.numColor = color


    # === getters
    def getRow(self):
        """Returns the value of the field 'Row'"""
        return self.row


    def getCol(self):
        """Returns the value fo the field 'Col'"""
        return self.col


    def getTileSize(self):
        """Returns fhte value of the field 'size'"""
        return self.size


    def getTileBuffer(self):
        """Returns the value of the field 'buffer'"""
        return self.sideBuffer
