# OthelloGame Driver Program
# Cooper Hancock
# 2021

import time
import sys

doClear = True # toggles console clear commands (only tested on windows cmd)
direct = False # toggles direct boot into mode

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

if 'mode' in sys.argv:
    direct = True

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
    if direct and len(sys.argv) > sys.argv.index('mode')+1: # support for direct boot into command
            mode = sys.argv[sys.argv.index('mode')+1]
    else:
        print('Choose a game to play: [1] Human vs. Computer [2] Computer vs. Human [3] Human vs. Human [4] Computer vs. Computer')
        print('[q] to exit [h] how to play ... [a] for advanced options')
        mode = input()
    # quit
    if mode == 'q':
        exit()
    # help
    elif mode == 'h':
        othello.how_to()
    # game mode 1
    elif mode == '1':
        b,w = othello.main() # runs othello H v. C
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    # game mode 2
    elif mode == '2':
        b,w = othello.main(computer, human) # runs othello C v. H
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    # game mode 3
    elif mode == '3':
        b,w = othello.main(human, human) # runs othello H v. H
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    # game mode 4
    elif mode == '4':
        input('Press Enter to see Corner Chooser play Random Chooser')
        b,w = othello.main('corner', 'random') # runs othello H v. H
        print('Black:',b,'White:',w)
        time.sleep(2)
        input('Press Enter to return to home page')
        othello.clear(doClear)
    # list advanced commands
    elif mode == 'a':
        othello.clear(doClear)
        print('Advanced options:') 
        print('[5] Play Tester (runs players configured in playTest.py file)')
        print('[6] Run Tournament')
    # play test
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
        playTest.run_test(p1,p2,games)
        input('Press Enter to exit')
        othello.clear(doClear)
    # tournament
    elif mode == '6':
        try:
            import playTest
        except:
            print('Fatal Error: playTest.py not found. Exiting...')
            time.sleep(4)
            continue
        othello.clear(doClear)
        print('Welcome to the Tournament Wizard')
        players = []
        p = ''
        print('available choosers:', othello.choosers.chooser_list)
        while p!='done':
            p = input('Enter chooser to add to tournament: ')
            if not p in othello.choosers.chooser_list:
                if p == 'done':
                    print('Chooser list finalized')
                    break
                else:
                    print('Error: chooser unavailable')
                    p = ''
                    continue
            players.append(p)
        print('Choosers playing in tournament:',players)
        input('Press Enter to run tournament')
        playTest.log('\n' + 'New Tournament\n' + str(time.asctime(time.localtime(time.time()))))
        winner = playTest.single_elim_tournament(players)
        print('Winner of tournament is:', winner)
        input('Press Enter to exit')
        othello.clear(doClear)
    # genetic algorithm
    elif mode == '7':
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
    direct = False # turn of direct boot mode
