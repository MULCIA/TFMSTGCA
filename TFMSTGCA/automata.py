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

    def push_event(self):
        return True

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

    def run(self):
        for it in range(self.iterations):
            if it in self.mitotic_agenda:
                events = self.pop_events(it)
                for pos in events:
                    current_cell = self.cells[pos]
                    if self.experiments.random_death_test():
                        self.apply_random_cell_death(pos)
                    if self.experiments.genetic_damage_test(current_cell.mutations(), current_cell.genome.ea):
                        self.apply_genetic_damage_death(pos)
                    #TODO: Rest of experiments.
