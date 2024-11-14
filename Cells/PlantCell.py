from Cells.Cell import Cell
from Cells.HerbivoreCell import HerbivoreCell


class PlantCell(Cell):
    def __init__(self, is_alive, TTL):
        super().__init__(is_alive)
        self.TTL = TTL

    def determine_next_state(self, neighbors):
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.kill()
            elif any(isinstance(cell, HerbivoreCell) for cell in neighbors):
                self.kill()
