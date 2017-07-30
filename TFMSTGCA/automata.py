import numpy as np
from .experiments import Experiments
from .cell import Cell
from .grid import Grid

class Automata(object):

    def __init__(self, dimension, iterations, simulationGlobals):
        self.dimension = dimension
        self.size = self.dimension**3
        self.iterations = iterations
        self.simulationGlobals = simulationGlobals
        self.experiments = Experiments(simulationGlobals)
        self.cells = {}
        self.mitotic_agenda = {}
        self.grid = self.build()

    def build(self):
        position = (int(self.dimension/2),int(self.dimension/2),int(self.dimension/2))
        first_cell = Cell(position, 0, 0, 0, 0, 0, self.simulationGlobals.tl, self.simulationGlobals.m)
        self.cells[position] = first_cell
        grid = Grid(self.dimension, self.dimension, self.dimension, first_cell)
        self.mitotic_agenda[self.future_mitotic_event()] = [position]
        return grid

    def push_event(self, iteration, event):
        if iteration in self.mitotic_agenda:
            events = self.mitotic_agenda[iteration]
            events.append(event)
            self.mitotic_agenda[iteration] = events
        else:
            self.mitotic_agenda[iteration] = [event]

    def future_mitotic_event(self):
        return np.random.randint(self.simulationGlobals.min_future_mitotic_event, self.simulationGlobals.max_future_mitotic_event+1)

    def pop_events(self, iteration):
        events = self.mitotic_agenda[iteration]
        del self.mitotic_agenda[iteration]
        return events

    def apply_random_cell_death(self, position):
        #TODO: Remove cell from cell and from grid.
        return True

    def apply_genetic_damage_death(self, position):
        #TODO: Remove cell from cell and from grid.
        return True

    def apply_mitosis(self, test_1, test_2, test_3):
        if self.experiments.mitosis_test((test_1, test_2, test_3)):
            return True
        return False

    def apply_mutation(self, cell):
        pass

    def apply_modify_gi(self, cell):
        pass

    def copy_and_choose_new_position(self, cell):
        #TODO: make copy, choose new position and put in grid and cell list.
        pass

    def run(self):
        for iteration in range(self.iterations):
            events = self.pop_events(iteration) if iteration in self.mitotic_agenda else []
            for event in events: # event is a tuple with three elements == position
                cell = self.cells[event]
                if self.experiments.random_death_test():
                    self.apply_random_cell_death(event)
                elif self.experiments.genetic_damage_test(cell.mutations(), cell.genome.ea):
                    self.apply_genetic_damage_death(event)
                else:
                    spatial_boundary = 0 #TODO: check spatial boundary
                    is_neighborhood_full = True #TODO: check neighborhood
                    test_1 = self.experiments.growth_factor_cheking(cell.genome.sg, spatial_boundary)
                    test_2 = self.experiments.ignore_growth_inhibit_checking(is_neighborhood_full, cell.genome.igi)
                    test_3 = self.experiments.limitless_replicative_potencial_checking(cell.tl, cell.genome.ei)
                    if self.apply_mitosis(test_1, test_2, test_3):
                        cell = self.apply_mutation(cell)
                        cell = self.apply_modify_gi(cell)
                        self.copy_and_choose_new_position(cell)
                    self.push_event(self.future_mitotic_event(), cell)
