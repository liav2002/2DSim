from Cells.Cell import Cell

class PredatorCell(Cell):
    def __init__(self, TTL, is_alive = True):
        super().__init__(is_alive)
        self.TTL = TTL
        self.type = "Predator"

    def determine_next_state(self, neighbors):
        raise Exception("Predator Cells is not implemented yet.")