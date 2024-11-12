import time
from Grid import Grid

WIDTH = 10
HEIGHT = 10
TOTAL_GENERATIONS = 20
DELAY_BETWEEN_GENERATIONS = 0.5

grid = None


def initialize_game(grid_size, random_seed=None):
    global grid
    grid = Grid(grid_size[0], grid_size[1])
    grid.initialized_random(seed=random_seed)
    print_grid()


def next_generation():
    global grid
    grid.update_generation()
    print_grid()


def print_grid():
    for row in grid.cells:
        for cell in row:
            if cell.is_alive:
                print("█ ")
            else:
                print(". ")
        print("\n")


def run(generations, delay):
    for generation in range(generations):
        print(f"Generation {generation + 1}:")
        next_generation()
        time.sleep(delay)


def main():
    initialize_game((WIDTH, HEIGHT), random_seed=42)
    run(generations=TOTAL_GENERATIONS, delay=DELAY_BETWEEN_GENERATIONS)


if __name__ == "__main__":
    main()
