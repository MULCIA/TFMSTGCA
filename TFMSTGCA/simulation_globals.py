# In each cell
BASE_MUTATION_RATE = 10**5 #TODO: Check if correct value is 10**5 or 10**(-5)
TELOMER_LENGTH = 50

# Global
EVADE_APOPTOSIS = 10
FACTOR_INCREASE_BASE_RATE_MUTATION = 10**2
KILL_NEIGHBOR_PROBABILITY = 30
RANDOM_CELL_DEATH = 10**3

# Growth factor
PREDEFINED_SPATIAL_BOUNDARY = 0.95 #TODO: Check this value. Other posibility is 0.858.

# Random parameters for generating future mitotic event
MIN_FUTURE_MITOTIC_EVENT = 5
MAX_FUTURE_MITOTIC_EVENT = 10

class SimulationGlobals(object):

    def __init__(self, base_mutation_rate, telomer_length, evade_apoptosis, factor_increase_base_rate_mutation, kill_neighbor, random_death, predefined_spatial_boundary, min_future_mitotic_event, max_future_mitotic_event):
        self.m = base_mutation_rate
        self.tl = telomer_length
        self.e = evade_apoptosis
        self.i = factor_increase_base_rate_mutation
        self.g = kill_neighbor
        self.a = random_death
        self.predefined_spatial_boundary = predefined_spatial_boundary
        self.min_future_mitotic_event = min_future_mitotic_event
        self.max_future_mitotic_event = max_future_mitotic_event
