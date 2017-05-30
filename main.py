import numpy as np

MUTATION_RATE = 10**5 
TELOMER_LENGTH = 50
DEATH_PROBABILITY = 10
FACTOR_INCREASE_BASE_RATE_MUTATION = 10**2
KILL_NRIGHBOR = 30
RANDOM_DEATH = 10**3


class SimulationGlobals:

    def __init__(self, mutation_rate, telomer_length, death_probability, factor_increase_base_rate_mutation, kill_neighbor, random_death):
        self.m = mutation_rate
        self.tl = telomer_length
        self.e = death_probability
        self.i = factor_increase_base_rate_mutation
        self.g = kill_neighbor
        self.a = random_death

class Tests:

    def __init__(self, simulationGlobals):
        self. simulationGlobals = simulationGlobals

    """ 
        Test 1: muerte aleatoria de la célula, con probabilidad 1/a.
    """
    def test_1(self):
        if np.random.random() < 1/self.simulationGlobals.a:
            return True
        return False

    """
        Test 2: muerte por mutaciones, con n mutaciones sufridas tiene probabilidad de muerte n/e.
    """
    def test_2(self, n, ea):
        if ea == 0 and np.random.randint(0,n) < n/self.simulationGlobals.e:
            return True
        return False
        """if cell in cells:
            cell_genome = cells[cell]
            n = cell_genome.mutations()
            if not cell_genome.ea:
                if np.random.randint(0,n) < n/self.simulationGlobals.e:
                    print("Muerte por mutaciones")
                    return '0'
        return '1'"""

    """
        Test 3: 
    """
    def test_3(self):
        pass

    """
        Test 4: matar a un vecino, si el vecindario está completo, probabilidad de matar a un vecino 1/g.
    """
    def test_4(self, is_neighborhood_full, igi):
        if is_neighborhood_full and igi == 1 and np.random.random() < 1/self.simulationGlobals.g:
            return True
        return False
        """full = check_full_neighborhood(cell, cells)
        if full and cell.igi and np.random.random() < 1/self.simulationGlobals.g:
            return '1'
        return '0'"""

    """
        Test 5: muerte por acortamiento de telomero. 
    """
    def test_5(self, tl, ei):
        if tl == 0 and ei == 0:
            return True
        return False


class Genome:
    
    def __init__(self, sg, igi, ea, ag, ei, mt):
        self.sg = sg
        self.igi = igi
        self.ea = ea
        self.ag = ag
        self.ei = ei
        self.mt = mt

    def mutations(self):
        count = 0
        if self.sg:
            count += 1
        if self.igi:
            count += 1
        if self.ea:
            count += 1
        if self.ag:
            count += 1
        if self.ei:
            count += 1
        if self.mt:
            count += 1
        return count

    def __str__(self):
        return str(self.sg) + str(self.igi) + str(self.ea) + str(self.ag) + str(self.ei) + str(self.mt)

class Cell:

    def __init__(self, position, sg, igi, ea, ag, ei, mt, tl):
        self.position = position
        self.tl = tl
        self.genome = Genome(sg, igi, ea, ag, ei, mt)

    def decrease_telomer(self):
        self.tl -= 1

    def mutations(self):
        return self.genome.mutations()

    def __str__(self):
        return str(self.genome)

class Grid:

    def __init__(self, height, width, depth, first_cell):
        self.height = height
        self.width = width
        self.depth = depth
        self.grid = self.build()
        self.initialization(first_cell)

    def build(self):
        grid = np.empty((self.height,self.width,self.depth))
        grid = grid.astype(np.str_)
        grid.fill('')
        return grid

    def initialization(self, first_cell):
        self.grid[int(self.height/2)][int(self.width/2)][int(self.depth/2)] = first_cell

class Automata:
    
    def __init__(self, dimension, iterations, simulationGlobals):
        self.dimension = dimension
        self.iterations = iterations
        self.simulationGlobals = simulationGlobals
        self.tests = Tests(simulationGlobals)
        self.cells = {}
        self.mitotic_agenda = {}
        self.grid = self.build()
        

    def build(self):
        position = (self.dimension/2,self.dimension/2,self.dimension/2)
        first_cell = Cell(position, 0, 0, 0, 0, 0, 0, self.simulationGlobals.tl)
        self.cells[position] = first_cell
        grid = Grid(self.dimension,self.dimension,self.dimension, first_cell)
        self.mitotic_agenda[self.future_mitotic_event()] = position
        return grid

    def future_mitotic_event(self):
        return np.random.randint(5,11)

    def run(self):
        pass


if __name__ == "__main__":

    """height = 10
    width = 10
    depth = 10

    grid = np.empty((height,width,depth))

    grid = grid.astype(np.str_)

    grid.fill(0)

    print(grid)"""

    """grid = Grid(10,10,10, None)
    print(grid.grid)"""

    simulationGlobals = SimulationGlobals(MUTATION_RATE, TELOMER_LENGTH, DEATH_PROBABILITY, FACTOR_INCREASE_BASE_RATE_MUTATION, KILL_NRIGHBOR, RANDOM_DEATH)

    #first_cell = Genome(0, 0, 0, 0, 0, 0, 50)

    #grid = Grid(3,3,3)

    automata = Automata(3, 10, simulationGlobals)

    print(automata.grid.grid)

