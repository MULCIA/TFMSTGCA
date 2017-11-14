from TFMSTGCA.simulation_globals import *
from TFMSTGCA.automata import Automata

if __name__ == "__main__":

    simulationGlobals = SimulationGlobals(100, TELOMER_LENGTH, EVADE_APOPTOSIS, FACTOR_INCREASE_BASE_RATE_MUTATION, KILL_NEIGHBOR_PROBABILITY, RANDOM_CELL_DEATH, PREDEFINED_SPATIAL_BOUNDARY, MIN_FUTURE_MITOTIC_EVENT, MAX_FUTURE_MITOTIC_EVENT)

    #simulationGlobals = SimulationGlobals(100000, 35, 20, 100, 10, 400, PREDEFINED_SPATIAL_BOUNDARY, MIN_FUTURE_MITOTIC_EVENT, MAX_FUTURE_MITOTIC_EVENT)

    automata = Automata(50, 8000, simulationGlobals)

    automata.run(True)
