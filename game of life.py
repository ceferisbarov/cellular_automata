import math
import copy
from Cell import cell

                
def set_lattice(length, choice):
    '''
    Current: sets a 2 dimensional, finite, digital lattice,
    digits of which store a cell each
    
    Final: sets an n dimensional, infinite coordinate system,
    digits of which store a cell each
    '''
    lattice = []
    for n in range(length):
        lattice.append([])
    
    if choice == 1:
        for x in range(length):
            for y in range(length):
                lattice[x] += [cell(1,x,y) if x == math.floor(length/2)\
                                               else cell(0,x,y)]

    elif choice == 2:
        for x in range(length):
            for y in range(length):
                lattice[x] += [cell(1,x,y) if ((y == math.floor(length/2)\
                                                or y == math.floor(length/2)-1))\
                                               and (x == math.floor(length/2)\
                                                or x == math.floor(length/2)-1)\
                                           else cell(0,x,y)]

    elif choice == 3:
        for x in range(length):
            for y in range(length):
                lattice[x] += [cell(1,x,y) if (x == math.floor(length/2)\
                                               and (y == math.floor(length/2)+1\
                                                or y == math.floor(length/2)\
                                                or y == math.floor(length/2)-1))\
                                           else cell(0,x,y)]

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
        
        for x in lattice:
            for y in x:
                print(y.get_life(), end = ' ')
            print('\n')
        print('\n')    
        
def main():
    print("Choose a pattern: ")
    print("1. Line\n2. Block\n3. Blinker")
    choice = int(input())
    print("Length of the nxn lattice: ")
    size = int(input())
    print("Number of evaluations: ")
    number = int(input())
    
    lattice = set_lattice(size, choice)
    
    for x in lattice:
        for y in x:
            print(y.get_life(), end = '   ')
        print('\n')
    print('-----')
    
    play(lattice, number)

    for x in lattice:
        for y in x:
            print(y.get_life(), end = '   ')
        print('\n')
        
if __name__ == '__main__':
    main()
