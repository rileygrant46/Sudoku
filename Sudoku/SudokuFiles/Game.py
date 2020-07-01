# import relevant modules
from .Board import*
from .Util import*

# issue warning if Pygame modules don't properly load
if not pg.font:
    print ("Warning, fonts disabled!")
if not pg.mixer:
    print ("Warning, sounds disabled!")


# game class, holds a Board object and variables
class Game(pg.sprite.Sprite):
    """A class to represent a game"""


    # the __init__ method as constructor
    def __init__(self):
        """requisite constructor"""
        pg.init()
        self.board = Board()
        self.gameWidth = self.board.bSize
        self.gameHeight = self.board.bSize + (self.board.aTSize * 4)
        self.screen = pg.display.set_mode((self.gameWidth, self.gameHeight))
        pg.display.set_caption("Sudoku")
        pg.mouse.set_visible(1)
        # instantiate board and a utility object
        self.util = Util()
        self.running = False
        # prep background
        self.bgColor = (180, 180, 180)
        self.bg = pg.Surface(self.screen.get_size())
        self.bg.convert()
        self.bg.fill(self.bgColor)
        self.textColor = (10, 10, 10)
        # if font is working, add header and footer text
        if pg.font:
            self.gameAddText()
        self.rect = None
        self.image = None
        # prepare Pygame objects
        self.clock = pg.time.Clock()
        self.allsprites = pg.sprite.RenderPlain(self.board)
        # display the background
        self.screen.blit(self.bg, (0, 0) )
        pg.display.update()


    # helper method for init
    def gameAddText(self):
        """Uses a Util helper to blit the info text onto the board"""
        # text global stuff
        textColor = self.textColor
        bg = self.bg
        midX = int(bg.get_width() / 2)
        # add text above board with helper
        hSize = 36
        hString = "Welcome to Sudoku!"
        hLocY = self.board.aTSize / 2
        self.util.placeTextOnBackground(bg, hSize, hString, textColor, midX, hLocY)
        # add text below board with helper
        fSize = 24
        fStrA = "Click or use the arrow keys to change the active tile"
        fYA = hLocY+self.board.bSize + (hLocY * 2)
        self.util.placeTextOnBackground(bg, fSize, fStrA, textColor, midX, fYA)
        fStrB = "Use the number keys to input a number"
        fYB = hLocY+self.board.bSize + (hLocY * 3)
        self.util.placeTextOnBackground(bg, fSize, fStrB, textColor, midX, fYB)
        fStrC = "Press 'K' at any point to solve the puzzle"
        fYC = hLocY+self.board.bSize + (hLocY * 4)
        self.util.placeTextOnBackground(bg, fSize, fStrC, textColor, midX, fYC)
        fStrD = "Press 'C' at any point to clear the current puzzle"
        fYD = hLocY+self.board.bSize + (hLocY * 5)
        self.util.placeTextOnBackground(bg, fSize, fStrD, textColor, midX, fYD)
        fStrE = "Press 'G' at any point to generate a new puzzle"
        fYE = hLocY+self.board.bSize + (hLocY * 6)
        self.util.placeTextOnBackground(bg, fSize, fStrE, textColor, midX, fYE)


    # update method for pygame
    def update(self):
        """Draws the game onto the background"""
        # ended up doing nothing here, the background only gets drawn once
        #  and just runs update() on the board
        pass


    def runGame(self):
        """Runs the game"""
        # run main loop stuff
        self.running = True
        while (self.running):
            # make the clock tick at 60 tps
            self.clock.tick(60)
            # handle input events
            for event in pg.event.get():
                # handlers to end game
                self.gameHandleEvents(event)
            # draw everything
            self.doEveryTick()


    def gameHandleEvents(self, event):
        """Runs all event handlers"""
        self.endGameHandlers(event)
        self.mouseClickHandler(event)
        self.arrowKeysHandler(event)
        self.inputNumberHandler(event)
        self.generatePuzzleHandler(event)
        self.clearBoardHandler(event)
        self.solveBoardHandler(event)


    def endGameHandlers(self, event):
        """Handler to end game"""
        # handlers to end game
        if event.type == pg.QUIT:
            self.running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.running = False


    def mouseClickHandler(self, event):
        """Handler for mouse click"""
        # handler to click to make a tile active
        if (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
            pos = pg.mouse.get_pos()
            # integer division to determine which row, col
            rowClick = int( ( (pos[1] - 50) / 56) )
            colClick = int( (pos[0] / 56) )
            if (rowClick < 9 and colClick < 9):
                tile = self.board.arrayTiles[rowClick][colClick]
                self.board.setCurrentActive(tile)


    def arrowKeysHandler(self, event):
        """Handler for arrow keys"""
        # initialize list to check
        arrowKeys = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]
        # number keys for shifting active handler
        if (event.type == pg.KEYDOWN and arrowKeys.count(event.key) > 0):
            # if no active, set (0, 0) as active
            if (self.board.currentActive == None):
                self.board.setCurrentActive(self.board.arrayTiles[0][0])
            # ugly ass ifs to check which key it is, check one thing, then change
            else:
                # save current row and col
                tempRow = self.board.currentActive.row
                tempCol = self.board.currentActive.col
                tile = self.board.arrayTiles[tempRow][tempCol]
                # ifs to prevent index out of bound
                if (event.key == pg.K_UP and tempRow > 0):
                    tile = self.board.arrayTiles[tempRow - 1][tempCol]
                elif (event.key == pg.K_DOWN and tempRow < 8):
                    tile = self.board.arrayTiles[tempRow + 1][tempCol]
                elif (event.key == pg.K_LEFT and tempCol > 0):
                    tile = self.board.arrayTiles[tempRow][tempCol - 1]
                elif (event.key == pg.K_RIGHT and tempCol < 8):
                    tile = self.board.arrayTiles[tempRow][tempCol + 1]
                # actually set the active
                self.board.setCurrentActive(tile)

    def inputNumberHandler(self, event):
        """Handler for input of numbers"""
        # relevant lists
        numberGuesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 69, 0, 0]
        numberGuesses2 = [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4,
                            pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_r,
                            pg.K_DELETE, pg.K_BACKSPACE]
        # check for this action
        if (event.type == pg.KEYDOWN and numberGuesses2.count(event.key) > 0):
            if (self.board.currentActive == None):
                pass
            index = numberGuesses2.index(event.key)
            num = numberGuesses[index]
            self.board.setCurrentActiveNumber(num)

    def generatePuzzleHandler(self, event):
        """Handler for generating puzzle"""
        if (event.type == pg.KEYDOWN and event.key == pg.K_g):
            self.board.generatePuzzle()

    def clearBoardHandler(self, event):
        """Handler to clearing board"""
        # wipe board handler
        if (event.type == pg.KEYDOWN and event.key == pg.K_c):
            self.board.wipeBoard()

    def solveBoardHandler(self, event):
        """Handler for solving board"""
        # solve board handler
        if (event.type == pg.KEYDOWN and event.key == pg.K_k):
            self.board.solveBoard()


    def doEveryTick(self):
        """runs this every tick"""
        self.allsprites.update()
        self.screen.blit(self.bg, (0, 0))
        self.allsprites.draw(self.screen)
        pg.display.update()
