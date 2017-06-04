from unittest import TestCase
from TFMSTGCA.cell import Cell
from TFMSTGCA.grid import Grid

class TestExperiments(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        position = (1,1,1)
        first_cell = Cell(position, 1,1,1,1,1, 50, 10**5)
        self.grid = Grid(3, 3, 3, first_cell)

    def test_initialization(self):
        self.assertTrue(self.grid.grid[1][1][1], Cell((1,1,1), 1,1,1,1,1, 50, 10**5))