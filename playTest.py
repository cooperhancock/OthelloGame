# OthelloGame Play Tester
# Cooper Hancock
# 2021

import othello
import time

filename = 'playTestResults.txt'

def log(string, mode=False):
    str(string)
    with open(filename, 'a') as f:
        f.write(string + '\n')
    print(string)

def run_test_GA(player1, player2, games=1000, mode='default'):
    log('\n' + str(time.asctime(time.localtime(time.time())))) # define section of log files for instance of program
    log(str(player1) + '\n' + str(player2)) # log players

    player1score = 0
    player2score = 0

    for i in range(games):
        p1,p2 = othello.main(player1, player2, 'quiet')
        if p1>p2:
            print(str(i) + ': player 1 wins')
            player1score += 1
        elif p2>p1:
            print(str(i) + ': player 2 wins')
            player2score += 1
        else:
            log('tie')
    log('player 1: ' + str(player1score) + ' player 2: ' + str(player2score))
