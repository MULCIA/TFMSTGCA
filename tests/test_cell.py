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

if __name__ == '__main__':
    unittest.main()