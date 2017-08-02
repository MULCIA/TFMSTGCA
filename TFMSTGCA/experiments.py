import numpy as np

class Experiments(object):

    def __init__(self, simulationGlobals):
        self.simulationGlobals = simulationGlobals

    def random_death_test(self):
        if np.random.random() < 1/self.simulationGlobals.a:
            return True
        return False

    def genetic_damage_test(self, n, ea):
        if ea == 0 and np.random.random() < n/self.simulationGlobals.e:
            return True
        return False

    def growth_factor_cheking(self, sg, spatial_boundary):
        if spatial_boundary > self.simulationGlobals.predefined_spatial_boundary and sg == 0:
            return False
        return True

    def ignore_growth_inhibit_checking(self, igi):
        if igi == 1 and np.random.random() < 1/self.simulationGlobals.g:
            return True
        return False

    def limitless_replicative_potencial_checking(self, tl, ei):
        if tl == 0 and ei == 0:
            return False
        return True
