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

analytics = Analytics()

analytics.plot_grid(cells.keys())
analytics.plot_grid_plotly(cells.keys())

measure = {
                'iterations': [1,2,3,4],
                'cells': [10,350,352,435],
                'healthy': [10,350,351,400],
                'carcinogenic': [0,0,1,35]
            }

analytics.plot_cells(measure)

analytics.plot_health_vs_carcino(measure)

mutations = {
                'iterations': [1,2,3,4],
                'sg': [0,0,1,25],
                'igi': [0,0,0,5],
                'ea': [0,0,0,5],
                'ei': [0,0,0,0],
                'gi': [0,0,0,0]
            }

analytics.plot_mutations(mutations)
