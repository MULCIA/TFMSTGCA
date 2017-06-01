import random
import numpy as np

# In each cell
BASE_MUTATION_RATE = 10**5 #TODO: Check if correct value is 10**5 or 10**(-5)
TELOMER_LENGTH = 50

# Global
EVADE_APOPTOSIS = 10
FACTOR_INCREASE_BASE_RATE_MUTATION = 10**2
KILL_NEIGHBOR_PROBABILITY = 30
RANDOM_CELL_DEATH = 10**3

# Growth factor
PREDEFINED_SPATIAL_BOUNDARY = 0.95 #TODO: Check this value. Other posibility is 0.858.

# Random parameters for generating future mitotic event
MIN_FUTURE_MITOTIC_EVENT = 5
MAX_FUTURE_MITOTIC_EVENT = 10

class SimulationGlobals:

    def __init__(self, base_mutation_rate, telomer_length, evade_apoptosis, factor_increase_base_rate_mutation, kill_neighbor, random_death, predefined_spatial_boundary, min_future_mitotic_event, max_future_mitotic_event):
        self.m = base_mutation_rate
        self.tl = telomer_length
        self.e = evade_apoptosis
        self.i = factor_increase_base_rate_mutation
        self.g = kill_neighbor
        self.a = random_death
        self.predefined_spatial_boundary = predefined_spatial_boundary
        self.min_future_mitotic_event = min_future_mitotic_event
        self.max_future_mitotic_event = max_future_mitotic_event

class Tests:

    def __init__(self, simulationGlobals):
        self. simulationGlobals = simulationGlobals

    """ 
        Test 1: muerte aleatoria de la célula, con probabilidad 1/a.
    """
    def random_death_test(self):
        if np.random.random() < 1/self.simulationGlobals.a:
            return True
        return False

    """
        Test 2: muerte por mutaciones, con n mutaciones sufridas tiene probabilidad de muerte n/e.
    """
    def genetic_damage_test(self, n, ea):
        #TODO: np.random.randint(0,n)
        if ea == 0 and np.random.random() < n/self.simulationGlobals.e:
            return True
        return False

    """
        Test 3: factor de crecimiento dentro de umbral 
    """
    def growth_factor_cheking(self, sg, spatial_boundary):
        if spatial_boundary > self.predefined_spatial_boundary and sg == 0:
            return False
        return True

    """
        Test 4: matar a un vecino, si el vecindario está completo, probabilidad de matar a un vecino 1/g.
    """
    def ignore_growth_inhibit_checking(self, is_neighborhood_full, igi):
        if is_neighborhood_full and igi == 1 and np.random.random() < 1/self.simulationGlobals.g:
            return True
        return False

    """
        Test 5: muerte por acortamiento de telomero. 
    """
    def limitless_replicative_potencial_checking(self, tl, ei):
        if tl == 0 and ei == 0:
            return True
        return False

    """
        Check if applicable mitotic event from Test 3 to Test 5 results.
    """
    def mitosis_test(self, checking_results):
        if checking_results == (True, False, False):
            return True
        return False


class Genome:
    
    def __init__(self, sg, igi, ea, ei, gi):
        self.sg = sg
        self.igi = igi
        self.ea = ea
        self.ei = ei
        self.gi = gi

    def mutations(self):
        return sum(vars(self).values())

    def __str__(self):
        return str(self.sg) + str(self.igi) + str(self.ea) + str(self.ei) + str(self.gi)

