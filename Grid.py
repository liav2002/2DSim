import BasicCell
import numpy as np

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.zeros((self.width, self.height))

        if self.cells is None: self.initialized_random()

    def initialized_random(self, seed):
        pass

    def get_neighbors(self, cell):
        pass

    def update_generation(self):
        pass