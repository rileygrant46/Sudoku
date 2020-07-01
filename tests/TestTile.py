from nose.tools import*
from Sudoku.SudokuFiles.Tile import Tile



class TestTile(object):

    def __init__(self):
        self.testVar = 1

    @classmethod
    def setup_class(klass):
        pass

    @classmethod
    def teardown_class(klass):
        pass


    def setup(self):
        pass
        #self.testVar = 10

    def teardown(self):
        pass
        #self.testVar = 10


    def test_init(self):
        tile = Tile(1, 1, 1)
        assert_not_equal(None, tile)
