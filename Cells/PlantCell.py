from typing import List
from Cells.Cell import Cell


class PlantCell(Cell):
    def __init__(self, TTL: int, y: int, x: int, is_alive = True, cell_type="Plant") -> None:
        super().__init__(y=y, x=x, is_alive=is_alive, cell_type=cell_type)
        self.TTL = TTL

    def determine_next_state(self, neighbors: List[Cell]) -> None:
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"
            elif any(cell.cell_type == "Herbivore" for cell in neighbors):
                print(f"DEBUG: Herbivore eat Plant at ({self.y}, {self.x})")
                self.next_state = "kill"
            else:
                self.next_state = "none"
