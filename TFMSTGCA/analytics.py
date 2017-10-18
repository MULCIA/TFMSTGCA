import numpy as np
import matplotlib.pyplot as plt
from .cell import Cell

class Analytics(object):

    def __init__(self, cells, np_grid):
        self.cells = cells
        self.np_grid = np_grid

    def plot_cells(self):
        pass

    def plot_grid(self):
        pass

    def sum_healthy_cells(self):
        cont = 0
        for position,cell in self.cells.items():
            if str(cell) == '00000':
                cont += 1
        return cont

    def sum_carcinogenic_cells(self):
        cont = 0
        for position,cell in self.cells.items():
            if str(cell) != '00000':
                cont += 1
        return cont

    def sum_sg_mutations(self):
        cont = 0
        for position,cell in self.cells.items():
            if cell.genome.sg:
                cont += 1
        return cont

    def sum_igi_mutations(self):
        cont = 0
        for position,cell in self.cells.items():
            if cell.genome.igi:
                cont += 1
        return cont

    def sum_ea_mutations(self):
        cont = 0
        for position,cell in self.cells.items():
            if cell.genome.ea:
                cont += 1
        return cont

    def sum_ei_mutations(self):
        cont = 0
        for position,cell in self.cells.items():
            if cell.genome.ei:
                cont += 1
        return cont

    def sum_gi_mutations(self, cells):
        cont = 0
        for position,cell in self.cells.items():
            if cell.genome.gi:
                cont += 1
        return cont
