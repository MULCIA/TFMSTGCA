import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import plotly
import plotly.graph_objs as go
import numpy as np

class Analytics:

    """
        iterations_cells = {
            1:  {(0,0,0): Cell(...)},
            10: {(0,0,1): Cell(...)}
        }
    """
    def get_measurements(self, iteration_cells):
        measure = {
            'iterations': [],
            'cells': [],
            'healthy': [],
            'carcinogenic': []
        }
        mutation_measure = {
            'iterations': [],
            'sg': [],
            'igi': [],
            'ea': [],
            'ei': [],
            'gi': []
        }
        for iteration,cells in iteration_cells.items():
            iterations_measure = measure['iterations']
            iterations_measure.append(iteration)
            iterations_mutation = mutation_measure['iterations']
            iterations_mutation.append(iteration)
            analytics = self.sum_analytics_cells(cells)
            cells_length = measure['cells']
            cells_length.append(len(cells))
            healthy_length = measure['healthy']
            healthy_length.append(analytics[0])
            carcinogenic_length = measure['carcinogenic']
            carcinogenic_length.append(analytics[1])
            sg_length = mutation_measure['sg']
            sg_length.append(analytics[2])
            igi_length = mutation_measure['igi']
            igi_length.append(analytics[3])
            ea_length = mutation_measure['ea']
            ea_length.append(analytics[4])
            ei_length = mutation_measure['ei']
            ei_length.append(analytics[5])
            gi_length = mutation_measure['gi']
            gi_length.append(analytics[6])
        return (measure, mutation_measure)

    def plot_cells(self, measure):
        """
        measure = {
            'iterations': [1,2,3,4],
            'cells': [10,350,352,435],
            'healthy': [10,350,351,400],
            'carcinogenic': [0,0,1,35]
        }
        """
        plt.plot(measure['iterations'], measure['cells'])
        plt.show()

    def plot_health_vs_carcino(self, measure):
        """
        measure = {
            'iterations': [1,2,3,4],
            'cells': [10,350,352,435],
            'healthy': [10,350,351,400],
            'carcinogenic': [0,0,1,35]
        }
        """
        plt.plot(measure['iterations'], measure['healthy'], '-', measure['iterations'], measure['carcinogenic'], 'bs')
        plt.show()

    def plot_mutations(self, measure):
        """
        mutation_measure = {
            'iterations': [1,2,3,4],
            'sg': [0,0,1,25],
            'igi': [0,0,0,5],
            'ea': [0,0,0,5],
            'ei': [0,0,0,0],
            'gi': [0,0,0,0]
        }
        """
        plt.plot(
                    measure['iterations'], measure['sg'], '-',
                    measure['iterations'], measure['igi'], 'bs',
                    measure['iterations'], measure['ea'], 'g^',
                    measure['iterations'], measure['ei'], '-',
                    measure['iterations'], measure['gi'], 'bs',
                )
        plt.show()

    def plot_grid(self, cells_positions):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = [position[0] for position in cells_positions]
        y = [position[1] for position in cells_positions]
        z = [position[2] for position in cells_positions]
        ax.scatter(x, y, z, zdir='z', c='red')
        plt.show()

    def plot_grid_plotly(self, cells_positions):
        x = [position[0] for position in cells_positions]
        y = [position[1] for position in cells_positions]
        z = [position[2] for position in cells_positions]

        c = [value for value in range(32)]

        trace1 = go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=24,
                color=c[::-1],        # set color to an array/list of desired values
                colorscale='Viridis',   # choose a colorscale
                opacity=0.8
            )
        )

        data = [trace1]
        layout = go.Layout(
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='3d-scatter-colorscale')

    def sum_analytics_cells(self, cells):
        cont_healty, cont_carcinogenic, cont_sg, cont_igi, cont_ea, cont_ei, cont_gi = 0,0,0,0,0,0,0
        for _,cell in cells.items():
            if str(cell) == '00000':
                cont_healty += 1
            else:
                cont_carcinogenic += 1
            if cell.genome.sg:
                cont_sg += 1
            if cell.genome.igi:
                cont_igi += 1
            if cell.genome.ea:
                cont_ea += 1
            if cell.genome.ei:
                cont_ei += 1
            if cell.genome.gi:
                cont_gi += 1
        return (cont_healty, cont_carcinogenic, cont_sg, cont_igi, cont_ea, cont_ei, cont_gi)

    def pretty_show(self, iteration, cells):
        print('Iteracion: ' + str(iteration))
        print('Numero total de celulas: ' + str(len(cells)))
        print('Celulas cancerosas: ' + str(self.sum_carcinogenic_cells(cells)))
        print('>>>>>>>')
