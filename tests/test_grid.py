from unittest import TestCase
from TFMSTGCA.cell import Cell
from TFMSTGCA.grid import Grid

class TestExperiments(TestCase):

    def setUp(self):
        self.grid = Grid(3, 3, 3)

    def test_neighborhood(self):
        result = self.grid.neighborhood((0,0,0), 1)
        self.assertEqual(26,len(result))

    def test_filter_True(self):
        result = self.grid.filter(0, 10)
        self.assertEqual(result, True)

    def test_filter_True(self):
        result = self.grid.filter(-1, 10)
        self.assertEqual(result, False)

    def test_build(self):
        grid = self.grid.build()
        self.assertEqual(grid[1][1][1], '')

    def test_create_numpy_grid(self):
        cells = {(1,1,1): Cell((1,1,1),0,0,0,0,0,50,10**5)}
        grid = self.grid.create_numpy_grid(cells)
        self.assertEqual(grid[1][1][1], '00000')
