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
        self.assertEqual(self.grid.grid[1][1][1], str(Cell((1,1,1), 1,1,1,1,1, 50, 10**5)))

    def test_neighborhood(self):
        result = self.grid.neighborhood((0,0,0), 1)
        self.assertEqual(26,len(result))

    def test_filter_True(self):
        result = self.grid.filter(0, 10)
        self.assertEqual(result, True)

    def test_filter_True(self):
        result = self.grid.filter(-1, 10)
        self.assertEqual(result, False)

    def test_extract_cube_from_grid(self):
        positions = [(0,0,0),(0,0,1)]
        result = self.grid.extract_cube_from_grid(positions)
        self.assertEqual(len(result), 2)
        self.assertTrue(result[0] == '')
        self.assertTrue(result[0] == '')
