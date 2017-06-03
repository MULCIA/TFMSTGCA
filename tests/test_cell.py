from unittest import TestCase
from TFMSTGCA.cell import Cell
from TFMSTGCA.genome import Genome

class TestCell(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        position = (1,1,1)
        self.genome = Genome(1,1,1,1,1)
        self.cell = Cell(position, 1,1,1,1,1, 50, 10**5)

    def test_get_mutations(self):
        self.assertEqual(self.cell.mutations(), 5)

    def test_decrease_telomer(self):
        self.cell.decrease_telomer()
        self.assertEqual(self.cell.tl, 49)

    def test_increment_base_muration_rate_gi_0(self):
        self.cell.genome.gi = 0
        self.cell.increment_base_muration_rate(10)
        self.assertEqual(self.cell.m, 10**5)

    def test_increment_base_muration_rate_gi_1(self):
        self.cell.increment_base_muration_rate(10)
        self.assertEqual(self.cell.m, 10**5 * 10)

    def test_kill_neighbor_empty(self):
        result = self.cell.kill_neighbor([])
        self.assertEqual(result, None)

    def test_kill_neighbor(self):
        position_a = (1,1,1)
        position_b = (1,1,2)
        result = self.cell.kill_neighbor([position_a, position_b])
        self.assertTrue(result == position_a or result == position_b)

    def test_perform_mitosis(self):
        new_cell = self.cell.perform_mitosis((1,1,1), 10**2)
        self.assertEqual(new_cell.genome.sg, self.cell.genome.sg)
        self.assertEqual(new_cell.genome.igi, self.cell.genome.igi)
        self.assertEqual(new_cell.genome.ea, self.cell.genome.ea)
        self.assertEqual(new_cell.genome.ei, self.cell.genome.ei)
        self.assertEqual(new_cell.genome.gi, self.cell.genome.gi)
        self.assertEqual(new_cell.tl, self.cell.tl)
        self.assertEqual(new_cell.m, self.cell.m)

if __name__ == '__main__':
    unittest.main()