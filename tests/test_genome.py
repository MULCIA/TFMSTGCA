from unittest import TestCase
from TFMSTGCA.genome import Genome

class TestGenome(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.genome = Genome(1,1,1,1,1)

    def test_get_mutations(self):
        self.assertEqual(self.genome.mutations(), 5)

    def test_string(self):
        self.assertEqual(str(self.genome),"11111")

if __name__ == '__main__':
    unittest.main()
