from typing import List
from Cells.Cell import Cell

class BasicCell(Cell):
    def __init__(self, is_alive: bool, y: int, x: int, cell_type="Basic") -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type)


    def determine_next_state(self, neighbors: List[Cell]) -> None:
        alive_neighbors = sum([1 for neighbor in neighbors if neighbor.is_alive])

        if self.is_alive and (alive_neighbors < 2 or alive_neighbors > 3):
                self.next_state = "kill"

        elif not self.is_alive and alive_neighbors == 3:
            self.next_state = "revival"

        else:
            self.next_state = "none"
