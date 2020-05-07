# import relevant modules
from Sudoku.Board import*
from Sudoku.Util import*

# issue warning if Pygame modules don't properly load
if not pg.font:
    print ("Warning, fonts disabled!")
if not pg.mixer:
    print ("Warning, sounds disabled!")

# setup static directories for graphics - never used in this
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

# declare generic variables
width = 504
height = 700
bgColor = (180, 180, 180)

# instantiate a Util for use in file
util = Util()


# fucckkkk turn Game into a class?
# there will be a static main function
#  java has like,
#    public static void main(string[] args){
#      blablabla
#    }
#  for all its main function pretty much for this reason
#    its truly an OO language by design. so you always declare a static
#    method in a main class.
#
#  Just have the Game have a main method
#    and make a main class, that holds a 'game'
#    then the main class will have a static method that calls the
#    Game's main method.
#      ez gg?

# main function
def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in a loop
    until the function returns."""

    # intialize some shit
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("My Test!")
    pg.mouse.set_visible(1)

    # create the background
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(bgColor)

    # add text to game
    if pg.font:
        # text global stuff
        textColor = (10, 10, 10)
        midX = int(background.get_width() / 2)
        bg = background

        # header text
        hSize = 36
        #
        hString = "I'm going to commit Sudoku"
        hLocY = 25
        util.placeTextOnBackground(bg, hSize, hString, textColor, midX, hLocY)

        # footer text
        fSize = 24
        #
        fStrA = "Click or use the arrow keys to change the active tile"
        fYA = 25+504+50
        util.placeTextOnBackground(bg, fSize, fStrA, textColor, midX, fYA)
        fStrB = "Use the number keys to input a number"
        fYB = 25+504+75
        util.placeTextOnBackground(bg, fSize, fStrB, textColor, midX, fYB)
        fStrC = "Press 'K' at any point to solve the puzzle"
        fYC = 25+504+100
        util.placeTextOnBackground(bg, fSize, fStrC, textColor, midX, fYC)
        fStrD = "Press 'C' at any point to clear the current puzzle"
        fYD = 25+504+125
        util.placeTextOnBackground(bg, fSize, fStrD, textColor, midX, fYD)
        fStrE = "Press 'G' at any point to generate a new puzzle"
        fYE = 25+504+150
        util.placeTextOnBackground(bg, fSize, fStrE, textColor, midX, fYE)



    # display the background
    screen.blit(background, (0, 0))
    pg.display.update()

    # prepare game objects
    clock = pg.time.Clock()
    aRect = Board()
    allsprites = pg.sprite.RenderPlain((aRect))

    # prep variables for key handlers
    arrowKeys = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]
    numberGuesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 69, 0, 0]
    numberGuesses2 = [pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4,
                        pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_r,
                        pg.K_DELETE, pg.K_BACKSPACE]


    # ===== MAIN LOOP ===== #
    running = True
    while running:
        # 60 ticks per second
        clock.tick(60)

        # handle input events
        for event in pg.event.get():

            # handlers to end game
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

            # handler to click to make a tile active
            elif (event.type == pg.MOUSEBUTTONDOWN and event.button == 1):
                pos = pg.mouse.get_pos()
                # integer division to determine which row, col
                rowClick = int( ( (pos[1] - 50) / 56) )
                colClick = int( (pos[0] / 56) )
                if (rowClick < 9 and colClick < 9):
                    tile = aRect.arrayTiles[rowClick][colClick]
                    aRect.setCurrentActive(tile)

            # number keys for shifting active handler
            elif (event.type == pg.KEYDOWN and arrowKeys.count(event.key) > 0):
                # if no active, set (0, 0) as active
                if (aRect.currentActive == None):
                    aRect.setCurrentActive(aRect.arrayTiles[0][0])
                # ugly ass ifs to check which key it is, check one thing, then change
                else:
                    tempRow = aRect.currentActive.row
                    tempCol = aRect.currentActive.col
                    if (event.key == pg.K_UP and tempRow > 0):
                        tile = aRect.arrayTiles[tempRow - 1][tempCol]
                    elif (event.key == pg.K_DOWN and tempRow < 8):
                        tile = aRect.arrayTiles[tempRow + 1][tempCol]
                    elif (event.key == pg.K_LEFT and tempCol > 0):
                        tile = aRect.arrayTiles[tempRow][tempCol - 1]
                    elif (event.key == pg.K_RIGHT and tempCol < 8):
                        tile = aRect.arrayTiles[tempRow][tempCol + 1]
                    aRect.setCurrentActive(tile)

            # number input handler
            elif (event.type == pg.KEYDOWN and numberGuesses2.count(event.key) > 0):
                if (aRect.currentActive == None):
                    break
                index = numberGuesses2.index(event.key)
                num = numberGuesses[index]
                aRect.setCurrentActiveNumber(num)

            # guess mode handler

            # generate a puzzle handler
            elif (event.type == pg.KEYDOWN and event.key == pg.K_g):
                aRect.generatePuzzle()

            # wipe board handler
            elif (event.type == pg.KEYDOWN and event.key == pg.K_c):
                aRect.wipeBoard()

            # solve board handler
            elif (event.type == pg.KEYDOWN and event.key == pg.K_k):
                aRect.solveBoard()


        # draw everything
        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.update()

    # if running != true, quit the game
    pg.quit()

# game over man, game over


# this calls the main function when this script is executed
if __name__ == "__main__":
    main()
