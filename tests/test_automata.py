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

    def test_push_event_create(self):
        event = (1,1,1)
        iteration = 5
        self.automata.push_event(iteration, event)
        events = self.automata.mitotic_agenda[iteration]
        self.assertEqual(events[0], event)

    def test_push_event_update(self):
        iteration = 5
        self.automata.push_event(iteration, (1,1,1))
        self.automata.push_event(iteration, (2,2,2))
        events = self.automata.mitotic_agenda[iteration]
        self.assertTrue((1,1,1) in events)
        self.assertTrue((2,2,2) in events)

    def test_kill_cell(self):
        self.automata.kill_cell((1,1,1))
        self.assertTrue((1,1,1) not in self.automata.cells.keys())
        self.assertEqual(self.automata.grid.grid[1][1][1],'')

    def test_mutate(self):
        self.automata.mutate(None)
        self.assertTrue(True)

    def test_modify_gi(self):
        self.automata.modify_gi(None)
        self.assertTrue(True)

    def copy_and_choose_new_position(self):
        self.automata.copy_and_choose_new_position(None)
        self.assertTrue(True)
