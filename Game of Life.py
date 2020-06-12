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
            if x == math.floor(length/2):
                lattice += [[cell(1,x,y) for y in range(length)]]
            else:
                lattice += [[cell(0,x,y) for y in range(length)]]

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
#        count_1 = 0
#        count_0 = 0
##        for n in lattice:
#            if n.get_life() == 1:
#                count_1 += 1
#            else:
#                count_0 += 1
#        print(count_1 / (count_1 + count_0), end=', ')
#        print('\n')
#        for n in lattice:
#            print(n.genome if len(n.genome) != 0 else 10*'-')
#    
        
def main():
    print("Choose a pattern: ")
    print("1.\n2. Block\n3. Blinker")
    choice = int(input())
    print("Size of the lattice: ")
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
        
main()

