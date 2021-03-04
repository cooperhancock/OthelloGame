import othello
import time

filename = 'playTestResults.txt'

# config
games = 1000
player1 = [[5, 5], [7, 7], [4, 5], [7, 0], [2, 2], [2, 5], [7, 6], [1, 0], [0, 0], [1, 1], [2, 7], [6, 0], [0, 2], [6, 6], [3, 3], [1, 2], [5, 0], [0, 4], [4, 0], [6, 7], [5, 6], [6, 5], [0, 1], [0, 7], [5, 4], [4, 4], [2, 0], [0, 3], [6, 3], [1, 7], [7, 5], [7, 1], [3, 0], [3, 1], [5, 7], [3, 5], [7, 3], [7, 2], [4, 7], [4, 6], [0, 6], [1, 3], [0, 5], [7, 4], [4, 2], [1, 6], [3, 7], [2, 6], [6, 1], [3, 4], [5, 3], [4, 1], [5, 1], [6, 4], [4, 3], [1, 4], [1, 5], [2, 4], [5, 2], [3, 2], [2, 3], [3, 6], [6, 2], [2, 1]]
player2 = []

def log(string, mode=False):
    str(string)
    with open(filename, 'a') as f:
        f.write(string + '\n')
    print(string)

def advanced_chooser(player, valid_moves):
    for i in player:
        if i in valid_moves:
            return i

def run_test_GA(player1=player1, player2=player2, games=games, mode='default'):
    results = []
    log('\n' + str(time.asctime(time.localtime(time.time())))) # define section of log files for instance of program
    log(str(player1) + '\n' + str(player2)) # log players

    for i in range(games):
        print('game ' + str(i))
        game = othello.Othello()
        canMove = 2
        while canMove > 0:
            # player's move
            game.current_player = 'B'
            moves, flips = game.valid_moves()
            if len(moves) != 0:
                if player1 == []:
                    move = moves.index(game.computer_chooser(moves))
                else:
                    move = moves.index(advanced_chooser(player1,moves))
                game.move(moves, flips, move)
            else:
                canMove -= 1
            # computer's (random) move
            game.current_player = 'W'
            moves, flips = game.valid_moves()
            if len(moves) != 0:
                if player2 == []:
                    move = moves.index(game.computer_chooser(moves))
                elif mode == 'first':
                    move = moves.index(game.first_move(moves))
                else:
                    move = moves.index(advanced_chooser(player2,moves))
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

    log('player playing B (player 1)')
    log(str(results.count(True)))
    log('player playing W (player 2)')
    log(str(results.count(False)))

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
                if player2 == []:
                    move = moves.index(game.computer_chooser(moves))
                elif mode == 'first':
                    move = moves.index(game.first_move(moves))
                else:
                    move = moves.index(advanced_chooser(player2,moves))
                game.move(moves, flips, move)
            else:
                canMove -= 1
            # player's move
            game.current_player = 'W'
            moves, flips = game.valid_moves()
            if len(moves) != 0:
                if player1 == []:
                    move = moves.index(game.computer_chooser(moves))
                else:
                    move = moves.index(advanced_chooser(player1,moves))
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

    log('player playing B (player 2)')
    log(str(results.count(True)))
    log('player playing W (player 1)')
    log(str(results.count(False)))