import numpy as np

class Grid(object):

    def __init__(self, height, width, depth, first_cell):
        self.height = height
        self.width = width
        self.depth = depth
        self.grid = self.build()
        self.initialization(first_cell)

    def build(self):
        grid = np.empty((self.height,self.width,self.depth))
        grid = grid.astype(np.str_)
        grid.fill('')
        return grid

    def initialization(self, first_cell):
        self.grid[self.__middle__(self.height)][self.__middle__(self.width)][self.__middle__(self.depth)] = first_cell

    def filter_side_positions(self, origin, positions):
        pass

    def extract_cube_from_grid(self, positions):
        return [self.grid[x][y][x] for x,y,z in positions]

    """def classify_neighborhood(self, cube):
        neighbor = dict()
        neighbor['occupied'] = [cell.position for cell in cube if str(cell) != '']
        neighbor['empties'] = [cell.position for cell in cube if str(cell) == '']
        return neighbor"""

    def neighborhood(self, origin, radio):
        x0,y0,z0 = origin
        return [(i+x0,j+y0,k+z0) for i in range(-radio, radio+1) for j in range(-radio, radio+1) for k in range(-radio, radio+1) if (i+x0,j+y0,k+z0) != origin]

    def __middle__(self, value):
        return int(value/2)
