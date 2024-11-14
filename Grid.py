from Cells.CellFactory import CellFactory
from Enums import *
import yaml
import random

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


class Grid:
    def __init__(self, width, height, cells_map):
        self.width = width
        self.height = height
        self.cells = []
        self.init_board(cells_map)

    def init_board(self, cells_map):
        empty_cells_position = []
        num_of_plants = config['NUM_OF_PLANTS']

        for y, row in enumerate(cells_map):
            cell_row = []
            for x, cell_type in enumerate(row):
                cell = CellFactory.create_cell(cell_type)
                cell_row.append(cell)
                if not cell.is_alive: empty_cells_position.append((y, x))
            self.cells.append(cell_row)

        for _ in range(num_of_plants):
            chosen_empty_cell = random.choice(empty_cells_position)
            y, x = chosen_empty_cell
            self.cells[y][x] = CellFactory.create_cell(cell_type="Plant")

    def get_neighbors(self, cell):
        neighbors = []
        x, y = self.get_cell_position(cell)

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbors.append(self.cells[ny][nx])

        return neighbors

    def get_cell_position(self, cell):
        x = -1
        y = -1

        for y, row in enumerate(self.cells):
            if cell in row:
                x = row.index(cell)
                break

        if x == -1 or y == -1:
            raise Exception("ERROR <grid.get_cell_position()>: Cells not found")

        return x, y

    def update_generation(self):
        for row in self.cells:
            for cell in row:
                neighbors = self.get_neighbors(cell)
                cell.determine_next_state(neighbors)

        for row in self.cells:
            for cell in row:
                cell.update_state()
