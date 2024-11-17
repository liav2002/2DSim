from typing import Tuple
from Cells.Cell import Cell
from Cells.BasicCell import BasicCell
from Cells.HerbivoreCell import HerbivoreCell
from Cells.PlantCell import PlantCell
from Cells.PredatorCell import PredatorCell
from Cells.RockCell import RockCell
from Cells.TreeCell import TreeCell
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


class CellFactory:
    @staticmethod
    def create_cell(cell_type: str, position: Tuple[int, int], cell_state = True) -> Cell:
        if cell_type == "Basic":
            return BasicCell(is_alive=True, y=position[0], x=position[1], is_reproducible=False)
        elif cell_type == "Empty":
            return BasicCell(is_alive=False, y=position[0], x=position[1], is_reproducible=False)
        elif cell_type == "Plant":
            return PlantCell(TTL=config["PLANTS_STEPS"], is_alive=cell_state, y=position[0], x=position[1])
        elif cell_type == "Herbivore":
            return HerbivoreCell(TTL=config["HERBIVORE_LIFE_STEPS"], is_alive=cell_state, y=position[0], x=position[1], sight=config["HERBIVORE_SIGHT"])
        elif cell_type == "Predator":
            return PredatorCell(TTL=config["PREDATOR_LIFE_STEPS"], is_alive=cell_state, y=position[0], x=position[1], sight=config["PREDATOR_SIGHT"])
        elif cell_type == "Rock":
            return RockCell(y=position[0], x=position[1])
        elif cell_type == "Tree":
            return TreeCell(y=position[0], x=position[1])
        else:
            raise ValueError(f"Unknown cell type: {cell_type}")
