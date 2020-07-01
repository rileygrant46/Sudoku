import pygame as pg

from nose.tools import*
from Sudoku.SudokuFiles.Tile import Tile

class TestTile(object):
    """A Class to represent testing of the Tile methods"""

    # constructor method
    def __init__(self):
        """The requisite constructor to Instantiate a TestTile Object"""
        self.testTile = None
        # dummy surface to use in test methods
        self.mySurface = None


    def setup(self):
        """A Setup method to be run before each test"""
        self.testTile = Tile(1, 1, 1)
        self.mySurface = pg.Surface( (10, 10) )


    def teardown(self):
        """A Teardown method to be run after each test"""
        pass


    # Tests
    # ===================



    @with_setup(setup, teardown)
    def test_init(self):
        """A method to test that __init__ creates an object"""
        assert_not_equal(None, self.testTile)


    @with_setup(setup, teardown)
    def test_setActive(self):
        """A method to test that setActive works properly"""
        assert_equal(self.testTile.active, False)
        self.testTile.setActive()
        assert_equal(self.testTile.active, True)


    @with_setup(setup, teardown)
    def test_setInactive(self):
        """A method to test that setInactive works properly"""
        assert_equal(self.testTile.active, False)
        self.testTile.setActive()
        assert_equal(self.testTile.active, True)
        self.testTile.setInactive()
        assert_equal(self.testTile.active, False)


    @with_setup(setup, teardown)
    def test_setNumber(self):
        """A method to test that setNumber works properly"""
        assert_equal(self.testTile.num, 1)
        self.testTile.setNumber(4)
        assert_equal(self.testTile.num, 4)


    @with_setup(setup, teardown)
    def test_setColor(self):
        """A method to test that setColor works properly"""
        assert_equal(self.testTile.numColor, (10, 10, 10) )
        self.testTile.setColor( (150, 150, 150) )
        assert_equal(self.testTile.numColor, (150, 150, 150) )


    @with_setup(setup, teardown)
    def test_getRow(self):
        """A method to test that getRow works properly"""
        assert_equal(self.testTile.getRow(), 1)


    @with_setup(setup, teardown)
    def test_getCol(self):
        """A method to test that getCol works properly"""
        assert_equal(self.testTile.getCol(), 1)


    @with_setup(setup, teardown)
    def test_getTileSize(self):
        """A method to test that getTileSize works properly"""
        assert_equal(self.testTile.getTileSize(), 50)


    @with_setup(setup, teardown)
    def test_getBuffer(self):
        """A method to test that getTileBuffer works properly"""
        assert_equal(self.testTile.getTileBuffer(), 3)

    @with_setup(setup, teardown)
    def test_update(self):
        """A method to test that the update method works properly"""
        # this is really tested graphically, no unit test here
        pass


    @with_setup(setup, teardown)
    def test_checkAndSetColor(self):
        """A method to test that checkAndSetColor works properly"""
        # make explicitly sure that the tile is inactive, check functionality
        self.testTile.setInactive()
        self.testTile.checkAndSetColor()
        assert_equal(self.testTile.tileColor, (210, 210, 210) )
        # make explicitly sure that the tile is active, check functionality
        self.testTile.setActive()
        self.testTile.checkAndSetColor()
        assert_equal(self.testTile.tileColor, (190, 190, 250) )


    @with_setup(setup, teardown)
    def test_checkAndSetNumber(self):
        """A method to test that checkAndSetNumber works properly"""
        assert_equal(self.testTile.num, 1)
        self.testTile.setNumber(0)
        self.testTile.checkAndSetNumber(self.mySurface)
        assert_equal(self.testTile.num, 0)

    @with_setup(setup, teardown)
    def test_setColorType(self):
        """A method to test that setColorType works properly"""
        assert_equal(self.testTile.numColor, (10, 10, 10) )
        # make sure other strings do nothing to the text
        self.testTile.setColorType("dummy")
        assert_equal(self.testTile.numColor, (10, 10, 10) )
        # check the grey text on putting in input
        self.testTile.setColorType("input")
        assert_equal(self.testTile.numColor, (100, 100, 100) )
        # check the purple text on inputting solve
        self.testTile.setColorType("solve")
        assert_equal(self.testTile.numColor, (200, 10, 250) )
