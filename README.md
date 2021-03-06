# OthelloGame
 
**Welcome to the OthelloGame README**

*v1.1*
*Changelog*
* *Added tournament mode with support for single elimination tournament*
* *Added command line arg support for booting with initial command*

## Running:

**Run OthelloGame.py**

## Main File Structure

* **OthelloGame**
    * contains main user interface and connects to all following modules
* othello
    * defines othello game class
    * contains main game engine
* choosers
    * handles all computer chooser algorithms
* playTest
    * testing ground for computer chooser algorithms

## Othello the Game

Othello is an abstract strategy board game played on an 8x8 square board. Two players play against each other one as Black one as White. The game begins with two of each colored tile in the center of the board. Players take turns placing tiles in a location on the board that will 'trap' their opponents tiles on 2 opposite sides, causing the opponents 'trapped' tiles to 'flip' to the color of the player who trapped them. Gameplay continues until no more moves can be played, and the winner is the player with the most tiles on the board. For a more detailed description of the game see [the wikipedia article](https://en.wikipedia.org/wiki/Reversi).

## Command Line Arguments

The program can be run with the following command line args for added functionality

* **default**
    * for users who only with to play a game of othello
    * boots directly into human vs. corner chooser game configuration
* debug
    * activates debug mode, providing debugging readouts for game methods
* log
    * provides a turn by turn log file with basic debugging information
    * _note_: _log will only run for first game_
* basic-render
    * disables clear() function, which may not work on Unix machines
    * default run configuration will try clear() and notify the user if the function will not work on their machine
* mode \[*mode*\]
    * boot directly into mode indicated after 'mode'

## OthelloGame Program Structure:

* initializes program and checks to make sure othello and chooser modules can be run

### Functions

* GA wizard
    * collects input for configuring an instance of the genetic algorithm
    * runs genetic algorithm program
    * _note_: _genetic algorithm is not supported in this version_ **_*do not attempt to run_**

### User Interface

* displays available commands and runs different functions/modules based on command
    * 1: Run game with Human v. Corner Chooser configuration
    * 2: Run game with Corner Chooser v. Human configuration
    * 3: Run game with Human v. Human configuration
    * 4: Run game with Corner Chooser v. Random Chooser configuration
    * h: Runs how-to-play sequence
    * q: Quits program
    * a: Displays advaced options:
        * 5: Run PlayTest with given choosers
        * 6: Run Tournament
        * 7: Run genetic algorithm **_*not yet supported_**

## Othello Program Structure:

### Utilities
* contains global variables for modes controlled by command line args
* processes command line args

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

### Main

* contains the main user interface for playing a game
    * takes in 2 players and a game mode
        * 'quiet' game mode skips printing out game and telling user when a chooser is making a move
    * validates players by comparing to choosers list
    * sets up game
    * loops through gameplay until neither player can make a move
        * if human player, diplays valid moves and prompts user for move
        * if chooser, plays move based on output of indicated chooser algorithm
    * at the end of the game, winner is calculated and diplayed
    * function returns scores of each player

## Choosers Program

### Choosers

* random move
    * original chooser function
    * selects random move
* first move
    * selects first move in valid moves list
* corner
    * selects move closest to a corner

## PlayTest Program

* Run Test
    * takes in 2 choosers and number of games to play
    * plays that number of games in quiet mode to run as fast as possible
    * displays results and saves them to a log file
* Single Elimination Tournament
    * takes in list of players
    * recursively executes a single elimination tournament bracket for players
        * each 'game' in tournament is a run test of 1000 games
        * *note that if there is a tie, the second player is declared winner*
    * returns winner of tournament

*Code and README by Cooper Hancock*
*3/5/2021*