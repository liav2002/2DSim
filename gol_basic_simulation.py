import time
import os

from Grid import Grid

ON_PYCHARM = False
WIDTH = 20
HEIGHT = 11
TOTAL_GENERATIONS = 5
DELAY_BETWEEN_GENERATIONS = 0.5
TEMPLATE_PATTERN = [[False] * 20,
                    [False] * 20,
                    [False] * 20,
                    [False] * 7 + [True, False] * 3 + [False] * 7,
                    [False] * 6 + [True] + [False] * 5 + [True] + [False] * 7,
                    [False] * 5 + [True, False] * 2 + [False] * 2 + [True, False] * 2 + [False] * 5,
                    [False] * 6 + [True] + [False] * 5 + [True] + [False] * 7,
                    [False] * 7 + [True, False] * 3 + [False] * 7,
                    [False] * 20,
                    [False] * 20,
                    [False] * 20]

grid = None


def initialize_game(grid_size, pattern):
    global grid
    grid = Grid(grid_size[0], grid_size[1], pattern)
    print_grid()


def next_generation():
    global grid
    grid.update_generation()
    print_grid()


def print_grid():
    if not ON_PYCHARM:
        os.system("cls")
    else:
        print("\n" * 100)

    for row in grid.cells:
        for cell in row:
            if cell.is_alive:
                print("0", end=" ")
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
