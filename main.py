from TFMSTGCA.simulation_globals import *
from TFMSTGCA.automata import Automata

if __name__ == "__main__":

    simulationGlobals = SimulationGlobals(BASE_MUTATION_RATE, TELOMER_LENGTH, EVADE_APOPTOSIS, FACTOR_INCREASE_BASE_RATE_MUTATION, KILL_NEIGHBOR_PROBABILITY, RANDOM_CELL_DEATH, PREDEFINED_SPATIAL_BOUNDARY, MIN_FUTURE_MITOTIC_EVENT, MAX_FUTURE_MITOTIC_EVENT)

    automata = Automata(50, 10, simulationGlobals)

    automata.run(False)
