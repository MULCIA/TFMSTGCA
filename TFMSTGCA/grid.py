import numpy as np

class Grid:

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

    def classify_neighborhood(self, cube):
        neighbor = dict()
        neighbor['occupied'] = [cell.position for cell in cube if str(cell) != '']
        neighbor['empties'] = [cell.position for cell in cube if str(cell) == '']
        return neighbor

    def interval(x, delta, cube_dimension):
        return [i for i in [-1, 0, 1] if x + 1 >= 1 + delta and x + i <= cube_dimension - 1 + delta]

    def neighborhood(self, origin):
        x0,y0,z0 = origin
        cube_positions = [(i+1,j+1,k+1) for i in interval(1, x0, cube_dimension) for j in interval(1, y0, cube_dimension) for k in interval(1, z0, cube_dimension) if (i,j,k) != (0,0,0)]
        cube = self.extract_cube_from_grid(self.filter_side_positions(origin, cube_positions))
        neighbor = classify_neighborhood(cube)
        return neighbor

    def __middle__(self, value):
        return int(value/2)