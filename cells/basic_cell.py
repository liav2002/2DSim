from typing import List
from cells.cell import Cell
from logger.file_logger import FileLogger

class BasicCell(Cell):
    def __init__(self, is_alive: bool, y: int, x: int, file_logger_observer: FileLogger, cell_type="Basic", is_reproducible = False) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type, file_logger_observer=file_logger_observer)
        self.is_reproducible = is_reproducible


    def determine_next_state(self, neighbors: List[Cell]) -> None:
        alive_neighbors = sum([1 for neighbor in neighbors if neighbor.is_alive])

        if self.is_alive and (alive_neighbors < 2 or alive_neighbors > 3):
                self.next_state = "kill"

        elif self.is_reproducible and not self.is_alive and alive_neighbors == 3:
            self.next_state = "revival"

        else:
            self.next_state = "none"
