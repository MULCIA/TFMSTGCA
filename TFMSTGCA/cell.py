import numpy as np
from .genome import Genome

class Cell(object):

    def __init__(self, position, sg, igi, ea, ei, gi, tl, m):
        self.position = position
        self.tl = tl
        self.m = m
        self.genome = Genome(sg, igi, ea, ei, gi)

    def decrease_telomer(self):
        if self.tl > 0:
            self.tl -= 1

    def increment_base_muration_rate(self, i):
        if self.genome.gi == 1:
            self.m *= i

    def mutations(self):
        return self.genome.mutations()

    def add_mutations(self):
        for var,val in vars(self.genome).items():
            if val== 0 and np.random.random() < 1/self.m:
                setattr(self.genome, var, 1)

    def perform_mitosis(self, position, i):
        self.decrease_telomer()
        self.increment_base_muration_rate(i)
        new_cell = Cell(position, self.genome.sg, self.genome.igi, self.genome.ea, self.genome.ei, self.genome.gi, self.tl, self.m)
        new_cell.add_mutations()
        return new_cell

    def __str__(self):
        return str(self.genome)
