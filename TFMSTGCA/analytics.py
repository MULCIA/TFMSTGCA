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

        plt.plot(measure['iterations'], measure['healthy'],'b-', label='Células sanas')
        plt.plot(measure['iterations'], measure['carcinogenic'],'r--', label='Células cancerosas')

        plt.legend(loc='upper center')

        #plt.plot(measure['iterations'], measure['healthy'], 'b-', measure['iterations'], measure['carcinogenic'], 'r--')

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

        plt.plot(measure['iterations'], measure['sg'], 'o-', label='SG')
        plt.plot(measure['iterations'], measure['igi'], 'g--', label='IGI')
        plt.plot(measure['iterations'], measure['ea'], 'r--', label='EA')
        plt.plot(measure['iterations'], measure['ei'], 'b-', label='EI')
        plt.plot(measure['iterations'], measure['gi'], 'k:', label='GI')

        plt.legend(loc='upper center')


        """plt.plot(
                    measure['iterations'], measure['sg'], 'o-',
                    measure['iterations'], measure['igi'], 'g--',
                    measure['iterations'], measure['ea'], 'r--',
                    measure['iterations'], measure['ei'], 'b-',
                    measure['iterations'], measure['gi'], 'k:',
                )"""

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
        h_x, h_y, h_z, c_x, c_y, c_z = [], [], [], [], [], []
        for position, cell in cells_positions.items():
            if str(cell) == '00000':
                h_x.append(position[0])
                h_y.append(position[1])
                h_z.append(position[2])
            else:
                c_x.append(position[0])
                c_y.append(position[1])
                c_z.append(position[2])

        trace_healthy = go.Scatter3d(
            x=h_x,
            y=h_y,
            z=h_z,
            name='Células sanas',
            mode='markers',
            marker=dict(
                size=8,
                color='rgb(217, 217, 217)',
                opacity=0.8
            )
        )

        trace_cancer = go.Scatter3d(
            x=c_x,
            y=c_y,
            z=c_z,
            mode='markers',
            name='Células cancerosas',
            marker=dict(
                size=8,
                color='rgb(1, 83, 0)',
                opacity=0.8
            )
        )

        data = [trace_healthy, trace_cancer]
        layout = go.Layout(
            margin=dict(
                l=0,
                r=0,
                b=0,
                t=0
            )
        )
        fig = go.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='experiments-result')

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
        result = self.sum_analytics_cells(cells)
        print('Celulas cancerosas: ' + str(result[1]))
        print('>>>>>>>')
