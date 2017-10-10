import random
import numpy as np
from .simulation_globals import PREDEFINED_SPATIAL_BOUNDARY
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
        self.cells = {}
        self.mitotic_agenda = {}
        self.grid = self.build()

    def build(self):
        position = (int(self.length/2),int(self.length/2),int(self.length/2))
        first_cell = Cell(position, 0, 0, 0, 0, 0, self.simulationGlobals.tl, self.simulationGlobals.m)
        self.cells[position] = first_cell
        grid = Grid(self.length, self.length, self.length, first_cell)
        self.mitotic_agenda[self.future_mitotic_event()] = [position]
        return grid

    def future_mitotic_event(self):
        return np.random.randint(self.simulationGlobals.min_future_mitotic_event, self.simulationGlobals.max_future_mitotic_event+1)

    def push_event(self, iteration, event):
        if iteration in self.mitotic_agenda:
            events = self.mitotic_agenda[iteration]
            """if event in events:
                print("Colisión!")"""
            events.append(event)
            self.mitotic_agenda[iteration] = events
        else:
            self.mitotic_agenda[iteration] = [event]

    def pop_events(self, iteration):
        events = self.mitotic_agenda[iteration]
        del self.mitotic_agenda[iteration]
        return events

    def kill_cell(self, position):
        del self.cells[position]
        self.grid.grid[position[0]][position[1]][position[2]] = ''

    def copy_and_choose_new_position(self, position, cell, iteration):
        # TODO: En self.grid.neighborhood(position, 1) poner 1 como constante en simulationGlobals
        neighborhood = self.grid.classify_neighborhood(self.grid.check_limits(self.grid.neighborhood(position, 1), self.length))
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

    def second_test(self, cell):
        neighborhood = self.grid.classify_neighborhood(self.grid.check_limits(self.grid.neighborhood(cell.position, 1), self.length))
        is_neighborhood_full = False if len(neighborhood['empties']) > 0 else True
        if is_neighborhood_full:
            return self.experiments.ignore_growth_inhibit_checking(cell.genome.igi)
        else:
            return True

    def third_test(self, cell):
        return self.experiments.limitless_replicative_potencial_checking(cell.tl, cell.genome.ei)

    def run(self):
        for iteration in range(self.iterations):
            events = self.pop_events(iteration) if iteration in self.mitotic_agenda else []
            for event in events: # event is a tuple with three elements == position
                cell = self.cells[event]
                if self.experiments.random_death_test():
                    """print(event)
                    print(cell)
                    print(str(events))
                    print("Muerte aleatoria!")
                    print(str(self.cells))"""
                    self.kill_cell(event)
                    #print(str(self.cells))
                elif self.experiments.genetic_damage_test(cell.mutations(), cell.genome.ea):
                    """print(event)
                    print(cell)
                    print(str(events))
                    print("Muerte por daño genético!")
                    print(str(self.cells))"""
                    self.kill_cell(event)
                    #print(str(self.cells))
                else:
                    test_1, test_2, test_3 = self.first_test(cell), self.second_test(cell), self.third_test(cell)
                    if test_1 and test_2 and test_3: #Perform mitosis
                        """
                            # TODO: Comprobar estos 5 pasos, ya que, los 4 primeros se hacen en 'copy_and_choose_new_position'.

                            1. Incrementar la tasa base de mutacion si el marcador GI esta presente.
                            2. ¿Hacer la division y mantener el genoma de la celula madre?
                            3. Añadir mutaciones a la nueva celula de acuerdo a la base de mutaciones base.
                            4. Decrementar en una unidad el telomero en ambas celulas.
                            5. Programar nuevo evento mitotico en el futuro para ambas celulas.
                        """
                        self.copy_and_choose_new_position(event, cell, iteration)
                        self.push_event(iteration + self.future_mitotic_event(), event)
                    elif test_3:
                        self.push_event(iteration + self.future_mitotic_event(), event)
                    else: # Telomer is 0 and EI is OFF
                        self.kill_cell(event)
