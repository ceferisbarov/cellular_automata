import matplotlib.pyplot as plt
import math
import copy
import random
from cell import Cell

def get_lattice_life(lattice):
    lattice_life = [[] for n in range(len(lattice))]
    for x in range(len(lattice)):
        for y in lattice[x]:
            lattice_life[x].append(y.get_life())
                
    return lattice_life
                
def set_lattice(length, choice):
    '''
    Given the choice of lattice pattern, sets a 2 dimensional, finite lattice,
    digits of which store a cell each
    '''
#TODO: replace this with a function that sets n dimensional, infinite lattice.
  
    lattice = []
    for n in range(length):
        lattice.append([])
    
    if choice == 1:
        for x in range(length):
            for y in range(length):
                lattice[x] += [Cell(1,x,y) if x == math.floor(length/2)\
                                               else Cell(0,x,y)]

    elif choice == 2:
        for x in range(length):
            for y in range(length):
                lattice[x] += [Cell(1,x,y) if ((y == math.floor(length/2)\
                                                or y == math.floor(length/2)-1))\
                                               and (x == math.floor(length/2)\
                                                or x == math.floor(length/2)-1)\
                                           else Cell(0,x,y)]

    elif choice == 3:
        for x in range(length):
            for y in range(length):
                lattice[x] += [Cell(1,x,y) if (x == math.floor(length/2)\
                                               and (y == math.floor(length/2)+1\
                                                or y == math.floor(length/2)\
                                                or y == math.floor(length/2)-1))\
                                           else Cell(0,x,y)]
    elif choice == 4:
        for x in range(length):
            for y in range(length):
                lattice[x] += [Cell(1,x,y) if (random.random() <= 0.5)\
                                           else Cell(0,x,y)]
    
    plt.imshow(get_lattice_life(lattice))
    plt.show()

    return lattice

def play(lattice, number):
    '''
    After main() receives the input and sets the lattice,
    play() takes care of the rest. Just to keep main() tiny and neat.
    '''
    
    for n in range(number): 
        lattice_copy = copy.deepcopy(lattice)
        for x in lattice:
            for y in x:
                y.evaluate(lattice_copy)
    
        plt.imshow(get_lattice_life(lattice))
        plt.show()

        
def main():
    print("Choose a pattern: ")
    print("1. Line\n2. Block\n3. Blinker\n4. Random")
    choice = int(input())
    print("Length of the nxn lattice: ")
    size = int(input())
    print("Number of evaluations: ")
    number = int(input())
    
    lattice = set_lattice(size, choice)
        
    play(lattice, number)
    
if __name__ == '__main__':
    main()
