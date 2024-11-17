import yaml
import time
import os

from typing import Tuple, List
from Cells.PlantCell import PlantCell
from Cells.BasicCell import BasicCell
from Grid import Grid
from Enums import *

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

ON_PYCHARM = config['ON_PYCHARM']
WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']
TOTAL_GENERATIONS = config['TOTAL_GENERATIONS']
DELAY_BETWEEN_GENERATIONS = config['DELAY_BETWEEN_GENERATIONS']
TEMPLATE_PATTERN = config['TEMPLATE_PATTERN']



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
    print(f"Generation: {_id + 1}.")
    input("DEBUG:press any key to continue...")


def print_grid() -> None:
    # if not ON_PYCHARM:
    #     os.system("cls")
    # else:
    #     print("\n" * 100)

    for row in grid.cells:
        for cell in row:
            print(CELL_CHARACTER[cell.cell_type] if cell.is_alive else ".", end=" ")
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
