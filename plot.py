import copy
import matplotlib.pyplot as plt
from TFMSTGCA.cell import Cell
from TFMSTGCA.grid import Grid
from TFMSTGCA.analytics import Analytics

"""cells = {
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

measure = {
    'iterations': [100,200,300,400,500,600,700,800,900,1000],
    'all': [1000,32000,50000,82000,86000,95000,101000,108000,112000,118000],
    'sg': [1000,30000,65000,65000,68000,71000,76000,80000,83000,85000],
    'igi': [1000,40000,60000,65000,68000,70000,72000,74000,75000,77000],
    'ea': [1000,8000,25000,25000,20000,15000,15000,10000,5000,2000],
    'ei': [1000,43000,67000,75000,80000,85000,90000,100000,110000,112000],
    'gi': [1000,5000,10000,30000,35000,35000,40000,74000,70000,65000]
}

plt.plot(measure['iterations'], measure['all'], 'black', label='ALL')
plt.plot(measure['iterations'], measure['sg'], 'o-', label='SG')
plt.plot(measure['iterations'], measure['igi'], 'g--', label='IGI')
plt.plot(measure['iterations'], measure['ea'], 'r--', label='EA')
plt.plot(measure['iterations'], measure['ei'], 'b-', label='EI')
plt.plot(measure['iterations'], measure['gi'], 'k:', label='GI')

plt.legend(loc='best')

plt.show()

analytics = Analytics()

#analytics.plot_grid(cells.keys())
analytics.plot_grid_plotly(cells)

result = analytics.get_measurements(iterations_cells)
measure, mutations = result[0], result[1]

analytics.plot_cells(measure)

analytics.plot_health_vs_carcino(measure)

analytics.plot_mutations(mutations)"""
