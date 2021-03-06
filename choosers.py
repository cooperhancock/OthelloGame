# OthelloGame Chooser Algorithms
# Cooper Hancock
# 2021

import random
import math

# list of active choosers
chooser_list = ['corner','random','first','advanced1','advanced2','ga','human']

# GA chromosome
GAchromosome = player = {'B': [[4, 7], [1, 0], [3, 1], [7, 3], [0, 6], [1, 4], [2, 3], [6, 6], [7, 4], [0, 5], [3, 7], [2, 2], [7, 5], [4, 5], [1, 6], [4, 1], [6, 4], [2, 4], [3, 4], [1, 3], [5, 2], [2, 0], [4, 0], [0, 3], [7, 7], [0, 4], [6, 3], [3, 3], [6, 0], [5, 5], [1, 7], [2, 5], [2, 7], [6, 5], [2, 6], [6, 7], [2, 1], [4, 4], [7, 0], [7, 1], [7, 6], [3, 0], [5, 3], [4, 3], [5, 1], [5, 0], [0, 1], [1, 5], [5, 6], [4, 2], [1, 2], [0, 2], [0, 7], [7, 2], [4, 6], [3, 2], [6, 2], [1, 1], [5, 4], [0, 0], [3, 5], [3, 6], [6, 1], [5, 7]], 'W': [[7, 0], [1, 5], [1, 6], [1, 1], [2, 2], [0, 0], [1, 4], [2, 0], [6, 2], [0, 3], [3, 2], [7, 2], [2, 4], [0, 7], [5, 0], [2, 5], [2, 7], [3, 6], [4, 6], [6, 3], [4, 5], [7, 6], [3, 5], [5, 5], [7, 1], [5, 3], [5, 1], [1, 3], [0, 5], [5, 2], [2, 1], [7, 4], [7, 7], [2, 6], [5, 4], [1, 0], [7, 5], [6, 5], [5, 7], [1, 7], [4, 0], [4, 2], [0, 6], [0, 4], [3, 1], [4, 4], [6, 4], [1, 2], [4, 3], [6, 0], [4, 1], [6, 6], [6, 7], [3, 3], [7, 3], [3, 0], [3, 7], [5, 6], [0, 2], [2, 3], [3, 4], [6, 1], [4, 7], [0, 1]]}


# distance formula utility function
def distance(coord1, coord2):
    return math.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)

# all choosers return a coordinate
# coordinate must be a valid move

# random move
def computer_chooser(valid_moves): 
    return valid_moves[random.randint(0,len(valid_moves)-1)]

# first available move
def first_move(valid_moves):
    return valid_moves[0]

# chooser from GA
def advanced_chooser(current_player, valid_moves, ga_player):
    for i in ga_player.chromosome[current_player]:
        if i in valid_moves:
            return i

# closest to corner 
def corner_chooser(valid_moves):
    closest = valid_moves[0]
    shortestDistance = distance([0,0],valid_moves[0])
    for i in valid_moves:
        dist = distance([0,0],i)
        if dist < shortestDistance:
            closest = i
            shortestDistance = dist
        dist = distance([0,7],i)
        if dist < shortestDistance:
            closest = i
            shortestDistance = dist
        dist = distance([7,0],i)
        if dist < shortestDistance:
            closest = i
            shortestDistance = dist
        dist = distance([7,7],i)
        if dist < shortestDistance:
            closest = i
            shortestDistance = dist
    return closest

if __name__ == "__main__":
    moves = [[3,3],[6,1]]
    print(corner_chooser(moves))