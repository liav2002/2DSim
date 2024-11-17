from typing import List
from Cells.Cell import *

class PredatorCell(MovableCell):
    def __init__(self, TTL: int, y: int, x: int, sight: int, is_alive = True, cell_type="Predator") -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, sight=sight, cell_type=cell_type)
        self.TTL = TTL

    def determine_next_state(self, neighbors: List[Cell]):
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"
                return

    def determine_next_pos(self, sub_grid: List[List[Cell]]) -> None:
        pass