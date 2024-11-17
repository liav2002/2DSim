from typing import List
from Cells.Cell import Cell


class RockCell(Cell):
    def __init__(self, y: int, x: int, is_alive=True) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x)
        self.type = "Rock"

    def determine_next_state(self, neighbors: List[Cell]):
        raise Exception("Rock Cells is not implemented yet.")
