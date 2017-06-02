import numpy as np
from genome import *

class Cell(object):

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