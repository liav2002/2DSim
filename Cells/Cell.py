from typing import List

class Cell:
    def __init__(self, y: int, x: int, is_alive=True) -> None:
        self.is_alive = is_alive
        self.next_state = None
        self.y = y
        self.x = x

    def kill(self) -> None:
        self.is_alive = False

    def revival(self) -> None:
        self.is_alive = True

    def update_state(self) -> None:
        if self.next_state == "kill":
            self.kill()
        elif self.next_state == "revival":
            self.revival()

    def determine_next_state(self, neighbors: List[Cell]) -> None:
        raise Exception("Should have implemented this")


class MovableCell(Cell):
    def __init__(self, y: int, x: int, is_alive=True) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x)

    def determine_next_pos(self, sub_grid: List[List[Cell]]) -> None:
        raise Exception("Should have implemented this")
