from Cells.Cell import Cell

class TreeCell(Cell):
    def __init__(self, is_alive = True):
        super().__init__(is_alive)

    def determine_next_state(self, neighbors):
        raise Exception("Tree Cells is not implemented yet.")