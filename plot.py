import copy
from TFMSTGCA.cell import Cell
from TFMSTGCA.grid import Grid
from TFMSTGCA.analytics import Analytics

cells = {
            (0,0,0): Cell((0,0,0),0,0,0,0,0,50,10**5),
            (0,0,1): Cell((0,0,1),0,0,0,0,0,50,10**5),
            (0,1,0): Cell((0,1,0),1,0,0,0,0,50,10**5),
            (0,1,1): Cell((0,1,1),1,0,0,0,0,50,10**5),
            (1,0,0): Cell((1,0,0),0,1,0,0,0,50,10**5),
            (1,0,1): Cell((1,0,1),0,1,0,0,0,50,10**5),
            (1,1,0): Cell((1,1,0),0,0,1,0,0,50,10**5),
            (1,1,1): Cell((1,1,1),0,0,1,0,0,50,10**5),
            (0,0,2): Cell((0,0,2),0,0,0,1,0,50,10**5),
            (0,2,0): Cell((0,2,0),0,0,0,1,0,50,10**5),
            (0,2,2): Cell((0,2,2),0,0,0,0,1,50,10**5),
            (2,0,0): Cell((2,0,0),0,0,0,0,1,50,10**5),
            (2,0,2): Cell((2,0,2),1,1,1,1,1,50,10**5),
            (2,2,0): Cell((2,2,0),1,1,1,1,1,50,10**5),
            (5,5,5): Cell((5,5,5),0,1,1,1,1,50,10**5)
        }

iterations_cells = {
    10: copy.deepcopy(cells),
    20: copy.deepcopy(cells)
}

analytics = Analytics()

#analytics.plot_grid(cells.keys())
analytics.plot_grid_plotly(cells)

"""result = analytics.get_measurements(iterations_cells)
measure, mutations = result[0], result[1]

analytics.plot_cells(measure)

analytics.plot_health_vs_carcino(measure)

analytics.plot_mutations(mutations)"""
