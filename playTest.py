import othello
import time


games = 1000
filename = 'playTestResults.txt'

results = []

def log(string, mode=False):
    str(string)
    with open(filename, 'a') as f:
        f.write(string + '\n')
    print(string)


log('\n' + str(time.asctime(time.localtime(time.time())))) # define section of log files for instance of program
log(str(othello.player)) # log player

for i in range(games):
    print('game ' + str(i))
    game = othello.Othello()
    canMove = 2
    while canMove > 0:
        # player's move
        game.current_player = 'B'
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.advanced_chooser(moves))
            game.move(moves, flips, move)
        else:
            canMove -= 1
        # computer's (random) move
        game.current_player = 'W'
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.computer_chooser(moves))
            game.move(moves, flips, move)
        else:
            canMove -= 1
        
    white = 0
    black = 0
    for list in game.board: 
        white += list.count('W')
        black += list.count('B')
    if black>white:
        print('won')
        results.append(True)
    else:
        print('lost')
        results.append(False)

log('player playing B')
log(str(results.count(True)))

results = []

for i in range(games):
    print('game ' + str(i))
    game = othello.Othello()
    canMove = 2
    while canMove > 0:
        # computer's (random) move
        game.current_player = 'B'
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.computer_chooser(moves))
            game.move(moves, flips, move)
        else:
            canMove -= 1
        # player's move
        game.current_player = 'W'
        moves, flips = game.valid_moves()
        if len(moves) != 0:
            move = moves.index(game.advanced_chooser(moves))
            game.move(moves, flips, move)
        else:
            canMove -= 1
        
    white = 0
    black = 0
    for list in game.board: 
        white += list.count('W')
        black += list.count('B')
    if black>white:
        print('won')
        results.append(True)
    else:
        print('lost')
        results.append(False)

log('player playing W')
log(str(results.count(True)) + '\n')