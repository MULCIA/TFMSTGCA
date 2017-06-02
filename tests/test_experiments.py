from unittest import TestCase
from TFMSTGCA.experiments import Tests
from TFMSTGCA.simulation_globals import SimulationGlobals

class TestTests(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.simulationGlobals = SimulationGlobals(10**5,50,10,10**2,30,10**3,0.95,5,10)
        self.tests = Tests(self.simulationGlobals)

    def test_limitless_replicative_potencial_checking_limiteless(self):
        result = self.tests.limitless_replicative_potencial_checking(0, 0)
        self.assertEqual(result, True)

    def test_limitless_replicative_potencial_checking_limited(self):
        result = self.tests.limitless_replicative_potencial_checking(1, 0)
        self.assertEqual(result, False)

    def test_mitosis_test_mitosis(self):
        result = self.tests.mitosis_test((True, False, False))
        self.assertEqual(result, True)

    def test_mitosis_test_not_mitosis(self):
        result = self.tests.mitosis_test((False, False, False))
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()