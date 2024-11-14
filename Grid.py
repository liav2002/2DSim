from Cells.BasicCell import BasicCell
from Cells.HerbivoreCell import HerbivoreCell
from Cells.PlantCell import PlantCell
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
            for x, type in enumerate(row):
                if type == CELL_TYPE["Basic"]:
                    cell = BasicCell(is_alive=True)
                elif type == CELL_TYPE["Herbivore"]:
                    cell = HerbivoreCell(is_alive=True)
                else:
                    cell = BasicCell(is_alive=False)

                cell_row.append(cell)
                if not cell.is_alive: empty_cells_position.append((y, x))
            self.cells.append(cell_row)

        for _ in range(num_of_plants):
            chosen_empty_cell = random.choice(empty_cells_position)
            y, x = chosen_empty_cell
            self.cells[y][x] = PlantCell(is_alive=True, TTL=config["PLANTS_STEPS"])

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
        next_state = [[None for _ in range(self.width)] for _ in range(self.height)]

        for row in self.cells:
            for cell in row:
                neighbors = self.get_neighbors(cell)

                if type(cell) is PlantCell: cell_next = PlantCell(is_alive=True, TTL=config["PLANTS_STEPS"])
                else: cell_next = BasicCell(is_alive=cell.is_alive)

                cell_next.determine_next_state(neighbors)
                next_state[self.cells.index(row)][row.index(cell)] = cell_next

        self.cells = next_state
