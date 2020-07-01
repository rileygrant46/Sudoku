
import pygame as pg

from nose.tools import*
from Sudoku.SudokuFiles.Game import Game

class TestGame(object):
    """A Class to localize Game tests"""

    # Constructor method
    def __init__(self):
        """The requisite constructor to instantiate a TestBoard"""
        pass

    def setup(self):
        self.testGame = Game()

    def teardown(self):
        pass


    # Tests
    # ==========

    @with_setup(setup, teardown)
    def test_stub(self):
        """A method to test that """
        pass


    # Methods:
    # ==========

    # . __init__
    @with_setup(setup, teardown)
    def test_init(self):
        """Test that init properly instantiates an object."""
        assert_not_equal(self.testGame, None)


    # . gameAddText                    (graphical)
    @with_setup(setup, teardown)
    def test_gameAddText(self):
        """Test that gameAddText properly blits the text onto tiles."""
        # this is tested graphically, it is UI
        pass


    # . update                         (graphical)
    @with_setup(setup, teardown)
    def test_update(self):
        """Test that update properly updates tiles per data."""
        # this is tested graphically, as it is UI
        pass

    # . runGame                        (loops, runs game)
    @with_setup(setup, teardown)
    def test_runGame(self):
        """Test that runGame properly starts and runs the game"""
        # this is tested by playing the game. No good way to unit test this.
        pass

    # . gameHandleEvents               (test by all sub methods)
    @with_setup(setup, teardown)
    def test_gameHandleEvents(self):
        """Test that gameHandleEvents properly """
        # this kinda gonna be reiterating the other tests??
        # the tests of all the individual methods below make this test work
        pass

    # . endGameHandlers
    @with_setup(setup, teardown)
    def test_endGameHandlers1(self):
        """Test that endGameHandlers properly ends game"""
        # check that it starts as False
        assert_equal(self.testGame.running, False)
        # set explicitly to True, make sure it is set
        self.testGame.running = True
        assert_equal(self.testGame.running, True)
        # create a Quit type Pygame event, and run with method, then check
        eventQuit = pg.event.Event(pg.QUIT)
        self.testGame.endGameHandlers(eventQuit)
        assert_equal(self.testGame.running, False)

    @with_setup(setup, teardown)
    def test_endGameHandlers1(self):
        """Test that endGameHandlers properly ends game"""
        # check that it starts as False
        assert_equal(self.testGame.running, False)
        # set explicitly to True, make sure it is set
        self.testGame.running = True
        assert_equal(self.testGame.running, True)
        # create a Quit type Pygame event, and run with method, then check
        eventEscape = pg.event.Event(pg.KEYDOWN)
        pass


    # . mouseClickHandler
    # . arrowKeysHandler
    # . inputNumberHandler
    # . generatePuzzleHandler
    # . clearBoardHandler
    # . solveBoardHandler
    # . doEveryTick
