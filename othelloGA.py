# OthelloGame Chooser Genetic Algorithm
# Cooper Hancock
# 2021

import othello
import random
import time

healthy_chromosome = [] # for mutations and chromosome health verification
for i in range(8):
    for j in range(8):
        healthy_chromosome.append([i,j])

main_log_file='mainGA.txt'
debug_log_file='debugGA.txt'

# Chromosome Data Structure:
# tuple of 2 lists - each list contains 64 coordinates each coordinate represented as a list [row,col]
# the first list in the tuple is for B moves, the second for W moves

################
# PLAYER CLASS #
################

class Player:

    # creates player with fitness and chromosome, sets up chromosome as 64 item list
    def __init__(self):
        self.fitness = 0
        self.chromosome = {'B':[],'W':[]}
        for key in self.chromosome:
            for i in range(64):
                self.chromosome[key].append(0)
    
    # crosses player with passed other player
    # also performs mutations
    def crossover(self, other, mutation_rate):
        child = Player()
        child.chromosome['B'] = self.chromosome['B'] # inherit black moves from one parent
        child.chromosome['W'] = self.chromosome['W'] # inherit white moves from other parent
        for key in child.chromosome:
            # iterate from both ends of the list to the middle
            # mutation_rate chance of swapping items at the current points
            for i in range(int(len(child.chromosome[key])//2)):
                rand = random.randint(0,100)/100
                if rand < mutation_rate:
                    temp = child.chromosome[key][i]
                    child.chromosome[key][i] = child.chromosome[key][len(child.chromosome[key])-1-i]
                    child.chromosome[key][len(child.chromosome[key])-1-i] = temp
        return child

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

# create population of given size of given players with tuple of 2 randomized chromosomes
def random_population(size):
    population = []
    for i in range(size):
        new_player = Player()
        for key in new_player.chromosome:
            new_chromosome = create_chromosome()
            random.shuffle(new_chromosome)
            new_player.chromosome[key] = new_chromosome
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

# player plays a game of Othello with every other player in the population
# each game it wins increases its fitness by 1, up to a possible population_size-1
# takes list of players
def calc_fitness(population,mode=''):
    n = len(population)
    progress = 0
    printed = 0
    for i in range(n-1):
        for j in range(i+1,n):
            left = int(progress/((n*n+n)//2)*100)
            if left!=printed: 
                if mode!='quiet': 
                    print(left,'of 100')
                    printed = left
            if i != j:
                if mode!='quiet': log('calulating fitness of ' + str(i) + ' and ' + str(j), True)
                b,w = othello.main('advanced1','advanced2','quiet',population[i],population[j])
                population[i].fitness += b>w
                population[j].fitness += w>b
            progress += 1

def runGA(mutation_rate=0.05, generations=100, population_size=100, survivors=10, main_log='mainGA.txt', debug_log='debugGA.txt', debug_mode=False, white=True, black=True):

    # GLOBAL MODIFIERS #

    global main_log_file
    global debug_log_file
    main_log_file = main_log
    debug_log_file = debug_log

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
    dummyPop = random_population(int(population_size//2))
    calc_fitness(dummyPop,'quiet')
    log('estimated time to complete: ' + str(((time.time()-timeStart)*4*generations/60)) + ' minutes')
    x = input('Press Enter to continue or q to quit')
    if x == 'q':
        return

    # main simulation of each generation
    for gen in range(generations):

        # calculate fitness of population
        timeStart = time.time()
        log('CALCULATING FITNESS...')
        calc_fitness(population)
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
        log('highest fitness = ' + str(highestFitness) + ' of possible ' + str((population_size*population_size+population_size)/2))
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