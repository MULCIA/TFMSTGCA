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

    def test_pop_events(self):
        iteration = 5
        self.automata.mitotic_agenda[iteration] = "Event!"
        self.automata.pop_events(iteration)
        self.assertTrue(iteration not in self.automata.mitotic_agenda)

    def test_push_event(self):
        self.assertTrue(self.automata.push_event())

    def test_apply_random_cell_death(self):
        self.assertTrue(self.automata.apply_random_cell_death(None))

    def test_apply_genetic_damage_death(self):
        self.assertTrue(self.automata.apply_genetic_damage_death(None))
