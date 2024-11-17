from typing import List
from Cells.Cell import Cell
from Cells.HerbivoreCell import HerbivoreCell


class PlantCell(Cell):
    def __init__(self, TTL: int, y: int, x: int, is_alive = True) -> None:
        super().__init__(y=y, x=x, is_alive=is_alive)
        self.TTL = TTL
        self.type = "Plant"

    def determine_next_state(self, neighbors: List[Cell]) -> None:
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"
            elif any(isinstance(cell, HerbivoreCell) for cell in neighbors):
                self.next_state = "kill"
            else:
                self.next_state = "none"
