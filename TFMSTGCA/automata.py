import random
import numpy as np
from .experiments import Experiments
from .cell import Cell
from .grid import Grid

class Automata(object):

    def __init__(self, dimension, iterations, simulationGlobals):
        self.dimension = dimension
        self.size = self.dimension**3
        self.iterations = iterations+1
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

    def kill_cell(self, position):
        del self.cells[position]
        self.grid.grid[position[0]][position[1]][position[2]] = ''

    def copy_and_choose_new_position(self, position, cell, iteration):
        neighborhood = self.grid.classify_neighborhood(self.grid.check_limits(self.grid.neighborhood(position, 1), self.dimension))
        new_position = random.choice(neighborhood['empties'])
        cell_copy = cell.perform_mitosis(new_position, self.simulationGlobals.i)
        self.push_event(iteration + self.future_mitotic_event(), cell_copy.position)
        self.cells[position] = cell
        self.cells[new_position] = cell_copy

    def first_test(self, cell):
        spatial_boundary = 0 #TODO: check spatial boundary
        return self.experiments.growth_factor_cheking(cell.genome.sg, spatial_boundary)

    def second_test(self, cell):
        is_neighborhood_full = False #TODO: check neighborhood
        if is_neighborhood_full:
            return self.experiments.ignore_growth_inhibit_checking(cell.genome.igi)
        else:
            return True

    def third_test(self, cell):
        return self.experiments.limitless_replicative_potencial_checking(cell.tl, cell.genome.ei)

    def telomer_death_test(self, test_result):
        if not test_result:
            return True
        return False

    def run(self):
        for iteration in range(self.iterations):
            print(self.cells)
            events = self.pop_events(iteration) if iteration in self.mitotic_agenda else []
            for event in events: # event is a tuple with three elements == position
                cell = self.cells[event]
                if self.experiments.random_death_test():
                    self.kill_cell(event)
                elif self.experiments.genetic_damage_test(cell.mutations(), cell.genome.ea):
                    self.kill_cell(event)
                else:
                    test_1, test_2, test_3 = self.first_test(cell), self.second_test(cell), self.third_test(cell)
                    if test_1 and test_2 and test_3: #Perform mutation
                        self.copy_and_choose_new_position(event, cell, iteration)
                    else:
                        if self.telomer_death_test(test_3): #Telomer death
                            self.kill_cell(event)
                        else:
                            self.push_event(iteration + self.future_mitotic_event(), event)
