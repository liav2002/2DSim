from logger.observable import Observable
from typing import List

class Cell(Observable):
    def __init__(self, y: int, x: int, cell_type: str, is_alive=True) -> None:
        super().__init__()
        self.is_alive = is_alive
        self.next_state = None
        self.cell_type = cell_type
        self.y = y
        self.x = x

    def kill(self) -> None:
        self.is_alive = False
        self.notify_observers(f"Cell {self.cell_type} at ({self.y}, {self.x}) died.")

    def revival(self) -> None:
        self.is_alive = True
        self.notify_observers(f"Cell {self.cell_type} at ({self.y}, {self.x}) revived.")

    def update_state(self) -> None:
        if self.next_state == "kill":
            self.kill()
        elif self.next_state == "revival":
            self.revival()

    def determine_next_state(self, neighbors: list) -> None:
        raise Exception("Should have implemented this")


class MovableCell(Cell):
    def __init__(self, y: int, x: int, sight: int, cell_type: str, is_alive=True) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type)
        self.sight = sight
        self.next_x = -1
        self.next_y = -1
        self.move = False

    def reset_next_pos(self) -> None:
        self.next_x = -1
        self.next_y = -1
        self.move = False

    def determine_next_pos(self, sub_grid: List[List[Cell]]) -> None:
        raise Exception("Should have implemented this")
