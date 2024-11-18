from typing import List
from cells.cell import Cell


class RockCell(Cell):
    def __init__(self, y: int, x: int, is_alive=True, cell_type="Rock") -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type)

    def determine_next_state(self, neighbors: List[Cell]):
        raise Exception("Rock cells is not implemented yet.")
