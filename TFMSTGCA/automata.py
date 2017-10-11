import random
import numpy as np
from .simulation_globals import PREDEFINED_SPATIAL_BOUNDARY, NEIGHBORHOOD_RADIUS
from .experiments import Experiments
from .cell import Cell
from .grid import Grid

class Automata(object):

    def __init__(self, length, iterations, simulationGlobals):
        self.length = length
        self.size = self.length**3
        self.iterations = iterations+1
        self.simulationGlobals = simulationGlobals
        self.experiments = Experiments(simulationGlobals)
        position = (self.length//2,self.length//2,self.length//2)
        self.cells = {position: Cell(position, 0, 0, 0, 0, 0, self.simulationGlobals.tl, self.simulationGlobals.m)}
        self.mitotic_agenda = {self.future_mitotic_event(): [position]}
        self.grid = Grid(self.length, self.length, self.length)

    def future_mitotic_event(self):
        return np.random.randint(self.simulationGlobals.min_future_mitotic_event, self.simulationGlobals.max_future_mitotic_event+1)

    def push_event(self, iteration, event):
        if iteration in self.mitotic_agenda:
            events = self.mitotic_agenda[iteration]
            events.append(event)
            self.mitotic_agenda[iteration] = events
        else:
            self.mitotic_agenda[iteration] = [event]

    def pop_events(self, iteration):
        events = self.mitotic_agenda[iteration]
        del self.mitotic_agenda[iteration]
        return events

    def discard_event(self, position, origin):
        for iteration, positions in self.mitotic_agenda.items():
            if iteration > origin and position in positions:
                positions.remove(position)
                self.mitotic_agenda[iteration] = positions

    def kill_cell(self, position):
        del self.cells[position]

    def copy_and_choose_new_position(self, position, cell, iteration):
        neighborhood = self.grid.classify_neighborhood(self.grid.check_limits(self.grid.neighborhood(position, NEIGHBORHOOD_RADIUS), self.length), self.cells)
        new_position = random.choice(neighborhood['empties'])
        cell_copy = cell.perform_mitosis(new_position, self.simulationGlobals.i)
        self.push_event(iteration + self.future_mitotic_event(), cell_copy.position)
        self.cells[new_position] = cell_copy

    def boundary_cheking(self, position):
        delta = ((1-PREDEFINED_SPATIAL_BOUNDARY)*self.length)/2
        delta_origin, delta_boundary = (delta,delta,delta), (self.length-1-delta,self.length-1-delta,self.length-1-delta)
        return [True,True,True] == [delta_origin[pos] <= position[pos] <= delta_boundary[pos] for pos in range(3)]

    def first_test(self, cell):
        spatial_boundary = self.boundary_cheking(cell.position)
        return self.experiments.growth_factor_cheking(cell.genome.sg, spatial_boundary)

    def second_test(self, cell, iteration):
        neighborhood = self.grid.classify_neighborhood(self.grid.check_limits(self.grid.neighborhood(cell.position, 1), self.length), self.cells)
        is_neighborhood_full = False if len(neighborhood['empties']) > 0 else True
        if is_neighborhood_full:
            if self.experiments.ignore_growth_inhibit_checking(cell.genome.igi):
                candidate = random.choice(neighborhood['occupied'])
                self.discard_event(candidate, iteration)
                self.kill_cell(candidate) # Kill neighbor
                return True
            else:
                return False
        else:
            return True

    def third_test(self, cell):
        return self.experiments.limitless_replicative_potencial_checking(cell.tl, cell.genome.ei)

    """def cancer_cells(self, cells):
        cont = 0
        for position,cell in cells.items():
            if str(cell) != '00000':
                cont += 1
        return cont

    def cancer_full_cells(self, cells):
        cont = 0
        for position,cell in cells.items():
            if str(cell) == '11111':
                cont += 1
        return cont"""

    def run(self):
        for iteration in range(self.iterations):
            """if iteration%10 == 0:
                print('Iteracion: ' + str(iteration))
                print('Numero total de celulas: ' + str(len(self.cells)))
                print('Celulas cancerosas: ' + str(self.cancer_cells(self.cells)))
                print('Celulas con todas las mutaciones: ' + str(self.cancer_full_cells(self.cells)))
                print('>>>>>>>')"""
            events = self.pop_events(iteration) if iteration in self.mitotic_agenda else []
            for event in events: # event is a tuple with three elements == position
                cell = self.cells[event]
                if self.experiments.random_death_test():
                    self.kill_cell(event)
                elif self.experiments.genetic_damage_test(cell.mutations(), cell.genome.ea):
                    self.kill_cell(event)
                else:
                    test_1, test_2, test_3 = self.first_test(cell), self.second_test(cell, iteration), self.third_test(cell)
                    if test_1 and test_2 and test_3: #Perform mitosis
                        self.copy_and_choose_new_position(event, cell, iteration)
                        self.push_event(iteration + self.future_mitotic_event(), event)
                    elif test_3:
                        self.push_event(iteration + self.future_mitotic_event(), event)
                    else: # Telomer is 0 and EI is OFF
                        self.kill_cell(event)