class Cell:

    def __init__(self, position, sg, igi, ea, ei, gi, tl, m):
        self.position = position
        self.tl = tl
        self.m = m
        self.genome = Genome(sg, igi, ea, ei, gi)

    def decrease_telomer(self):
        self.tl -= 1

    def increment_base_muration_rate(self, i):
        if self.gi == 1:
            self.m *= i

    def mutations(self):
        return self.genome.mutations()

    def add_mutations(self):
        vars = [var for var in vars(self) if var == 0]
        if len(vars) > 0:
            for var in vars:
                if np.random.random() < self.m:
                    setattr(self, var, 1)

    def kill_neighbor(self, neighbors):
        if len(neighbors) > 0:
            return np.random.choice(neighbors)
        return None

    def perform_mitosis(self, position, i): #TODO: Check if add_mutations() performs only on new cell.
        self.decrease_telomer()
        self.increment_base_muration_rate(i)
        new_cell = Cell(position, self.sg, self.igi, self.ea, self.ei, self.gi, self.tl, self.m)
        new_cell.add_mutations()
        return new_cell

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
        self.grid[self.__middle__(self.height)][self.__middle__(self.width)][self.__middle__(self.depth)] = first_cell

    def filter_side_positions(self, origin, positions):
        pass

    def extract_cube_from_grid(self, positions):
        return [self.grid[x][y][x] for x,y,z in positions]

    def classify_neighborhood(self, cube):
        neighbor = dict()
        neighbor['occupied'] = [cell.position for cell in cube if str(cell) != '']
        neighbor['empties'] = [cell.position for cell in cube if str(cell) == '']
        return neighbor

    def interval(x, delta, cube_dimension):
        return [i for i in [-1, 0, 1] if x + 1 >= 1 + delta and x + i <= cube_dimension - 1 + delta]

    def neighborhood(self, origin):
        x0,y0,z0 = origin
        cube_positions = [(i+1,j+1,k+1) for i in interval(a, x0, cube_dimension) for j in interval(b, y0, cube_dimension) for k in interval(c, z0, cube_dimension) if (i,j,k) != (0,0,0)]
        cube = self.extract_cube_from_grid(self.filter_side_positions(origin, cube_positions))
        neighbor = classify_neighborhood(cube)
        return neighbor

    def __middle__(self, value):
        return int(value/2)

class Automata:
    
    def __init__(self, dimension, iterations, simulationGlobals):
        self.dimension = dimension
        self.size = self.dimension**3
        self.iterations = iterations
        self.simulationGlobals = simulationGlobals
        self.tests = Tests(simulationGlobals)
        self.cells = {}
        self.mitotic_agenda = {}
        self.grid = self.build()
        

    def build(self):
        position = (int(self.dimension/2),int(self.dimension/2),int(self.dimension/2))
        first_cell = Cell(position, 0, 0, 0, 0, 0, self.simulationGlobals.tl, self.simulationGlobals.m)
        self.cells[position] = first_cell
        grid = Grid(self.dimension,self.dimension,self.dimension, first_cell)
        self.mitotic_agenda[self.future_mitotic_event()] = [position]
        return grid

    def push_event(self):
        pass

    def future_mitotic_event(self):
        return np.random.randint(self.simulationGlobals.min_future_mitotic_event, self.simulationGlobals.max_future_mitotic_event+1)

    def pop_events(self, iteration):
        events = self.mitotic_agenda[iteration]
        del self.mitotic_agenda[iteration]
        return events

    def apply_random_cell_death(self, position):
        #TODO: Remove cell from cell and from grid.
        print("Random cell death has occurred!") #TODO: Remove this statement.
        pass

    def apply_genetic_damage_death(self, position):
        #TODO: Remove cell from cell and from grid.
        print("Genetic damage death has occurred!") #TODO: Remove this statement.
        pass

    def run(self):
        for it in range(self.iterations):
            if it in self.mitotic_agenda:
                events = self.pop_events(it)
                for pos in events:
                    current_cell = self.cells[pos]
                    apply_random_cell_death(pos) if self.tests.random_death_test() else None
                    apply_genetic_damage_death(pos) if self.tests.genetic_damage_test(current_cell.mutations(), current_cell.genome.ea) else None
                    #TODO: Rest of tests.

if __name__ == "__main__":

    simulationGlobals = SimulationGlobals(BASE_MUTATION_RATE, TELOMER_LENGTH, EVADE_APOPTOSIS, FACTOR_INCREASE_BASE_RATE_MUTATION, KILL_NEIGHBOR_PROBABILITY, RANDOM_CELL_DEATH, PREDEFINED_SPATIAL_BOUNDARY, MIN_FUTURE_MITOTIC_EVENT, MAX_FUTURE_MITOTIC_EVENT)

    automata = Automata(3, 10, simulationGlobals)

    #print(automata.grid.grid[1][1][1])

    automata.run()

    #first_cell = Genome(0, 0, 0, 0, 0, 0, 50)

    #grid = Grid(3,3,3)

    """height = 10
    width = 10
    depth = 10

    grid = np.empty((height,width,depth))

    grid = grid.astype(np.str_)

    grid.fill(0)

    print(grid)"""

    """grid = Grid(10,10,10, None)
    print(grid.grid)"""



