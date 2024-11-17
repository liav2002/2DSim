from typing import List
from Cells.cell import Cell

class TreeCell(Cell):
    def __init__(self, y: int, x: int, is_alive = True, cell_type="Tree") -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type)

    def determine_next_state(self, neighbors: List[Cell]):
        raise Exception("Tree Cells is not implemented yet.")
