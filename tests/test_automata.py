from unittest import TestCase
from TFMSTGCA.automata import Automata
from TFMSTGCA.simulation_globals import SimulationGlobals

class TestAutomata(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.dimension = 3
        self.iterations = 5000
        self.simulationGlobals = SimulationGlobals(1,1,1,1,1,1,1,5,10)
        self.automata = Automata(self.dimension, self.iterations, self.simulationGlobals)

    def test_future_mitotic_event(self):
        result = [self.automata.future_mitotic_event() for i in range(100)]
        for res in result:
            self.assertTrue(5 <= res <= 10)
