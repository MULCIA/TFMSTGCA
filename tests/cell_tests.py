from unittest import TestCase
from TFMSTGCA.cell import *

class TestCell(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        position = (1,1,1)
        self.genome = Genome(1,1,1,1,1)
        self.cell = Cell(position, 1,1,1,1,1, 50, 10**5)

    def test_get_genome_mutations(self):
        self.assertEqual(self.genome.mutations(), 5)

    def test_get_genome_mutations(self):
        self.assertEqual(self.cell.mutations(), 5)

    def test_decrease_telomer(self):
        self.assertEqual(self.cell.decrease_telomer, 49)