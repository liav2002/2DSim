import yaml
import time
import os

from logger.file_logger import FileLogger
from game_manager.grid import Grid
from enums.enums import *

with open('./config/game_config.yaml', 'r') as file:
    game_config = yaml.safe_load(file)

with open('./input/patterns.yaml', 'r') as file:
    patterns = yaml.safe_load(file)


class Game:
    def __init__(self):
        self.width = game_config['WIDTH']
        self.height = game_config['HEIGHT']
        self.total_generations = game_config['TOTAL_GENERATIONS']
        self.delay_between_generations = game_config['DELAY_BETWEEN_GENERATIONS']
        self.pattern = patterns['TEMPLATE_PATTERN']

        self.grid = Grid(width=self.width, height=self.height, cells_map=self.pattern,
                         file_logger_observer=FileLogger('./logs'))

        self.print_grid()
        print("Generation: 0.")
        input("press any key to start...")

    def next_generation(self, _id: int) -> None:
        self.grid.update_generation()
        self.print_grid()
        print(f"Generation: {_id}.")
        # input("DEBUG:press any key to continue...")

    def print_grid(self) -> None:
        print("\n" + " " * 50 + "=" * 60)
        for row in self.grid.cells:
            print(" " * 50, end="")
            for cell in row:
                print(chr(CELL_CHARACTER[cell.cell_type]) if cell.is_alive else chr(CELL_CHARACTER["Empty"]), end=" ")
            print("\n")
        print(" " * 50 + "=" * 60)

    def run(self) -> None:
        for generation in range(self.total_generations):
            self.next_generation(_id=generation + 1)
            time.sleep(self.delay_between_generations)

        print("\n\nDONE!\n\n")
