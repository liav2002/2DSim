from typing import List

from cells.cell import Cell
from looger.file_logger import FileLogger


class PlantCell(Cell):
    def __init__(self, TTL: int, y: int, x: int, file_logger_observer: FileLogger, is_alive=True,
                 cell_type="Plant") -> None:
        super().__init__(y=y, x=x, is_alive=is_alive, cell_type=cell_type, file_logger_observer=file_logger_observer)
        self.TTL = TTL

    def determine_next_state(self, neighbors: List[Cell]) -> None:
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"
            elif any(cell.cell_type == "Herbivore" and cell.is_alive for cell in neighbors):
                self.notify_observers(f"Plant at ({self.y}, {self.x}) was eaten by Herbivore.")
                self.next_state = "kill"
            else:
                self.next_state = "none"
