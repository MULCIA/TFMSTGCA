import matplotlib.pyplot as plt

class Analytics:

    def plot_cells(self, measure):
        """
        measure = {
            'iterations': [1,2,3,4],
            'cells': [10,350,352,435]
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
            'cells': [10,350,352,435]
            'healthy': [10,350,351,400],
            'carcinogenic': [0,0,1,35]
        }
        """
        plt.plot(measure['iterations'], measure['healthy'], '-', measure['iterations'], measure['carcinogenic'], 'bs')
        plt.show()

    def plot_mutations(self, measure):
        """
        measure = {
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

    def plot_grid(self, np_grid):
        pass

    def sum_healthy_cells(self, cells):
        cont = 0
        for _,cell in cells.items():
            if str(cell) == '00000':
                cont += 1
        return cont

    def sum_carcinogenic_cells(self, cells):
        cont = 0
        for _,cell in cells.items():
            if str(cell) != '00000':
                cont += 1
        return cont

    def sum_sg_mutations(self, cells):
        cont = 0
        for _,cell in cells.items():
            if cell.genome.sg:
                cont += 1
        return cont

    def sum_igi_mutations(self, cells):
        cont = 0
        for _,cell in cells.items():
            if cell.genome.igi:
                cont += 1
        return cont

    def sum_ea_mutations(self, cells):
        cont = 0
        for _,cell in cells.items():
            if cell.genome.ea:
                cont += 1
        return cont

    def sum_ei_mutations(self, cells):
        cont = 0
        for _,cell in cells.items():
            if cell.genome.ei:
                cont += 1
        return cont

    def sum_gi_mutations(self, cells):
        cont = 0
        for _,cell in cells.items():
            if cell.genome.gi:
                cont += 1
        return cont

    def pretty_show(self, iteration, cells):
        print('Iteracion: ' + str(iteration))
        print('Numero total de celulas: ' + str(len(cells)))
        print('Celulas cancerosas: ' + str(self.sum_carcinogenic_cells(cells)))
        print('>>>>>>>')
