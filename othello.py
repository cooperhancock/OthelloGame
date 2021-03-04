# Cooper Hancock
# Othello Board Game

import os
import time
import sys
import random

# coordinates [x (row), y (col)]

#############
# UTILITIES #
#############

# program settings (defaults)
debug = False # toggles debug prints
howToPlay = True # toggles how-to sequence
doClear = True # toggles console clear commands (only tested on windows cmd)
log = False # toggles writing log file
turn = 1 # turn tracker for log file

# command line args
if 'debug' in sys.argv:
    debug = True
if 'expert' in sys.argv:
    howToPlay = False
if 'basic-render' in sys.argv:
    doClear = False
if 'log' in sys.argv:
    log = True
    f = open("othellologs.txt", 'w')

# player chromosome from GA
player = [[4, 0], [5, 1], [7, 4], [1, 2], [2, 1], [6, 1], [4, 1], [6, 4], [7, 5], [6, 5], [1, 1], [6, 2], [7, 3], [5, 3], [0, 3], [7, 2], [1, 5], [6, 7], [5, 0], [4, 6], [6, 6], [5, 5], [0, 2], [2, 0], [6, 3], [5, 7], [4, 4], [3, 7], [0, 5], [4, 2], [0, 6], [3, 3], [3, 2], [3, 5], [5, 2], [1, 6], [0, 4], [2, 4], [3, 0], [2, 6], [1, 4], [2, 5], [5, 4], [2, 2], [1, 3], [7, 6], [2, 7], [4, 3], [0, 1], [4, 5], [3, 1], [3, 6], [4, 7], [3, 4], [7, 0], [6, 0], [0, 7], [7, 1], [0, 0], [1, 0], [1, 7], [7, 7], [5, 6], [2, 3]]


#################
# OTHELLO CLASS #
#################

class Othello():
    def __init__(self):
        self.board = []
        self.current_player = 'B'
        for i in range(8):
            row = []
            for j in range(8):
                if (i==3 and j==3) or (i==4 and j==4):
                    row.append('W')
                elif (i==3 and j==4) or (i==4 and j==3):
                    row.append('B')
                else: 
                    row.append('*')
            self.board.append(row)

    def __str__(self):
        global log, f
        s = ''
        #for i in range(8):
        #    s += str(i) + ' '
        #s += '\n'
        for i in range(8):
            #s += str(i) + ' '
            for j in range(8):
                s += self.board[i][j] + '  '
            s += '\n'
        if log:
            f.write(s)
        return s
        
    # makes move with player 'W' or 'B' by setting new tile and flipping appropriate tiles
    # pass in coordinate to place new tile and list of tiles to flip
    def move(self, valid_moves, flip_tiles, move_index):
        # place new tile
        coord = valid_moves[move_index]
        self.board[coord[0]][coord[1]] = self.current_player

        # flip necessary tiles
        for i in range(len(flip_tiles)):
            if valid_moves[i] == coord:
                for list in flip_tiles[i]:
                    if debug:
                        print(list)
                    self.board[list[0]][list[1]] = self.current_player
        

    def valid_moves(self): 
        # iterate through player's tiles
        # check cardinal adjacencies for opposite tile
        # if opp tile found, follow in direction until blank
        # add blank tile to valid move list
        global debug # access to debug mode
        validMoves = [] # list of coordinates
        flipTiles = [] # list of lists of coordinates, each sub list corresponds to the same indexed valid move
        for i in range(8):
            for j in range(8):
                if debug:
                    print('coord',i,j)
                if self.board[i][j] == self.current_player:
                    for row_step in range(-1,2):
                        for col_step in range(-1,2):
                            if debug:
                                print('step',i+row_step,j+col_step)
                            if i+row_step < 0 or i+row_step > 7 or j+col_step < 0 or j+col_step > 7:
                                continue
                            elif self.board[i+row_step][j+col_step] == self.current_player or self.board[i+row_step][j+col_step] == '*':
                                continue
                            else:
                                toFlip = []
                                toFlip.append([i+row_step,j+col_step])
                                if debug:
                                    print('there is move by me',i,j)
                                for step in range(2,7):
                                    if i+row_step*step < 0 or i+row_step*step > 7 or j+col_step*step < 0 or j+col_step*step > 7:
                                        break
                                    elif self.board[i+row_step*step][j+col_step*step] == '*':
                                        validMoves.append([i+row_step*step,j+col_step*step])
                                        flipTiles.append(toFlip)
                                        break
                                    toFlip.append([i+row_step*step, j+col_step*step])
        return validMoves, flipTiles

    # random move
    def computer_chooser(self, valid_moves): ## TEMPORARY ##
        return valid_moves[random.randint(0,len(valid_moves)-1)] # coordinate

    # chooser from GA
    def advanced_chooser(self, valid_moves):
        global player
        for i in player:
            if i in valid_moves:
                return i
    
    # display board with valid moves
    def render(self, valid_moves):
        i = 1
        for list in valid_moves:
            self.board[list[0]][list[1]] = str(i)
            i += 1
        print(self)

        # removes numbers from board
        board_tiles = ['W','B','*']
        for i in range(8):
            for j in range(8):
                if not self.board[i][j] in board_tiles:
                    self.board[i][j] = '*'

