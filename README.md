# OthelloGame
 
**Welcome to the OthelloGame README**

## Running:

**Run othello_driver.py**

### The program can be run with the following command line args:

* debug
    * activates debug mode, providing debugging readouts for game methods
* log
    * provides a turn by turn log file with basic debugging information
* basic-render
    * disables clear() function, which may not work on Unix machines
    * default run configuration will try clear() and notify the user if the function will not work on their machine

None of these args should need to be run, but are mostly just left over from early development stages

## Main Othello Program Structure:

### Utilities
* contains global variables for modes controlled by command line args
* processes command line args
* contains data from genetic algorithm that is used to make computer moves

### Othello Class
* init 
    * initializes instance of Othello with starting player and board with starting configuration
* str 
    * defines toString for object
    * has kind of weird spacing to allow for 2 digit valid move numbers
* move
    * accepts a list of valid moves, a list of flip lists, and a move index
    * places new tile according to valid move list at move index
    * iterates through flip lists to find lists that correspond to the chosen move 
        * flips tile at each coordinate in each needed flip list
* valid_moves
    * iterates through each space on the board
    * for each tile of the current player, 'looks' in each direction to see if there is a valid move in that direction
        * if it 'finds' a valid move, it records it and the tiles it traversed to get to the valid move
    * returns valid moves (list of coordinates), and a corresponding flip list (list of lists of coordinates to flip)
    * each valid move will have a list of coordinates to flip in the flip list at the same index
* computer_chooser
    * makes a random move
* advanced_chooser
    * chooses the first valid move in its list of moves
    * currently optimized for playing as White
* render
    * momentarily edits the board to display valid moves to the player
    
### Non-Class Functions
* clear
    * clears the terminal
    * also has the ability to clear single lines in the terminal
* how_to
    * runs through an introduction to the game so the player knows how to play

### Debug
* contains a function for running various debugging features

### Main Games

#### Main

* contains the main user interface for playing the default game
    * sets up game
    * in a while loop runs human player move B, then computer move W
    * once neither can move, calculates winner

## Othello Driver Program


