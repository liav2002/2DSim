from Cells.Cell import Cell

class HerbivoreCell(Cell):
    def __init__(self, TTL, is_alive = True):
        super().__init__(is_alive)
        self.TTL = TTL
        self.type = "Herbivore"

    def determine_next_state(self, neighbors):
        raise Exception("Herbivore Cells is not implemented yet.")