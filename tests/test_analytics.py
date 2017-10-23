import copy
from unittest import TestCase
from TFMSTGCA.cell import Cell
from TFMSTGCA.analytics import Analytics

class TestAnalytics(TestCase):

    def setUp(self):
        self.analytics = Analytics()
        self.cells = {
            (0,0,0): Cell((0,0,0),0,0,0,0,0,50,10**5),
            (0,0,1): Cell((0,0,1),0,0,0,0,0,50,10**5),
            (0,1,0): Cell((0,1,0),1,0,0,0,0,50,10**5),
            (0,1,1): Cell((0,1,1),1,0,0,0,0,50,10**5),
            (1,0,0): Cell((1,0,0),0,1,0,0,0,50,10**5),
            (1,0,1): Cell((1,0,1),0,1,0,0,0,50,10**5),
            (1,1,0): Cell((1,1,0),0,0,1,0,0,50,10**5),
            (1,1,1): Cell((1,1,1),0,0,1,0,0,50,10**5),
            (0,0,2): Cell((0,0,2),0,0,0,1,0,50,10**5),
            (0,2,0): Cell((0,2,0),0,0,0,1,0,50,10**5),
            (0,2,2): Cell((0,2,2),0,0,0,0,1,50,10**5),
            (2,0,0): Cell((2,0,0),0,0,0,0,1,50,10**5),
            (2,0,2): Cell((2,0,2),1,1,1,1,1,50,10**5),
            (2,2,0): Cell((2,2,0),1,1,1,1,1,50,10**5)
        }
        self.iterations_cells = {
            10: copy.deepcopy(self.cells),
            20: copy.deepcopy(self.cells)
        }

    def test_sum_analytics_cells(self):
        result = self.analytics.sum_analytics_cells(self.cells)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 12)
        self.assertEqual(result[2], 4)
        self.assertEqual(result[3], 4)
        self.assertEqual(result[4], 4)
        self.assertEqual(result[5], 4)
        self.assertEqual(result[6], 4)

    def test_get_measurements(self):
        result = self.analytics.get_measurements(self.iterations_cells)
        measure, mutation_measure = result[0], result[1]
        self.assertEqual(len(measure['iterations']), 2)
        self.assertEqual(len(mutation_measure['iterations']), 2)
        measure_cells = measure['cells']
        self.assertEqual(measure_cells[0], 14)
        self.assertEqual(measure_cells[1], 14)
        measure_healty = measure['healthy']
        self.assertEqual(measure_healty[0], 2)
        self.assertEqual(measure_healty[1], 2)
        mutation_measure_sg = mutation_measure['sg']
        self.assertEqual(mutation_measure_sg[0], 4)
        self.assertEqual(mutation_measure_sg[1], 4)
        mutation_measure_igi = mutation_measure['igi']
        self.assertEqual(mutation_measure_igi[0], 4)
        self.assertEqual(mutation_measure_igi[1], 4)
        mutation_measure_ea = mutation_measure['ea']
        self.assertEqual(mutation_measure_ea[0], 4)
        self.assertEqual(mutation_measure_ea[1], 4)
        mutation_measure_ei = mutation_measure['ei']
        self.assertEqual(mutation_measure_ei[0], 4)
        self.assertEqual(mutation_measure_ei[1], 4)
        mutation_measure_gi = mutation_measure['gi']
        self.assertEqual(mutation_measure_gi[0], 4)
        self.assertEqual(mutation_measure_gi[1], 4)
