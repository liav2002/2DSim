from Cells.Cell import *
from typing import List

class HerbivoreCell(MovableCell):
    def __init__(self, TTL: int, y: int, x: int, sight: int, is_alive = True) -> None:
        super().__init__(is_alive=is_alive,y=y ,x=x, sight=sight)
        self.TTL = TTL
        self.type = "Herbivore"

    def determine_next_state(self, neighbors: List[Cell]) -> None:
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"

    def determine_next_pos(self, sub_grid: List[List[Cell]]) -> None:
        pass