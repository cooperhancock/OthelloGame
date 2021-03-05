# OthelloGame Chooser Algorithms
# Cooper Hancock
# 2021

import random
import math

# list of active choosers
chooser_list = ['corner','random','first','advanced','human']

# advanced chooser Genetic Algorithm chromosome
player = []

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
def advanced_chooser(current_player, valid_moves):
    global player
    for i in player[current_player]:
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