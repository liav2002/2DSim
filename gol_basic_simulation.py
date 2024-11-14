import yaml
import time
import os

from Cells.PlantCell import PlantCell
from Cells.BasicCell import BasicCell
from Grid import Grid

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

ON_PYCHARM = config['ON_PYCHARM']
WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']
TOTAL_GENERATIONS = config['TOTAL_GENERATIONS']
DELAY_BETWEEN_GENERATIONS = config['DELAY_BETWEEN_GENERATIONS']
TEMPLATE_PATTERN = config['TEMPLATE_PATTERN']

grid = None


def initialize_game(grid_size, pattern):
    global grid
    grid = Grid(grid_size[0], grid_size[1], pattern)
    print_grid()
    input("press any key to start...")


def next_generation():
    global grid
    grid.update_generation()
    print_grid()
    input("DEBUG:press any key to continue...")


def print_grid():
    if not ON_PYCHARM:
        os.system("cls")
    else:
        print("\n" * 100)

    for row in grid.cells:
        for cell in row:
            if type(cell) is BasicCell and cell.is_alive:
                print("0", end=" ")
            elif type(cell) is PlantCell:
                print("P", end=" ")
            else:
                print(".", end=" ")
        print("\n")


def run(generations, delay):
    for generation in range(generations):
        next_generation()
        time.sleep(delay)

    print("\n\nDONE!\n\n")


def main():
    initialize_game((WIDTH, HEIGHT), TEMPLATE_PATTERN)
    run(generations=TOTAL_GENERATIONS, delay=DELAY_BETWEEN_GENERATIONS)


if __name__ == "__main__":
    main()
