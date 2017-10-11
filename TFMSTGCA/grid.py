import numpy as np

class Grid(object):

    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def filter(self, value, limit):
        if value >= 0 and value < limit:
            return True
        return False

    def check_limits(self, cube, limit):
        new_cube = list()
        for position in cube:
            x, y, z = position[0], position[1], position[2]
            if self.filter(x,limit) and self.filter(y,limit) and self.filter(z,limit):
                new_cube.append(position)
        return new_cube

    def classify_neighborhood(self, cube, cells):
        empties = list()
        occupied = list()
        neighbor = dict()
        for position in cube:
            if position in cells:
                empties.append(position)
            else:
                occupied.append(position)
        neighbor['occupied'] = occupied
        neighbor['empties'] = empties
        return neighbor

    def neighborhood(self, origin, radio):
        x0,y0,z0 = origin
        return [(i+x0,j+y0,k+z0) for i in range(-radio, radio+1) for j in range(-radio, radio+1) for k in range(-radio, radio+1) if (i+x0,j+y0,k+z0) != origin]
