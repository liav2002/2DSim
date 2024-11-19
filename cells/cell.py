from typing import List

from enums.enums import EVENT, CELL_TYPE
from looger.file_logger import FileLogger
from observers.observable import Observable
from data_collector.data_collector import DataCollector


class Cell(Observable):
    def __init__(self, y: int, x: int, cell_type: str, file_logger_observer: FileLogger,
                 data_collector_observer: DataCollector, is_alive=True) -> None:
        super().__init__()
        self.add_observer(file_logger_observer)
        self.add_observer(data_collector_observer)
        self.is_alive = is_alive
        self.next_state = None
        self.cell_type = cell_type
        self.y = y
        self.x = x

    def kill(self) -> None:
        self.is_alive = False

        if self.cell_type == CELL_TYPE["Plant"]:
            event = EVENT["PLANT_DIED"]

        elif self.cell_type == CELL_TYPE["Herbivore"]:
            event = EVENT["HERBIVORE_DIED"]

        elif self.cell_type == CELL_TYPE["Predator"]:
            event = EVENT["PREDATOR_DIED"]

        else:
            raise Exception("You try to kill unknown cell type.")

        self.notify_observers((event, f"Cell {self.cell_type} at ({self.y}, {self.x}) died."))

    def revival(self) -> None:
        self.is_alive = True
        self.notify_observers((EVENT["CELL_REVIVAL"], f"Cell {self.cell_type} at ({self.y}, {self.x}) revived."))

    def update_state(self) -> None:
        if self.next_state == "kill":
            self.kill()
        elif self.next_state == "revival":
            self.revival()

    def determine_next_state(self, neighbors: list) -> None:
        raise Exception("Should have implemented this")


class MovableCell(Cell):
    def __init__(self, y: int, x: int, sight: int, cell_type: str, file_logger_observer: FileLogger,
                 data_collector_observer: DataCollector, is_alive=True) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type, file_logger_observer=file_logger_observer,
                         data_collector_observer=data_collector_observer)
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
