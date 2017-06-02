from unittest import TestCase
from TFMSTGCA.experiments import Experiments
from TFMSTGCA.simulation_globals import SimulationGlobals

class TestExperiments(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.simulationGlobals = SimulationGlobals(1,1,1,1,1,1,1,1,1)
        self.experiments = Experiments(self.simulationGlobals)

    def test_random_death_test(self):
        result = self.experiments.random_death_test()
        self.assertEqual(result, True)

    def test_genetic_damage_test_True(self):
        result = self.experiments.genetic_damage_test(self.simulationGlobals.e, 0)
        self.assertEqual(result, True)

    def test_genetic_damage_test_False(self):
        result = self.experiments.genetic_damage_test(1, 1)
        self.assertEqual(result, False)

    def test_limitless_replicative_potencial_checking_limiteless(self):
        result = self.experiments.limitless_replicative_potencial_checking(0, 0)
        self.assertEqual(result, True)

    def test_limitless_replicative_potencial_checking_limited(self):
        result = self.experiments.limitless_replicative_potencial_checking(1, 0)
        self.assertEqual(result, False)

    def test_mitosis_test_mitosis(self):
        result = self.experiments.mitosis_test((True, False, False))
        self.assertEqual(result, True)

    def test_mitosis_test_not_mitosis(self):
        result = self.experiments.mitosis_test((False, False, False))
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()