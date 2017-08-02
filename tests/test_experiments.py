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

    def test_genetic_damage_test_True(self):
        result = self.experiments.growth_factor_cheking(1, 2)
        self.assertEqual(result, True)

    def test_genetic_damage_test_False(self):
        result = self.experiments.growth_factor_cheking(0, 2)
        self.assertEqual(result, False)

    def test_limitless_replicative_potencial_checking_limiteless(self):
        result = self.experiments.limitless_replicative_potencial_checking(0, 0)
        self.assertEqual(result, False)

    def test_limitless_replicative_potencial_checking_limited(self):
        result = self.experiments.limitless_replicative_potencial_checking(1, 0)
        self.assertEqual(result, False)

    def test_mitosis_test_mitosis(self):
        result = self.experiments.mitosis_test((True, False, False))
        self.assertEqual(result, True)

    def test_mitosis_test_not_mitosis(self):
        result = self.experiments.mitosis_test((False, False, False))
        self.assertEqual(result, False)

    def test_probability_random_death(self):
        self.experiments.simulationGlobals.a = 10**3
        result = [self.experiments.random_death_test() for i in range(10**4)]
        self.assertTrue(1 <= result.count(True) <= 30)

    def test_probability_genetic_damage(self):
        self.experiments.simulationGlobals.e = 10
        result = [self.experiments.genetic_damage_test(5, 0) for i in range(100)]
        self.assertTrue(35 <= result.count(True) <= 65)

    def test_probability_ignore_growth_inhibit_checking(self):
        self.experiments.simulationGlobals.g = 30
        result = [self.experiments.ignore_growth_inhibit_checking(1) for i in range(100)]
        self.assertTrue(0 <= result.count(True) <= 10)

if __name__ == '__main__':
    unittest.main()
