from unittest import TestCase
from TFMSTGCA.automata import Automata
from TFMSTGCA.simulation_globals import SimulationGlobals
from TFMSTGCA.cell import Cell

class TestAutomata(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.length = 3
        self.iterations = 5000
        self.simulationGlobals = SimulationGlobals(1,1,1,1,1,1,1,5,10)
        self.automata = Automata(self.length, self.iterations, self.simulationGlobals)

    def test_future_mitotic_event(self):
        result = [self.automata.future_mitotic_event() for i in range(100)]
        for res in result:
            self.assertTrue(5 <= res <= 10)

    def test_pop_events(self):
        iteration = 5
        self.automata.mitotic_agenda[iteration] = "Event!"
        self.automata.pop_events(iteration)
        self.assertTrue(iteration in self.automata.mitotic_agenda)

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

    def copy_and_choose_new_position(self):
        self.automata.copy_and_choose_new_position(None)
        self.assertTrue(True)

    def test_boundary_cheking_True(self):
        result = self.automata.boundary_cheking((1,1,1))
        self.assertEqual(result, True)

    def test_boundary_cheking_False(self):
        result = self.automata.boundary_cheking((0,1,1))
        self.assertEqual(result, False)

    def test_first_test_True(self):
        result = self.automata.first_test(Cell((0,0,0),1,0,0,0,0,0,0))
        self.assertEqual(result, True)

    def test_first_test_False(self):
        result = self.automata.first_test(Cell((0,0,0),0,0,0,0,0,0,0))
        self.assertEqual(result, False)

    def test_third_test_True(self):
        result = self.automata.third_test(Cell((0,0,0),0,0,0,1,0,50,0))
        self.assertEqual(result, True)

    def test_third_test_False(self):
        result = self.automata.third_test(Cell((0,0,0),0,0,0,0,0,0,0))
        self.assertEqual(result, False)

    def test_copy_and_choose_new_position(self):
        position = (int(self.length/2),int(self.length/2),int(self.length/2))
        cell = self.automata.cells[position]
        iteration = 1
        self.automata.copy_and_choose_new_position((0,0,0), cell, iteration)
        self.assertTrue(len(self.automata.cells) == 2)

    def test_run(self):
        self.automata.iterations = 1
        self.automata.run(False)
        self.assertTrue(0 <= len(self.automata.cells) <= 2)
