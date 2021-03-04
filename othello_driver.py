# OthelloGame Driver Program
# Cooper Hancock
# 2021

import time

# Attempt to start game
try:
    import othello
except:
    input('Fatal Error: othello.py not found. Press Enter to exit.')
othello.init()

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
    print('Choose a game to play: [1] Human vs. Computer [2] Computer vs. Human [3] Human vs. Human')
    print('[q] to exit [h] how to play ... [a] for advanced options')
    mode = input()
    if mode == 'q':
        exit()
    elif mode == 'h':
        othello.how_to()
    elif mode == '1':
        b,w = othello.main() # runs othello H v. C
    elif mode == '2':
        b,w = othello.mainTwo() # runs othello C v. H
    elif mode == '3':
        b,w = othello.mainThree() # runs othello H v. H
    elif mode == 'a':
        print('Advanced options:') 
        print('[4] Play Tester (runs players configured in playTest.py file)')
        print('[5] Run Genetic Algorithm')
    elif mode == '4':
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
        othermode = input('Enter mode ')
        playTest.run_test_GA(games=games//2, mode=othermode)
        print('Summary:')
        with open(playTest.filename) as f:
            lines = f.readlines()
            for i in range(len(lines)-10, len(lines)):
                print(lines[i])
        input('Press Enter to exit')
    elif mode == '5':
        try:
            import othelloGA
        except:
            print('Fatal Error: othelloGA.py not found. Exiting...')
            time.sleep(4)
            continue
        GA_wizard()
    else:
        print('invalid command')

