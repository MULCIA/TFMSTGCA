from unittest import TestCase
from TFMSTGCA import *

class TestGenome(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.genome = Genome(1,1,1,1,1)

    def test_get_mutations(self):
        self.assertEqual(self.genome.mutations(), 5)

if __name__ == '__main__':
    unittest.main()