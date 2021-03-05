# OthelloGame Driver Program
# Cooper Hancock
# 2021

import time
import sys

doClear = True # toggles console clear commands (only tested on windows cmd)

# Attempt to start game
try:
    import othello
except:
    input('Fatal Error: othello.py not found or could not run. Press Enter to exit.')
    exit()
x = othello.init()
# handle if cannot do clear function
if x==1: sys.argv.append('basic-render')
if 'basic-render' in sys.argv:
    doClear = False

# computer chooser algorithm to use for main games
computer = 'corner'
human = 'human'

# boot directly into game mode 1 with 'default' command line arg
if 'default' in sys.argv:
    othello.main()
    x = input('[q]uit or Enter main program ')
    if x=='q': exit()

# GA init wizard
def GA_wizard():
    print('Warning! Input paramater values carefully')
    print('Different values will lead to astronomically different run times')
    print('Read OthelloGame README for more information')
    print('games, mutation rate, generations, pop size, survivors')
    try:
        games = int(input())
        rate = float(input())
        gens = int(input())
        size = int(input())
        survivors = int(input())
    except:
        print('Input error. Exiting...')
        time.sleep(4)
        return
    try:
        othelloGA.runGA(games, rate, gens, size, survivors)
    except:
        print('Fatal Error: Could not execute genetic algorithm')
        print('Exiting...')
        time.sleep(4)
        return

# user interface
while True:
    print('Choose a game to play: [1] Human vs. Computer [2] Computer vs. Human [3] Human vs. Human [4] Computer vs. Computer')
    print('[q] to exit [h] how to play ... [a] for advanced options')
    mode = input()
    if mode == 'q':
        exit()
    elif mode == 'h':
        othello.how_to()
    elif mode == '1':
        b,w = othello.main() # runs othello H v. C
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    elif mode == '2':
        b,w = othello.main(computer, human) # runs othello C v. H
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    elif mode == '3':
        b,w = othello.main(human, human) # runs othello H v. H
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    elif mode == '4':
        input('Press Enter to see Corner Chooser play Random Chooser')
        b,w = othello.main('corner', 'random') # runs othello H v. H
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    elif mode == 'a':
        print('Advanced options:') 
        print('[5] Play Tester (runs players configured in playTest.py file)')
        print('[6] Run Genetic Algorithm')
    elif mode == '5':
        try:
            import playTest
        except:
            print('Fatal Error: playTest.py not found. Exiting...')
            time.sleep(4)
            continue
        games = input('Enter number of games to play ')
        try:
            games = int(games)
        except:
            print('Input error. Exiting...')
            time.sleep(4)
            continue
        p1 = input('Enter player 1 chooser: ')
        p2 = input('Enter player 2 chooser: ')
        if not ((p1 in othello.choosers.chooser_list) and (p2 in othello.choosers.chooser_list)):
            print('Input error. Exiting...')
            time.sleep(4)
            continue
        playTest.run_test_GA(p1,p2,games)
        input('Press Enter to exit')
        othello.clear(doClear)
    elif mode == '6':
        try:
            import othelloGA
        except:
            print('Fatal Error: othelloGA.py not found. Exiting...')
            time.sleep(4)
            continue
        GA_wizard()
        othello.clear(doClear)
    else:
        print('invalid command')
    if othello.log: 
        print('Closing log')
        othello.log = False
