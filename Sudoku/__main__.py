# Riley Grant
# May 11th, 2020
# Sudoku player / solver
# =========================

# import relevant modules from project
from SudokuFiles.Game import*


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


#class Main(object):
#
#    def __init__():
#        pass
#
#    @static
#    def main(self):
#        main()

aGame = Game()

if __name__ == "__main__":
    #main()
    aGame.runGame()
