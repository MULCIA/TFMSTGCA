import numpy as np
from .simulation_globals import SimulationGlobals

class Tests(object):

    def __init__(self, simulationGlobals = SimulationGlobals(10**5,50,10,10**2,30,10**3,0.95,5,10)):
        self.simulationGlobals = simulationGlobals

    """ 
        Test 1: muerte aleatoria de la célula, con probabilidad 1/a.
    """
    def random_death_test(self):
        if np.random.random() < 1/self.simulationGlobals.a:
            return True
        return False

    """
        Test 2: muerte por mutaciones, con n mutaciones sufridas tiene probabilidad de muerte n/e.
    """
    def genetic_damage_test(self, n, ea):
        #TODO: np.random.randint(0,n)
        if ea == 0 and np.random.random() < n/self.simulationGlobals.e:
            return True
        return False

    """
        Test 3: factor de crecimiento dentro de umbral 
    """
    def growth_factor_cheking(self, sg, spatial_boundary):
        if spatial_boundary > self.predefined_spatial_boundary and sg == 0:
            return False
        return True

    """
        Test 4: matar a un vecino, si el vecindario está completo, probabilidad de matar a un vecino 1/g.
    """
    def ignore_growth_inhibit_checking(self, is_neighborhood_full, igi):
        if is_neighborhood_full and igi == 1 and np.random.random() < 1/self.simulationGlobals.g:
            return True
        return False

    """
        Test 5: muerte por acortamiento de telomero. 
    """
    def limitless_replicative_potencial_checking(self, tl, ei):
        if tl == 0 and ei == 0:
            return True
        return False

    """
        Check if applicable mitotic event from Test 3 to Test 5 results.
    """
    def mitosis_test(self, checking_results):
        if checking_results == (True, False, False):
            return True
        return False