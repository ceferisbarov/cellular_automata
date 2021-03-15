class Cell(object):
    """
    This class is used as cells of the Cellular Automaton lattice.
    While not necessary for a conventional Conway's Game of Life program,
    it will be helpful in expanding the Game into something more.
    """
    def __init__(self,life, x, y):
        self.life = life
        self.x = x
        self.y = y
    
    def get_life(self):
        return self.life
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_life(self, life):
        self.life = life
                
    def evaluate(self, lattice):
        """
        Given the neighborhood, we calculate the next state of the cell,
        according to rules of the Game.
        Rules are to be changed and expanded for new projects.
        """
        neighborhood = self.get_neighborhood(lattice, 'Mr')
        
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
        """
        There are several different types of neighborhoods in CA.
        Here we can find von Neumann or Moore neighborhood of the given cell,
        according to the given input.
        """
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
