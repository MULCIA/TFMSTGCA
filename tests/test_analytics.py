from unittest import TestCase
import numpy as np
import matplotlib.pyplot as plt
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

    def test_sum_healthy_cells(self):
        result = self.analytics.sum_healthy_cells(self.cells)
        self.assertEqual(result, 2)

    def test_sum_carcinogenic_cells(self):
        result = self.analytics.sum_carcinogenic_cells(self.cells)
        self.assertEqual(result, 12)

    def test_sum_sg_mutations(self):
        result = self.analytics.sum_sg_mutations(self.cells)
        self.assertEqual(result, 4)

    def test_sum_igi_mutations(self):
        result = self.analytics.sum_igi_mutations(self.cells)
        self.assertEqual(result, 4)

    def test_sum_ea_mutations(self):
        result = self.analytics.sum_ea_mutations(self.cells)
        self.assertEqual(result, 4)

    def test_sum_ei_mutations(self):
        result = self.analytics.sum_ei_mutations(self.cells)
        self.assertEqual(result, 4)

    def test_sum_gi_mutations(self):
        result = self.analytics.sum_gi_mutations(self.cells)
        self.assertEqual(result, 4)
