from unittest import TestCase
from TFMSTGCA.simulation_globals import SimulationGlobals

class TestSimulationGlobals(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        self.simulationGlobals = SimulationGlobals(10**5,50,10,10**2,30,10**3,0.95,5,10)

    def test_simulations_params(self):
        self.assertEqual(self.simulationGlobals.m, 10**5)
        self.assertEqual(self.simulationGlobals.tl, 50)
        self.assertEqual(self.simulationGlobals.e, 10)
        self.assertEqual(self.simulationGlobals.i, 10**2)
        self.assertEqual(self.simulationGlobals.g, 30)
        self.assertEqual(self.simulationGlobals.a, 10**3)
        self.assertEqual(self.simulationGlobals.predefined_spatial_boundary, 0.95)
        self.assertEqual(self.simulationGlobals.min_future_mitotic_event, 5)
        self.assertEqual(self.simulationGlobals.max_future_mitotic_event, 10)

if __name__ == '__main__':
    unittest.main()