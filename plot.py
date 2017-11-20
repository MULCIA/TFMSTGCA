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
}"""

measure = {
    'iterations': [0,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000],
    'h': [125000,120000,120000,118000,117000,116500,115000,110000,108000,80000,42000,25000,10000,5000,5000,4000,1000,800,500,500,100],
    'c': [0,1000,1000,2700,3000,5000,6000,7000,7500,40000,80000,100000,110000,115000,118000,120000,122000,125000,125000,126000,127000]
}

plt.plot(measure['iterations'], measure['h'], 'b-', label='Células sanas')
plt.plot(measure['iterations'], measure['c'], 'r--', label='Células cancerosas')

"""measure = {
    'iterations': [50000,55000,60000,65000,70000,75000],
    'sg': [0,6000,33000,65000,113000,117000],
    'igi': [0,2000,6000,74000,121000,121000],
    'ea': [0,3000,4000,117000,120000,123000],
    'ei': [0,14000,65000,121000,124000,124000],
    'gi': [0,1000,1500,2300,2400,2600]
}

#plt.plot(measure['iterations'], measure['all'], 'black', label='ALL')
plt.plot(measure['iterations'], measure['sg'], 'o-', label='SG')
plt.plot(measure['iterations'], measure['igi'], 'g--', label='IGI')
plt.plot(measure['iterations'], measure['ea'], 'r--', label='EA')
plt.plot(measure['iterations'], measure['ei'], 'b-', label='EI')
plt.plot(measure['iterations'], measure['gi'], 'k:', label='GI')"""

plt.legend(loc='best')

plt.show()

"""analytics = Analytics()

#analytics.plot_grid(cells.keys())
analytics.plot_grid_plotly(cells)

result = analytics.get_measurements(iterations_cells)
measure, mutations = result[0], result[1]

analytics.plot_cells(measure)

analytics.plot_health_vs_carcino(measure)

analytics.plot_mutations(mutations)"""
