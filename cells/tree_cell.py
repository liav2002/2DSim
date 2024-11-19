from typing import List

from cells.cell import Cell
from enums.enums import CELL_TYPE
from looger.file_logger import FileLogger
from data_collector.data_collector import DataCollector

class TreeCell(Cell):
    def __init__(self, y: int, x: int, file_logger_observer: FileLogger, data_collector_observer: DataCollector,
                 is_alive=True, cell_type=CELL_TYPE["Tree"]) -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, cell_type=cell_type,
                         file_logger_observer=file_logger_observer,
                         data_collector_observer=data_collector_observer)

    def determine_next_state(self, neighbors: List[Cell]):
        raise Exception("Tree cells is not implemented yet.")
