from typing import List
from Cells.Cell import *

class PredatorCell(MovableCell):
    def __init__(self, TTL: int, y: int, x: int, sight: int, is_alive = True) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, sight=sight)
        self.TTL = TTL
        self.type = "Predator"

    def determine_next_state(self, neighbors: List[Cell]):
        raise Exception("Predator Cells is not implemented yet.")