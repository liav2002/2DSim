from ctypes.macholib.dyld import dyld_find

from BasicCell import BasicCell


class Grid:
    def __init__(self, width, height, cells_map):
        self.width = width
        self.height = height

        self.cells = []
        for row in cells_map:
            cell_row = []
            for state in row:
                cell = BasicCell(is_alive=bool(state))
                cell_row.append(cell)
            self.cells.append(cell_row)

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
            raise Exception("ERROR <grid.get_cell_position()>: Cell not found")

        return x, y

    def update_generation(self):
        next_state = [[None for _ in range(self.width)] for _ in range(self.height)]

        for row in self.cells:
            for cell in row:
                neighbors = self.get_neighbors(cell)
                cell_next = BasicCell(is_alive=cell.is_alive)
                cell_next.determine_next_state(neighbors)
                next_state[self.cells.index(row)][row.index(cell)] = cell_next

        self.cells = next_state
