from typing import Tuple

import yaml

from cells.cell import Cell
from cells.rock_cell import RockCell
from cells.tree_cell import TreeCell
from cells.basic_cell import BasicCell
from cells.plant_cell import PlantCell
from logger.file_logger import FileLogger
from cells.predator_cell import PredatorCell
from cells.herbivore_cell import HerbivoreCell

with open('config/cell_logic_config.yaml', 'r') as file:
    config = yaml.safe_load(file)


class CellFactory:
    @staticmethod
    def create_cell(cell_type: str, position: Tuple[int, int], file_logger_observer: FileLogger,
                    cell_state=True) -> Cell:
        if cell_type == "Basic":
            return BasicCell(is_alive=True, y=position[0], x=position[1], is_reproducible=False,
                             file_logger_observer=file_logger_observer)
        elif cell_type == "Empty":
            return BasicCell(is_alive=False, y=position[0], x=position[1], is_reproducible=False,
                             file_logger_observer=file_logger_observer)
        elif cell_type == "Plant":
            return PlantCell(TTL=config["PLANT"]["LIFE_STEPS"], is_alive=cell_state, y=position[0], x=position[1],
                             file_logger_observer=file_logger_observer)
        elif cell_type == "Herbivore":
            return HerbivoreCell(TTL=config["HERBIVORE"]["LIFE_STEPS"], is_alive=cell_state, y=position[0],
                                 x=position[1], sight=config["HERBIVORE"]["SIGHT"],
                                 file_logger_observer=file_logger_observer)
        elif cell_type == "Predator":
            return PredatorCell(TTL=config["PREDATOR"]["LIFE_STEPS"], is_alive=cell_state, y=position[0],
                                x=position[1], sight=config["PREDATOR"]["SIGHT"],
                                file_logger_observer=file_logger_observer)
        elif cell_type == "Rock":
            return RockCell(y=position[0], x=position[1], file_logger_observer=file_logger_observer)
        elif cell_type == "Tree":
            return TreeCell(y=position[0], x=position[1], file_logger_observer=file_logger_observer)
        else:
            raise ValueError(f"Unknown cell type: {cell_type}")
