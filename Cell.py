import random
import math
import string

initial_p_birth = 0.5
p_death_change = 0.1
initial_p_death = 0.1
initial_mutation_rate = 0.2
genome_size = 10

class cell(object):
    def __init__(self,life, x, y):
        self.life = life
        self.age = 0
        self.p_birth = initial_p_birth if self.life==0 else 0
        self.p_death = 0 if self.life==0 else initial_p_death
        self.genome = self.random_genome(genome_size) if life == 1 else ''
        self.mutation_rate = 0 if self.life == 0 else initial_mutation_rate
        self.x = x
        self.y = y
    
    def get_life(self):
        return self.life
    
    def get_age(self):
        return self.age
    
    def get_p_birth(self):
        return self.p_birth
    
    def get_p_death(self):
        return self.p_death
    
    def get_genome(self):
        return self.genome
    
    def get_mutation_rate(self):
        return self.mutation_rate
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_life(self, life):
        '''
        According to the input (0 or 1), reassigns the attribute values.
        '''
        self.life = life
        if life == 0:
            self.age = 0
            self.p_birth = initial_p_birth
            self.p_death = initial_p_death
            self.mutation_rate = 0
            self.genome = ''
        else:
            self.age = 0
            self.p_birth = 0
            self.p_death = 0.1
            self.mutation_rate = initial_mutation_rate
            self.genome = self.random_genome(genome_size)

    def add_age(self):
        self.age += 1
        
    def change_p_birth(self, value):
        self.p_birth += value
        
    def change_p_death(self, value):
        self.p_death += value
    
    def random_genome(self, genome_length):
        characters = string.ascii_letters
        return ''.join(random.choice(characters) for i in range(genome_length))
    
    def mutate_genome(self):
        for n in self.get_genome():
            if random.random() < self.get_mutation_rate():
                self.genome = self.genome.replace(n, random.choice(string.ascii_letters))
                
    def evaluate(self, lattice):
        neighborhood = self.get_neighborhood(lattice, 'Mr')
        
        #TODO: develop the algorithm
        count = 0
        for n in neighborhood:
            if n.get_life():
                count += 1
                
        if self.get_life():
            if count < 2 or count > 3:
                self.set_life(0)
            
        else:
            if count == 3:
                self.set_life(1)

                
    def get_neighborhood(self, lattice, neighborhood_type):
        #TODO: add a try-except statement
        neighborhood = []
        
        if self.x == 0:
            if self.y == 0:
                if neighborhood_type == 'vN':
                    neighborhood = [lattice[(self.x)+1][self.y],
                                    lattice[self.x][(self.y)+1]]             
                elif neighborhood_type == 'Mr':
                    neighborhood = [lattice[self.x+1][self.y],
                                    lattice[self.x][self.y+1],
                                    lattice[self.x+1][self.y+1]]
            elif self.y == len(lattice[0])-1:
                if neighborhood_type == 'vN':
                    neighborhood = [lattice[self.x][(self.y)-1],
                                    lattice[(self.x)+1][self.y]]
                elif neighborhood_type == 'Mr':
                    neighborhood = [lattice[self.x][self.y-1],
                                    lattice[self.x+1][self.y-1],
                                    lattice[self.x+1][self.y]]
            else:
                if neighborhood_type == 'vN':
                    neighborhood = [lattice[self.x][(self.y)-1],
                                    lattice[(self.x)+1][self.y],
                                    lattice[self.x][(self.y)+1]]
                elif neighborhood_type == 'Mr':
                    neighborhood = [lattice[self.x][self.y-1],
                                    lattice[self.x+1][self.y-1],
                                    lattice[self.x+1][self.y],
                                    lattice[self.x][self.y+1],
                                    lattice[self.x+1][self.y+1]]
        elif self.x == len(lattice[0])-1:
            if self.y == 0:
                if neighborhood_type == 'vN':
                    neighborhood = [lattice[(self.x)-1][self.y],
                                    lattice[self.x][(self.y)+1]]
                elif neighborhood_type == 'Mr':
                    neighborhood = [lattice[self.x-1][self.y],
                                    lattice[self.x-1][self.y+1],
                                    lattice[self.x][self.y+1]]

            elif self.y == len(lattice[0])-1:
                if neighborhood_type == 'vN':
                        neighborhood = [lattice[self.x][(self.y)-1],
                                        lattice[(self.x)-1][self.y]]
                elif neighborhood_type == 'Mr':
                        neighborhood = [lattice[self.x-1][self.y-1],
                                        lattice[self.x][self.y-1],
                                        lattice[self.x-1][self.y]]
        else:
            if self.y == 0:
                if neighborhood_type == 'vN':
                    neighborhood = [lattice[(self.x)-1][self.y],
                                    lattice[(self.x)+1][self.y],
                                    lattice[self.x][(self.y)+1]]
                elif neighborhood_type == 'Mr':
                    neighborhood = [lattice[self.x-1][self.y],
                                    lattice[self.x+1][self.y],
                                    lattice[self.x-1][self.y+1],
                                    lattice[self.x][self.y+1],
                                    lattice[self.x+1][self.y+1]]
            elif self.y == len(lattice[0])-1:
                if neighborhood_type == 'vN':
                    neighborhood = [lattice[self.x][(self.y)-1],
                                    lattice[(self.x)-1][self.y],
                                    lattice[(self.x)+1][self.y]]
                elif neighborhood_type == 'Mr':
                    neighborhood = [lattice[self.x-1][self.y-1],
                                    lattice[self.x][self.y-1],
                                    lattice[self.x+1][self.y-1],
                                    lattice[self.x-1][self.y],
                                    lattice[self.x+1][self.y]]
            else:
                    if neighborhood_type == 'vN':
                        neighborhood = [lattice[self.x][(self.y)-1],
                                        lattice[(self.x)-1][self.y],
                                        lattice[(self.x)+1][self.y],
                                        lattice[self.x][(self.y)+1]]
                    elif neighborhood_type == 'Mr':
                        neighborhood = [lattice[self.x-1][self.y-1],
                                        lattice[self.x][self.y-1],
                                        lattice[self.x+1][self.y-1],
                                        lattice[self.x-1][self.y],
                                        lattice[self.x+1][self.y],
                                        lattice[self.x-1][self.y+1],
                                        lattice[self.x][self.y+1],
                                        lattice[self.x+1][self.y+1]]
        
        return neighborhood