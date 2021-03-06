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

# run test for two players
def run_test(player1, player2, games=1000, mode='default'):
    if mode!='quiet': 
        log('\n' + str(time.asctime(time.localtime(time.time())))) # define section of log files for instance of program
        log(str(player1) + '\n' + str(player2)) # log players

    player1score = 0
    player2score = 0

    for i in range(games):
        p1,p2 = othello.main(player1, player2, 'quiet')
        if p1>p2:
            if mode!='quiet': print(str(i) + ': player 1 wins')
            player1score += 1
        elif p2>p1:
            if mode!='quiet': print(str(i) + ': player 2 wins')
            player2score += 1
        else:
            if mode!='quiet': print('tie')
    if mode!='quiet': log('player 1: ' + str(player1score) + ' player 2: ' + str(player2score))
    # return winner
    if player1score > player2score:
        return player1
    else:
        return player2

# recursively runs single elimination style bracket for list of players
# returns winner
def single_elim_tournament(playerlist):
    log('players: ' + str(playerlist))
    winnerlist = []
    if len(playerlist) == 1:
        log('end condition')
        return playerlist[0]
    else:
        if len(playerlist) % 2 == 1: # odd number of players
            winnerlist.append(run_test(playerlist[0],playerlist[1]))
            for i in range(2,len(playerlist)):
                winnerlist.append(playerlist[i])
        else: # even number of players
            for i in range(0,len(playerlist),2):
                winnerlist.append(run_test(playerlist[i],playerlist[i+1]))
        return single_elim_tournament(winnerlist)

# every player plays every other player for passed number of games
# returns tuple: list_of_scores(same order as players), winner
def round_robin(playerlist, games, mode='default'):
    pass
