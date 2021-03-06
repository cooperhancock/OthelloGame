# Othello Board Game
# Cooper Hancock
# 2021

import os
import time
import sys
import random
try:
    import choosers
except:
    input('Fatal Error: choosers.py not found. Press Enter to exit.')
    exit()

# coordinates [x (row), y (col)]

#############
# UTILITIES #
#############

# program settings (defaults)
debug = False # toggles debug prints
doClear = True # toggles console clear commands (only tested on windows cmd)
log = False # toggles writing log file
turn = 1 # turn tracker for log file

# command line args
if 'debug' in sys.argv:
    debug = True
if 'basic-render' in sys.argv:
    doClear = False
if 'log' in sys.argv:
    log = True
    f = open("othellologs.txt", 'w')

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
    
    # display board with valid moves
    def render(self, valid_moves):
        i = 1
        items=['W','B','*'] # items on board
        for list in valid_moves:
            if self.board[list[0]][list[1]] in items:
                self.board[list[0]][list[1]] = str(i)
            i += 1
        s = ''
        for i in range(8):
            for j in range(8):
                s += self.board[i][j] + '  '
                try:
                    if len(self.board[i][j]) == 2:
                        s = s[:-1]
                except:
                    pass
            s += '\n'
        print(s)

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
    input('Press Enter to exit')
    clear(doClear)

#########
# DEBUG #
#########

def _debug():
    print(type(1))
    print(isinstance(1, int))

    input('enter')

########
# MAIN #
########

# initialization/bootup of game
# returns 1 if need to change to basic render
def init():
    # clear() test
    try:
        clear(True)
    except:
        print('WARNING')
        print('This environment cannot run the current configuration')
        print('Changing to basic rendering mode...')
        input('Press Enter to start program')
        return 1

    if debug:
        _debug()

    # Game Initialization
    print('Welcome to Othello')


# play main game
# players can be human or any chooser
# mode param is list of modes:
# quiet to disable printing out board
def main(player1='human', player2='corner', mode='', GAplayer1=None, GAplayer2=None):

    # verify players
    if player1 not in choosers.chooser_list:
        print('Player Error: invalid player, setting to default...')
        time.sleep(2)
        player1='human'
    if player2 not in choosers.chooser_list:
        print('Player Error: invalid player, setting to default...')
        time.sleep(2)
        player2='corner'

    if player1=='advanced1':
        import othelloGA
        if not isinstance(GAplayer1, othelloGA.Player):
            input('GAplayer1 not of type Player, press Enter to exit')
            exit()
    if player1=='advanced2':
        import othelloGA
        if not isinstance(GAplayer2, othelloGA.Player):
            input('GAplayer2 not of type Player, press Enter to exit')
            exit()

    # use global config variables
    global turn, debug, log, doClear
    if log:
        f.write('Running Game config: ' + player1 +' '+ player2 +' '+ mode + '\n')

    # game setup
    game = Othello()
    canMove = 2
    move = ''
    if not mode=='quiet':
        print(game)
        print('Press Enter to Begin')
        input
        clear(doClear)

    # Main Engine

    while canMove > 0:
        canMove = 2
        if log: f.write('next loop\n')
        for i in range(2): # each turn first player1 ('B') then player2 ('W')
            players = [player1,player2]
            colors = ['B','W']
            game.current_player = colors[i]
            if log:
                f.write(str(turn) + game.current_player + ' i=' + str(i) + '\n')
            
            # print board
            if not mode=='quiet': print(game) 

            # get valid moves for this player's turn
            moves, flips = game.valid_moves()

            # execute move if there are moves to make
            if len(moves) != 0:
                # human player
                if players[i]=='human':
                    if log: f.write('human\n')
                    game.render(moves)
                    while not isinstance(move,int):
                        print('Player',str(i+1)+"'s turn! ("+colors[i]+')')
                        move = input('Enter move number: ')
                        if move == 'q':
                            print('quitting game')
                            if log:
                                f.close()
                            time.sleep(1)
                            return 0,0
                        try:
                            move = int(move)
                        except:
                            print('invalid move ', end='')
                            continue
                        if move <= 0 or move > len(moves):
                            print('invalid move ', end='')
                            move = ''
                            continue
                    move -= 1 # zero-index move
                    game.move(moves, flips, move)
                    clear(doClear)
                # computer player
                else:
                    if log: f.write('computer\n')
                    if players[i]=='random':
                        move = moves.index(choosers.computer_chooser(moves))
                    elif players[i]=='corner':
                        move = moves.index(choosers.corner_chooser(moves))
                    elif players[i]=='first':
                        move = moves.index(choosers.first_move(moves))
                    elif players[i]=='advanced1':
                        move = moves.index(choosers.advanced_chooser(game.current_player, moves, GAplayer1))
                    elif players[i]=='advanced2':
                        move = moves.index(choosers.advanced_chooser(game.current_player, moves, GAplayer2))
                    game.move(moves, flips, move)
                    if not mode=='quiet':
                        print('*computer is making a move*')
                        time.sleep(1)
                        clear(doClear)
                # log
                if log:
                    f.write('move: ' + str(move) + ' moves: ' + str(moves) + ' flips: ' + str(flips) + '\n')
            # if no moves to make
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

    if not mode=='quiet':
        print(game)
        if white>black:
            print("White wins!")
        elif black>white:
            print("Black wins!")
        else:
            print("It's a tie!")

    if log:
        f.write('black: ' + str(black) + ' white: ' + str(white))

    return black, white

