from typing import List
import random

import yaml

from cells.cell import Cell, MovableCell
from observers.observable import Observable
from looger.file_logger import FileLogger
from cells.cell_factory import CellFactory

with open('./config/game_config.yaml', 'r') as file:
    game_config = yaml.safe_load(file)

with open('config/cell_logic_config.yaml', 'r') as file:
    cell_config = yaml.safe_load(file)


class Grid(Observable):
    def __init__(self, width: int, height: int, cells_map: List[List[Cell]], file_logger_observer: FileLogger) -> None:
        super().__init__()
        self.add_observer(file_logger_observer)
        self.width = width
        self.height = height
        self.cells = []
        self.init_board(cells_map=cells_map)
        self.can_we_produce_herbivores = True
        self.cooldown_for_herbivores = cell_config["HERBIVORE"]["COOLDOWN_REPRODUCE_STEPS"]

    def init_board(self, cells_map: List[List[Cell]]):
        empty_cells_position = []
        num_of_plants = cell_config["PLANT"]["AMOUNT"]

        for y, row in enumerate(cells_map):
            cell_row = []
            for x, cell_type in enumerate(row):
                cell = CellFactory.create_cell(cell_type=cell_type, position=(y, x),
                                               file_logger_observer=self.observers[0])
                cell_row.append(cell)
                if not cell.is_alive: empty_cells_position.append((y, x))
            self.cells.append(cell_row)

        for _ in range(num_of_plants):
            chosen_empty_cell = random.choice(empty_cells_position)
            y, x = chosen_empty_cell
            self.cells[y][x] = CellFactory.create_cell(cell_type="Plant", position=(y, x),
                                                       file_logger_observer=self.observers[0])

    def get_neighbors(self, cell: Cell) -> List[Cell]:
        neighbors = []
        x, y = cell.x, cell.y

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        neighbors.append(self.cells[ny][nx])

        return neighbors

    def sub_grib_by_cell_sight(self, cell: Cell) -> List[List[Cell]]:
        if not isinstance(cell, MovableCell):
            raise ValueError("Only MovableCell instances can use this method.")

        x, y, sight = cell.x, cell.y, cell.sight
        start_row = max(0, y - sight)
        end_row = min(self.height, y + sight + 1)
        start_col = max(0, x - sight)
        end_col = min(self.width, x + sight + 1)

        sub_grid = [
            self.cells[row][start_col:end_col]
            for row in range(start_row, end_row)
        ]

        return sub_grid

    def swap_cells(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if not (0 <= x1 < self.width and 0 <= y1 < self.height):
            raise ValueError(f"Coordinates ({y1}, {x1}) are out of bounds.")
        if not (0 <= x2 < self.width and 0 <= y2 < self.height):
            raise ValueError(f"Coordinates ({y2}, {x2}) are out of bounds.")

        cell1 = self.cells[y1][x1]
        cell2 = self.cells[y2][x2]
        self.cells[y1][x1], self.cells[y2][x2] = cell2, cell1
        cell1.x, cell1.y = x2, y2
        cell2.x, cell2.y = x1, y1

    def update_generation(self) -> None:
        # loop for check for any updates on grid
        for row in self.cells:
            for cell in row:
                neighbors = self.get_neighbors(cell=cell)
                cell.determine_next_state(neighbors=neighbors)

                if isinstance(cell, MovableCell):
                    cell.determine_next_pos(sub_grid=self.sub_grib_by_cell_sight(cell=cell))

                if cell.cell_type == "Herbivore" and self.can_we_produce_herbivores:
                    cell.try_reproduce(neighbors=neighbors)

        # loop for doing all the updates we discovered on grid
        for row in self.cells:
            for cell in row:
                cell.update_state()

                if cell.cell_type == "Herbivore" and cell.next_state == "reproduce":
                    if self.can_we_produce_herbivores and cell.spawn_position is not None:
                        y, x = cell.spawn_position
                        self.cells[y][x] = CellFactory.create_cell(cell_type="Herbivore", position=(y, x),
                                                                   file_logger_observer=self.observers[0])
                        self.notify_observers(f"New Herbivore born at {cell.spawn_position}.")
                        cell.next_state = "none"
                        cell.spawn_position = None
                        self.can_we_produce_herbivores = False
                        self.cooldown_for_herbivores = cell_config["HERBIVORE"]["COOLDOWN_REPRODUCE_STEPS"]

                    elif self.cooldown_for_herbivores == 0:
                        self.can_we_produce_herbivores = True

                    else:
                        self.cooldown_for_herbivores -= 1

                if isinstance(cell, MovableCell) and cell.move:
                    self.swap_cells(x1=cell.x, y1=cell.y, x2=cell.next_x, y2=cell.next_y)
                    self.notify_observers(f"Cell {cell.cell_type} moved to ({cell.next_y}, {cell.next_x}).")
                    cell.reset_next_pos()
