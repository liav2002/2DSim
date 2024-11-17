from typing import Tuple, List
from Cells.Cell import *
from Cells.CellFactory import CellFactory
from Enums import *
import yaml
import random

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


class Grid:
    def __init__(self, width: int, height: int, cells_map: List[List[Cell]]) -> None:
        self.width = width
        self.height = height
        self.cells = []
        self.init_board(cells_map=cells_map)

    def init_board(self, cells_map: List[List[Cell]]):
        empty_cells_position = []
        num_of_plants = config['NUM_OF_PLANTS']

        for y, row in enumerate(cells_map):
            cell_row = []
            for x, cell_type in enumerate(row):
                cell = CellFactory.create_cell(cell_type=cell_type, position=(y, x))
                cell_row.append(cell)
                if not cell.is_alive: empty_cells_position.append((y, x))
            self.cells.append(cell_row)

        for _ in range(num_of_plants):
            chosen_empty_cell = random.choice(empty_cells_position)
            y, x = chosen_empty_cell
            self.cells[y][x] = CellFactory.create_cell(cell_type="Plant", position=(y, x))

    def get_neighbors(self, cell: Cell) -> List[Cell]:
        neighbors = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    nx, ny = cell.x + dx, cell.y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbors.append(self.cells[ny][nx])

        return neighbors

    def sub_grib_by_cell_sight(self, cell: Cell) -> List[List[Cell]]:
        pass

    def swap_cells(self, x1: int, y1: int, x2: int, y2: int) -> None:
        pass

    def update_generation(self) -> None:
        for row in self.cells:
            for cell in row:
                neighbors = self.get_neighbors(cell=cell)
                cell.determine_next_state(neighbors=neighbors)
                if isinstance(cell, MovableCell):
                    cell.determine_next_pos(sub_grid=self.sub_grib_by_cell_sight(cell=cell))

        for row in self.cells:
            for cell in row:
                cell.update_state()

                # TODO: save current indexes and next indexes for movable cell
                # if isinstance(cell, MovableCell):
                    #self.swap_cells()