#######################
# NON-CLASS FUNCTIONS #
#######################

# clears terminal
# ATTENTION! - if not using windows cmd, clear may not work and should be set to inactive
def clear(active, kind='clear', num=100):
    if not active: # if configured to not clear terminal
        return
    if kind == 'line':
        print('\b'*num,end='',flush=True)
    elif kind == 'clear':
        os.system('cls')

# provides a short how-to-play sequence
def how_to():
    how = Othello()
    how.current_player = 'B'
    clear(doClear)
    print('How to play:')
    print(how)
    print('This is what the starting board looks like.')
    print('You will play black (B). Your goal is to have the most tiles at the end.')
    input('Press Enter to continue..')
    clear(doClear)
    print(how)
    moves, flips = how.valid_moves()
    how.render(moves)
    print('On your turn, you will see 2 versions of the board.')
    print('The top shows just the tiles, and the bottom shows numbers where you can place a new tile.')
    move = input('Enter the number where you want to place a tile (1, 2, 3, or 4): ')
    try:
        move = int(move)
    except:
        print('Could not set',move,'as move, setting move to 1')
        move = 1
        time.sleep(2)
    if move > len(moves) or move <= 0:
        print('Could not set',move,'as move, setting move to 1')
        move = 1
        time.sleep(2)
    how.move(moves, flips, move-1)
    clear(doClear)
    print(how)
    print('Now the board looks like this.')
    print('Next the computer will make a move, and you will take turns until no more moves can be made.')
    input('Press Enter to start game')

#########
# DEBUG #
#########

def _debug():
    print(type(1))
    print(isinstance(1, int))

    input('enter to test:')
    # double computer test
    global turn, log
    game = Othello()
    canMove = 2
    move = ''
    while canMove > 0:
        # Black (player's) turn
        game.current_player = 'B'
        if log:
            f.write(str(turn) + game.current_player + '\n')
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.computer_chooser(moves))
            if log:
                f.write('move: ' + str(move) + ' moves: ' + str(moves) + ' flips: ' + str(flips) + '\n')
            game.move(moves, flips, move)
            print(game)
        else:
            canMove -= 1
        # White (computer's) turn
        game.current_player = 'W'
        if log:
            f.write(str(turn) + game.current_player + '\n')
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.advanced_chooser(moves))
            if log:
                f.write('move: ' + str(move) + ' moves: ' + str(moves) + ' flips: ' + str(flips) + '\n')
            game.move(moves, flips, move)
            print(game)
        else:
            canMove -= 1
        move = ''
        turn += 1

    # Calculate Winner
    white = 0
    black = 0
    for list in game.board: 
        white += list.count('W')
        black += list.count('B')
    print(game)
    if white>black:
        print("White wins!")
    elif black>white:
        print("Black wins!")
    else:
        print("It's a tie!")
    if log:
        f.write('white: ' + str(white) + ' black: ' + str(black))
    x = input('press enter to exit debug ')
    if x == 'q':
        f.close()
        exit()

########
# MAIN #
########

def main():

    global turn, debug, howToPlay, log, doClear

    # clear() test
    try:
        clear(True)
    except:
        print('WARNING')
        print('This environment cannot run the current configuration')
        print('Changing to basic rendering mode...')
        input('Press Enter to start program')

    if debug:
        _debug()

    # Game Initialization
    print('Welcome to Othello')
    if howToPlay:
        how_to()

    game = Othello()
    canMove = 2
    move = ''
    print(game)
    print('Press Enter to Begin')
    input
    clear(doClear)

    # Main Engine

    while canMove > 0:
        # Black (player's) turn
        game.current_player = 'B'
        if log:
            f.write(str(turn) + game.current_player + '\n')
        print(game)
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            game.render(moves)
            while not isinstance(move,int):
                move = input('Enter move number: ')
                if move == 'q':
                    print('quitting game')
                    if log:
                        f.close()
                    time.sleep(1)
                    exit()
                try:
                    move = int(move)
                except:
                    print('invalid move ', end='')
                    continue
                if move <= 0 or move > len(moves):
                    print('invalid move ', end='')
                    move = ''
                    continue
            if log:
                f.write('move: ' + str(move) + ' moves: ' + str(moves) + ' flips: ' + str(flips) + '\n')
            game.move(moves, flips, move-1)
            print(game)
        else:
            canMove -= 1

        # White (computer's) turn
        game.current_player = 'W'
        if log:
            f.write(str(turn) + game.current_player + '\n')
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.advanced_chooser(moves))
            if log:
                f.write('move: ' + str(move) + ' moves: ' + str(moves) + ' flips: ' + str(flips) + '\n')
            game.move(moves, flips, move)
            print('*computer is making a move*')
            time.sleep(1)
        else:
            canMove -= 1
        move = ''
        clear(doClear)
        turn += 1

    # Calculate Winner
    white = 0
    black = 0
    for list in game.board: 
        white += list.count('W')
        black += list.count('B')

    print(game)
    if white>black:
        print("White wins!")
    elif black>white:
        print("Black wins!")
    else:
        print("It's a tie!")

    if log:
        f.write('white: ' + str(white) + ' black: ' + str(black))
        f.close()
