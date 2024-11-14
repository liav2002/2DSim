from Cells.Cell import Cell

class HerbivoreCell(Cell):
    def __init__(self, is_alive):
        super().__init__(is_alive)

    def determine_next_state(self, neighbors):
        raise Exception("Herbivore Cells is not implemented yet.")