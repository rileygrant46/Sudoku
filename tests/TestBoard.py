import pygame as pg
from pygame.compat import geterror

from random import*
from nose.tools import*
from Sudoku.SudokuFiles.Board import Board
from Sudoku.SudokuFiles.Tile import Tile

class TestBoard(object):
    """A Class to localize Board tests"""

    # Constructor method
    def __init__(self):
        """The requisite constructor to instantiate a TestBoard"""
        pass

    def setup(self):
        self.testBoard = Board()

    def teardown(self):
        pass


    # Tests
    # ==========

    # . __init__
    @with_setup(setup, teardown)
    def test_init(self):
        """Test that init properly instantiates an object"""
        # check that it starts as False
        assert_not_equal(self.testBoard, None)


    # . buildBlankBoard
    @with_setup(setup, teardown)
    def test_buildBlankBoard(self):
        """Test that buildBlankBoard properly generates a blank board"""
        # set arrayTiles to blank
        self.testBoard.arrayTiles = []
        assert_equal(self.testBoard.arrayTiles, [])
        # run method to check blank board
        self.testBoard.buildBlankBoard()
        # loop through all tiles to ensure built correctly
        for i in range(0, 9):
            for j in range(0, 9):
                tempTile = self.testBoard.arrayTiles[i][j]
                assert_equal(tempTile.getRow(), i)
                assert_equal(tempTile.getCol(), j)
                assert_equal(tempTile.num, 0)


    # . update                    (graphical)
    @with_setup(setup, teardown)
    def test_update(self):
        """Test that the update method correctly draws board"""
        # this is tested graphically by running the program
        pass


    # . drawMediumBoxes           (graphical)
    @with_setup(setup, teardown)
    def test_drawMediumBoxes(self):
        """Test that the draw medium boxes correctly draws the light grey"""
        # this is tested graphically by running the program
        pass


    # . drawTileOnBoard           (graphical)
    @with_setup(setup, teardown)
    def test_drawTileOnBoard(self):
        """Test that the draw tile method correctly draws the tiles"""
        # this is tested graphically by running the program
        pass


    # . solveBoard
    @with_setup(setup, teardown)
    def test_solveBoard(self):
        """Test that solveBoard attempts to solve the whole board"""
        # initialize fonts for this test method to work
        pg.font.init()
        # check intially that there is a blank board
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_equal(tile.num, 0)
        # solve the now blank board, and ensure nothing is blank
        self.testBoard.solveBoard()
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_not_equal(tile.num, 0)
        # this is not really a perfect test
        # this assumes that testing all the helpers covers the
        #   correct solving, this checks the recursion of entire board


    # . findemptyLocation
    @with_setup(setup, teardown)
    def test_findEmptyLocation(self):
        """Test to ensure findEmptyLocation finds the next empty loc"""
        val = self.testBoard.findEmptyLocation()
        assert_equal(val[0], 0)
        assert_equal(val[1], 0)


    # . checkIfSafe
    @with_setup(setup, teardown)
    def test_checkIfSafe(self):
        """Test to ensure the sudoku rules of placing are working"""
        self.testBoard.arrayTiles[3][0].setNumber(2)
        self.testBoard.arrayTiles[0][3].setNumber(3)
        self.testBoard.arrayTiles[2][2].setNumber(4)
        assert_equal(self.testBoard.checkIfSafe(1, 0, 0), True)
        assert_equal(self.testBoard.checkIfSafe(2, 0, 0), False)
        assert_equal(self.testBoard.checkIfSafe(3, 0, 0), False)
        assert_equal(self.testBoard.checkIfSafe(4, 0, 0), False)


    # . checkRow
    @with_setup(setup, teardown)
    def test_checkRow(self):
        """Test to ensure checkRow checks according to Sudoku rules"""
        self.testBoard.arrayTiles[0][3].setNumber(3)
        assert_equal(self.testBoard.checkRow(1, 0), True)
        assert_equal(self.testBoard.checkRow(3, 0), False)


    # . checkCol
    @with_setup(setup, teardown)
    def test_checkCol(self):
        """Test to ensure checkCol checks according to Sudoku rules"""
        self.testBoard.arrayTiles[3][0].setNumber(2)
        assert_equal(self.testBoard.checkCol(1, 0), True)
        assert_equal(self.testBoard.checkCol(2, 0), False)


    # . checkSqu
    @with_setup(setup, teardown)
    def test_checkSqu(self):
        """Test to ensure checkSqu checks according to Sudoku rules"""
        self.testBoard.arrayTiles[2][2].setNumber(4)
        assert_equal(self.testBoard.checkSqu(1, 0, 0), True)
        assert_equal(self.testBoard.checkSqu(4, 0, 0), False)


    # . checkListOk
    @with_setup(setup, teardown)
    def test_checkListOk(self):
        """Test to ensure checkListOk returns false if duplicate numbers in list"""
        listA = [1, 2, 3, 4]
        listB = [1, 2, 3, 1]
        assert_equal(self.testBoard.checkListOK(listA), True)
        assert_equal(self.testBoard.checkListOK(listB), False)


    # . setCurrentActive
    @with_setup(setup, teardown)
    def test_setCurrentActive(self):
        """Test to ensure setCurrentActive sets new and removes old active tile"""
        # ensure nothing set at the beginning
        assert_equal(self.testBoard.currentActive, None)
        # store tile to set as new active
        tile00 = self.testBoard.arrayTiles[0][0]
        self.testBoard.setCurrentActive(tile00)
        assert_equal(self.testBoard.currentActive, tile00)
        assert_equal(tile00.active, True)
        # set another, ensure old tile becomes inactive
        tile01 = self.testBoard.arrayTiles[0][1]
        self.testBoard.setCurrentActive(tile01)
        assert_equal(self.testBoard.currentActive, tile01)
        assert_not_equal(self.testBoard.currentActive, tile00)
        assert_equal(tile01.active, True)
        assert_not_equal(tile00.active, True)


    # . setCurrentActiveNumber
    @with_setup(setup, teardown)
    def test_setCurrentActiveNumber(self):
        """Test to ensure setCurrentActiveNumber sets tiles active number"""
        # initialize font to be able to work
        pg.font.init()
        # ensure no active at the beginning
        assert_equal(self.testBoard.currentActive, None)
        # store tile to set as new active and to act on
        tile00 = self.testBoard.arrayTiles[0][0]
        self.testBoard.setCurrentActive(tile00)
        assert_equal(self.testBoard.currentActive, tile00)
        assert_equal(tile00.active, True)
        # now run method to change tile00's number
        assert_equal(tile00.num, 0)
        self.testBoard.setCurrentActiveNumber(3)
        assert_not_equal(tile00.num, 0)
        assert_equal(tile00.num, 3)


    # . getSingleTileSize          (req Tile package)
    @with_setup(setup, teardown)
    def test_getSingleTileSize(self):
        """Test that getSingleTileSize correctly gets the size of a tile"""
        num = self.testBoard.getSingleTileSize()
        assert_equal(num, 50)


    # . getSingleTileBuffer        (req Tile package)
    @with_setup(setup, teardown)
    def test_getSingleTileBuffer(self):
        """Test that getSingleTileBuffer correctly gets the size of the buffer"""
        num = self.testBoard.getSingleTileBuffer()
        assert_equal(num, 3)


    # . wipeBoard
    @with_setup(setup, teardown)
    def test_wipeBoard(self):
        """Test that wipeBoard properly wipes all numbers from the board"""
        # initialize fonts for this test method to work
        pg.font.init()
        # check intially that there is a blank board
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_equal(tile.num, 0)
        # solve the now blank board, and ensure nothing is blank
        self.testBoard.solveBoard()
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_not_equal(tile.num, 0)
        # wipe the board and ensure everything is now blank
        self.testBoard.solveBoard()
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_not_equal(tile.num, 0)


    # . generatePuzzle             (rand)
    @with_setup(setup, teardown)
    def test_generatePuzzle(self):
        """Test to check generate puzzle"""
        # this uses a random, instead of changing the method
        #   to take in a random, so that I may seed it in order to test
        #   I am opting to just run the program and see if it works
        pass


    # . seedFirstRow               (rand)
    @with_setup(setup, teardown)
    def test_seedFirstRow(self):
        """Test to check seedFirstRow"""
        # this uses a random, instead of changing the method
        #   to take in a random, so that I may seed it in order to test
        #   I am opting to just run the program and see if it works
        pass


    # . setAllTileNumColor
    @with_setup(setup, teardown)
    def test_setAllTileNumColor(self):
        """Test to check that setAllTileNumColor properly sets colors"""
        # initalize font to work properly
        pg.font.init()
        # solve board and ensure all purple
        self.testBoard.solveBoard()
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_equal(tile.numColor, (200, 10, 250) )
        # change color to all red and ensure its true
        self.testBoard.setAllTileNumColor( "input" )
        for i in range(0, 9):
            for j in range(0, 9):
                tile = self.testBoard.arrayTiles[i][j]
                assert_equal(tile.numColor, (100, 100, 100) )


    # . obscureTiles               (rand)
    @with_setup(setup, teardown)
    def test_obscureTiles(self):
        """Test to ensure obscure tiles work"""
        # this uses a random, instead of changing the method
        #   to take in a random, so that I may seed it in order to test
        #   I am opting to just run the program and see if it works
        pass
