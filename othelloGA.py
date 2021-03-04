import othello
import random
import time

healthy_chromosome = [] # for mutations and chromosome health verification
for i in range(8):
    for j in range(8):
        healthy_chromosome.append([i,j])

main_log_file='mainGA.txt'
debug_log_file='debugGA.txt'

################
# PLAYER CLASS #
################

class Player:

    # creates player with fitness and chromosome, sets up chromosome as 64 item list
    def __init__(self):
        self.fitness = 0
        self.chromosome = []
        for i in range(64):
            self.chromosome.append(0)
    
    # crosses player with passed other player
    def crossover(self, other, mutation_rate):
        child = Player()
        # inherit genes from parent 1
        for i in range(len(child.chromosome)): 
            log(str(child.chromosome[i]) + str(self.chromosome[i]), True)
            rand = random.randint(0,100)/100
            #print(rand)
            if rand > 0.5: # chance of inheriting from parent 1
                child.chromosome[i] = self.chromosome[i]
                log(str(child.chromosome),True)
            elif rand < mutation_rate:
                mutation = child.chromosome[0]
                while mutation in child.chromosome:
                    mutation = self.chromosome[random.randint(0,63)]
                child.chromosome[i] = mutation
                log(str(child.chromosome),True)
        # inherit genes from parent 2
        for i in range(len(other.chromosome)):
            rand = random.randint(0,100)/100
            if not 0 in child.chromosome: # to catch if child chromosome is full, but doesn't have all possible genes bc of a mutation
                break
            if not other.chromosome[i] in child.chromosome:
                if rand < mutation_rate:
                    mutation = child.chromosome[0]
                    while mutation in child.chromosome:
                        mutation = other.chromosome[random.randint(0,63)]
                    child.chromosome[child.chromosome.index(0)] = mutation
                    log(str(child.chromosome),True)
                else:
                    child.chromosome[child.chromosome.index(0)] = other.chromosome[i]
                    log(str(child.chromosome),True)
        # check that child has valid chromosome
        healthy = True
        for i in range(64):
            if child.chromosome.count(healthy_chromosome[i]) != 1:
                healthy = False
        if not healthy:
            return self.crossover(other, mutation_rate) # if child is not healthy, retry crossover
        else:
            return child

    # player plays n games of othello with a computer that chooses random moves
    # each game it wins increases its fitness by 1, up to a possible n
    def calc_fitness(self, games):
        self.fitness = 0
        for i in range(games//2): # half with player playing first
            log('game ' + str(i), True)
            game = othello.Othello()
            log(str(game), True)
            canMove = 2
            turn = 1
            while canMove > 0:
                # player's move
                game.current_player = 'B'
                moves, flips = game.valid_moves()
                log(str(moves), True)
                if len(moves) != 0:
                    try:
                        move = moves.index(self.advanced_chooser(moves))
                    except:
                        self.fitness = 0
                        log('!lethal chromosome! ' + str(self))
                        return
                    game.move(moves, flips, move)
                else:
                    canMove -= 1
                log(str(turn) + game.current_player + '\n' + str(game), True)
                # computer's (random) move
                game.current_player = 'W'
                moves, flips = game.valid_moves()
                log(str(moves), True)
                if len(moves) != 0:
                    move = moves.index(game.computer_chooser(moves))
                    game.move(moves, flips, move)
                else:
                    canMove -= 1
                log(str(turn) + game.current_player + '\n' + str(game), True)
                turn += 1
            white = 0
            black = 0
            for list in game.board: 
                white += list.count('W')
                black += list.count('B')
            if black>white:
                self.fitness += 1
                log('!won!', True)
        for i in range(games): # for now -- only run when player is W bc that's how it will be in the game
            log('game ' + str(i), True)
            game = othello.Othello()
            log(str(game), True)
            canMove = 2
            turn = 1
            while canMove > 0:
                # computer's (random) move
                game.current_player = 'B'
                moves, flips = game.valid_moves()
                log(str(moves), True)
                if len(moves) != 0:
                    move = moves.index(game.computer_chooser(moves))
                    game.move(moves, flips, move)
                else:
                    canMove -= 1
                log(str(turn) + game.current_player + '\n' + str(game), True)
                turn += 1
                # player's move
                game.current_player = 'W'
                moves, flips = game.valid_moves()
                log(str(moves), True)
                if len(moves) != 0:
                    try:
                        move = moves.index(self.advanced_chooser(moves))
                    except:
                        self.fitness = 0
                        log('!lethal chromosome! ' + str(self))
                        return
                    game.move(moves, flips, move)
                else:
                    canMove -= 1
                log(str(turn) + game.current_player + '\n' + str(game), True)
            white = 0
            black = 0
            for list in game.board: 
                white += list.count('W')
                black += list.count('B')
            if black>white:
                self.fitness += 1
                log('!won!', True)

    def advanced_chooser(self, valid_moves):
        for i in self.chromosome:
            if i in valid_moves:
                return i

    # less than operator
    def __lt__(self, other):
        return self.fitness < other.fitness

    def __str__(self):
        return str(self.chromosome)

#######################
# NON-CLASS FUNCTIONS #
#######################

# create chromosome of all possible coordinates on an 8x8 grid
def create_chromosome():
    chromosome = []
    for i in range(8):
        for j in range(8):
            chromosome.append([i,j])
    return chromosome

# create population of given size of given players with randomized chromosomes
def random_population(size):
    population = []
    for i in range(size):
        new_player = Player()
        new_player.chromosome = create_chromosome()
        random.shuffle(new_player.chromosome)
        population.append(new_player)
    return population

# logs data to log files (goes to debug file as well if True)
def log(string, mode=False):
    global main_log_file,debug_log_file
    str(string)
    if mode:
        with open(debug_log_file, 'a') as d:
            d.write(string + '\n')
    if not mode:
        with open(main_log_file, 'a') as m:
            m.write(string + '\n')
        print(string)

def runGA(games=100, mutation_rate=0.05, generations=100, population_size=100, survivors=10, main_log='mainGA.txt', debug_log='debugGA.txt', debug_mode=False, white=True, black=True):

    # GLOBAL MODIFIERS #

    global main_log_file
    global debug_log_file
    main_log_file = main_log
    debug_log_file = debug_log

    #games = 10 # number of games played to calculate fitness
    #mutation_rate = 0.05 # chance that a gene will mutate
    #generations = 1000 # number of generations to run
    #population_size = 50 # population size of each generation
    #survivors = 10 # number of players to directly move on to next generation

    ########
    # MAIN #
    ########

    log('\n' + str(time.asctime(time.localtime(time.time())))) # define section of log files for instance of program
    population = random_population(population_size) # create population of players

    # calculate run time
    timeStart = time.time()
    print('calculating run time...')
    population[0].calc_fitness(games)
    log('estimated time to complete: ' + str((time.time()-timeStart)*population_size*generations/60) + ' minutes') 
    x = input('Press Enter to continue or q to quit')
    if x == 'q':
        return

    # main simulation of each generation
    for gen in range(generations):

        # calculate fitness of population
        timeStart = time.time()
        log('CALCULATING FITNESS...')
        for i in range(population_size):
            log('calulating fitness of ' + str(i), True)
            print(i)
            population[i].calc_fitness(games)
        print()
        log(str(gen) + ' calc_fitness time = ' + str(time.time()-timeStart))

        # sorts population by fitness
        population.sort(key=lambda x: x.fitness, reverse=True)
        highestFitness = population[0].fitness
        s = ''
        for i in range(population_size):
            s += str(population[i].fitness)
            s += ' '
        log(s)
        log('highest fitness = ' + str(highestFitness))
        log('player = ' + str(population[0]))

        # create new population
        newPopulation = []

        # move best players to next generation
        for i in range(survivors):
            log('adding ' + str(i), True)
            newPopulation.append(population[i])

        # cross best 50% of population
        log('CROSSING...')
        for i in range(population_size-survivors):
            log('crossing ' + str(i), True)
            rand = random.randint(0,population_size/2)
            parent1 = population[rand]
            rand = random.randint(0,population_size/2)
            parent2 = population[rand]
            child = parent1.crossover(parent2, mutation_rate)
            newPopulation.append(child)
        
        # set population to new population
        population = newPopulation

    log('end\n')

if __name__ == "__main__":
    runGA()