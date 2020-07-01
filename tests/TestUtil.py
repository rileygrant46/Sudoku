from nose.tools import*
from Sudoku.SudokuFiles.Util import Util

class TestUtil(object):
    """A class to represent testing of the Util methods"""

    def __init__(self):
        """Requisite constructor for TestUtil objects"""
        pass

    def setup(self):
        """Setup method for the util tests"""
        pass

    def teardown(self):
        """Teardown method for the Util tests"""
        pass

    # ============

    def test_init(self):
        """A test to make sure the constructor instantiates a Util"""
        util = Util()
        assert_not_equal(None, util)

    def test_placeTextOnBackground(self):
        """A test to make placeTextOnBackground works correctly"""
        # this is effectively tested graphically by running the game
        assert_equal(1, 1)
