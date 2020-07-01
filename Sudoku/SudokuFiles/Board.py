# import standard Pygame libraries
import os
import pygame as pg
from pygame.compat import geterror

# import python modules
from random import*

# import modules from project
from .Tile import*
from .Util import*

# class to represent a board
class Board(pg.sprite.Sprite):
    """a board for testing purposes
    arrayTiles (2d array of Tile objects)
    """

    # constructor
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.arrayTiles = []
        self.buildBlankBoard()
        self.currentActive = None
        # call helpers to store tile size, buffer
        self.aTSize = self.getSingleTileSize()
        self.aTBuf = self.getSingleTileBuffer()
        # save helpful values based on tile size
        self.aTUnit = self.aTSize + (2 * self.aTBuf)
        self.bSize = (self.aTSize * 9) + (self.aTBuf * 18)
        # list of possible colors to be used
        self.bColors = [(10, 10, 10), (120, 120, 120)]
        # declare rect and image for Pygame
        myRect = pg.Rect( (1, 1), ( (self.bSize), (self.bSize) ) )
        myRect.midtop = (self.bSize, self.aTSize)
        self.rect = myRect
        mySurface = pg.Surface( ( (self.bSize), (self.bSize) ) )
        self.image = mySurface

    def buildBlankBoard(self):
        """ a method to build a standard sized sudoku board """
        # declare blank list
        arrayTiles = []
        # forloops to create an 2d array of blank tiles
        for i in range(0, 9):
            self.arrayTiles.append([])
            for j in range(0, 9):
                tileToAdd = Tile(i, j, 0)
                self.arrayTiles[i].append( tileToAdd )

    def update(self):
        """draws the object based on rando things"""
        # needed for Pygame
        myRect = pg.Rect( (1, 1), ( ( self.bSize ), ( self.bSize ) ) )
        mySurface = pg.Surface( ( ( self.bSize ), ( self.bSize ) ) )
        mySurface.fill( self.bColors[0] )
        # call helper to draw grey boxes for proper sudoku pattern
        self.drawMediumBoxes(mySurface)
        self.drawTilesOnBoard(mySurface)
        # declare surface and rect
        self.rect = myRect
        self.rect.midtop = ( (self.bSize / 2) , self.aTSize)
        # set the field to the just created one
        self.image = mySurface

    # helper to draw the grey boxes
    def drawMediumBoxes(self, mySurface):
        """draws 9 grey boxes onto the given surface
        to make it look like sudoku"""
        # get color from list
        colorMedium = self.bColors[1]
        # save lengths based on tile size and buffer
        lLong  = (3 * self.aTSize) + (5 * self.aTBuf)
        lShort = (3 * self.aTSize) + (4 * self.aTBuf)
        # declare different surface to place
        surfaceA = pg.Surface( (lLong, lLong) )
        surfaceA.fill( colorMedium )
        surfaceB = pg.Surface( (lShort, lLong) )
        surfaceB.fill( colorMedium )
        surfaceC = pg.Surface( (lLong, lShort) )
        surfaceC.fill( colorMedium )
        surfaceD = pg.Surface( (lShort, lShort) )
        surfaceD.fill( colorMedium )
        # save positions based on tile size and buffer
        posA = 0
        posB = (3 * self.aTSize) + (7 * self.aTBuf)
        posC = (6 * self.aTSize) + (13 * self.aTBuf)
        # blit all 9 grey boxes
        mySurface.blit( surfaceA, (posA, posA) )
        mySurface.blit( surfaceB, (posB, posA) )
        mySurface.blit( surfaceA, (posC, posA) )
        mySurface.blit( surfaceC, (posA, posB) )
        mySurface.blit( surfaceD, (posB, posB) )
        mySurface.blit( surfaceC, (posC, posB) )
        mySurface.blit( surfaceA, (posA, posC) )
        mySurface.blit( surfaceB, (posB, posC) )
        mySurface.blit( surfaceA, (posC, posC) )


    # helper method to draw the tiles
    def drawTilesOnBoard(self, mySurface):
        """draws every tile in the array of tiles on to the given surface"""
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.arrayTiles[i][j]
                xPos = (self.aTUnit / 2) + (j * self.aTUnit)
                yPos = (self.aTUnit / 2) + (i * self.aTUnit)
                surface = tile.image
                posPlace = surface.get_rect(centerx = xPos, centery = yPos)
                mySurface.blit(surface, posPlace)
                # break out of 'j' loop
            # break out of 'i' forloop


    # === BACKTRACKING TO SOLVE BOARD ===

    def solveBoard(self):
        """Recursive backtracking algorithm to try and solve the Sudoku board"""
        # search for an empty location on the board
        val = self.findEmptyLocation()
        # if method returned false, we've completely filled board and are done
        if(val == False):
            return True # yatzee :)
        # assign these in prep to check this location
        row = val[0]
        col = val[1]
        # if not, proceed with recursive backtracking algorithm
        for numCheck in range(1, 10):
            # calls check if safe, and if safe, assigns and recurs
            if (self.checkIfSafe(numCheck, row, col) ):
                self.arrayTiles[row][col].setNumber(numCheck)
                self.arrayTiles[row][col].setColorType("solve")
                self.arrayTiles[row][col].update()
                self.update()
                if( self.solveBoard() ):
                    # if it finally makes it here, it found a solution
                    return True
                # otherwise, reset this tile to 0
                self.arrayTiles[row][col].setNumber(0)
        # and backtrack to look for a solution
        return False

    # helper for solveBoard
    def findEmptyLocation(self):
        """Finds the next empty location on the board"""
        for i in range(0, 9):
            for j in range(0, 9):
                # first empty location found, return true
                if (self.arrayTiles[i][j].num == 0):
                    tile = self.arrayTiles[i][j]
                    val = [tile.row, tile.col]
                    return val
        # if it didn't find an empty location, return false
        return False


    # helper for backtracking
    def checkIfSafe(self, aNumb, aRow, aCol):
        """Checks if given number is safe to place per sudoku rules"""
        a = self.checkRow(aNumb, aRow)
        b = self.checkCol(aNumb, aCol)
        c = self.checkSqu(aNumb, aRow, aCol)
        # if they all return True
        if(a and b and c):
            return True
        else:
            return False


    # helper for checkIfSafe
    def checkRow(self, aNumb, aRow):
        """Lists all number in square, passes to checkListOk"""
        theList = [aNumb]
        # add all numbers in the row to the aList
        for j in range(0, 9):
            tileCheck = self.arrayTiles[aRow][j]
            if (tileCheck.num != 0):
                theList.append(tileCheck.num)
        # passes list to helper to check
        return self.checkListOK(theList)


    # helper for checkIfSafe
    def checkCol(self, aNumb, aCol):
        """Lists all number in square, passes to checkListOk"""
        theList = [aNumb]
        # adds all the numbers in the column to the list
        for i in range(0, 9):
            tileCheck = self.arrayTiles[i][aCol]
            if (tileCheck.num != 0):
                theList.append(tileCheck.num)
        # passes the list to the helper
        return self.checkListOK(theList)


    # helper for checkIfSafe
    def checkSqu(self, aNumb, aRow, aCol):
        """Lists all number in square, passes to checkListOk"""
        theList = [aNumb]
        # if to cover my ass for index out of bounds errors
        if (aRow == None or aCol == None):
            pass
        else:
            rowChunk = int(aRow / 3)
            colChunk = int(aCol / 3)
            # loops to add the stuff
            for i in range(0, 9):
                for j in range(0, 9):
                    tileCheck = self.arrayTiles[i][j]
                    rowT = int(tileCheck.row / 3)
                    colT = int(tileCheck.col / 3)
                    if ( (rowT == rowChunk and colT == colChunk) ):
                        if (tileCheck.num != 0):
                            theList.append(tileCheck.num)
            # pass to a helper
            return self.checkListOK(theList)


    # helper for checkCol, Row, Squ
    def checkListOK(self, aList):
        """ check list to see if the number is already contained"""
        toReturn = True
        for q in range(1, 10):
            if(aList.count(q) > 1):
                toReturn = False
            # end 'q' forloop
        return toReturn


    # setting the current active
    def setCurrentActive(self, aTile):
        """Inactivates current active tile, sets given tile as active"""
        # if there is a current active, make it inactive and update
        if (self.currentActive != None):
            self.currentActive.setInactive()
            self.currentActive.update()
        # set the given tile as active, and update
        self.currentActive = aTile
        self.currentActive.setActive()
        self.currentActive.update()


    # Used with Game keyhandler, sets the active tile's number to the given
    def setCurrentActiveNumber(self, aNumb):
        """Changes the number of the active tile to the given"""
        # if there is no active tile, do nothing
        if (self.currentActive == None):
            pass
        # set the number of the current active, and update
        self.currentActive.setNumber(aNumb)
        self.currentActive.setColorType("input")
        self.currentActive.update()


    # digs a layer down to get the tile size
    def getSingleTileSize(self):
        """returns the size of the tiles in the board"""
        toReturn = self.arrayTiles[0][0].getTileSize()
        return toReturn


    # digs a layer down to get buffer size
    def getSingleTileBuffer(self):
        """returns the size of the buffer of tiles in the board"""
        toReturn = self.arrayTiles[0][0].getTileBuffer()
        return toReturn


    # wipes the whole board
    def wipeBoard(self):
        """sets every tile to a number value of 0"""
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.arrayTiles[i][j]
                tile.setNumber(0)
                tile.update()


    # generates a puzzle to play
    def generatePuzzle(self):
        """generates a puzzle for the user"""
        # wipe the board
        self.wipeBoard()
        # seeds the first row with a random sequence of 1-9
        self.seedFirstRow()
        # solves the board
        self.solveBoard()
        # set all number colors to black
        self.setAllTileNumColor("dicks")
        # obscures a number of tiles randomly
        self.obscureTiles()



    # helper for generate puzzle
    def seedFirstRow(self):
        """Randomly shuffles a list (1, 9) to seed the first row of tiles"""
        rand = Random()
        l = list(range(1, 10))
        rand.shuffle( l )
        # use the random list to seed the first row
        for i in range(0, 9):
            tile = self.arrayTiles[0][i]
            tile.setNumber( l[i] )
            # already updates in set all colors, called right after


    # helper for generate puzzle
    def setAllTileNumColor(self, aColorString):
        """sets the colors of all the tile numbers to the given"""
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.arrayTiles[i][j]
                tile.setColorType(aColorString)
                tile.update()


    # helper for generate puzzle
    def obscureTiles(self):
        oCount = 45
        rand = Random()
        # just obscure random tiles until the number ticks to 0
        while (oCount != 0):
            randRow = rand.randint(0, 8)
            randCol = rand.randint(0, 8)
            randTile = self.arrayTiles[randRow][randCol]
            if (randTile.num != 0):
                randTile.setNumber(0)
                oCount = oCount - 1
                randTile.update()
            # if its already 0, loop around
            else:
                pass
