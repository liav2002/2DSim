import yaml
import time
import os

from typing import Tuple, List
from Cells.PlantCell import PlantCell
from Cells.BasicCell import BasicCell
from Grid import Grid
from Enums import *

with open('config/game_config.yaml', 'r') as file:
    game_config = yaml.safe_load(file)

with open('config/patterns.yaml', 'r') as file:
    patterns = yaml.safe_load(file)



ON_PYCHARM = game_config['ON_PYCHARM']
WIDTH = game_config['WIDTH']
HEIGHT = game_config['HEIGHT']
TOTAL_GENERATIONS = game_config['TOTAL_GENERATIONS']
DELAY_BETWEEN_GENERATIONS = game_config['DELAY_BETWEEN_GENERATIONS']

TEMPLATE_PATTERN = patterns['TEMPLATE_PATTERN']



grid = None


def initialize_game(grid_size: Tuple[int, int], pattern: List[List[str]]) -> None:
    global grid
    grid = Grid(width=grid_size[0], height=grid_size[1], cells_map=pattern)
    print_grid()
    print("Generation: 0.")
    input("press any key to start...")


def next_generation(_id: int) -> None:
    global grid
    grid.update_generation()
    print_grid()
    print(f"Generation: {_id}.")
    # input("DEBUG:press any key to continue...")


def print_grid() -> None:
    if not ON_PYCHARM:
        os.system("cls")
    else:
        print("\n" * 100)

    for row in grid.cells:
        for cell in row:
            print(chr(CELL_CHARACTER[cell.cell_type]) if cell.is_alive else chr(CELL_CHARACTER["Empty"]), end=" ")
        print("\n")


def run(generations: int, delay: float) -> None:
    for generation in range(generations):
        next_generation(_id = generation + 1)
        time.sleep(delay)

    print("\n\nDONE!\n\n")


def main():
    initialize_game(grid_size=(WIDTH, HEIGHT), pattern=TEMPLATE_PATTERN)
    run(generations=TOTAL_GENERATIONS, delay=DELAY_BETWEEN_GENERATIONS)


if __name__ == "__main__":
    main()
