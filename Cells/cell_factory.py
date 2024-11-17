from typing import Tuple
from Cells.cell import Cell
from Cells.basic_cell import BasicCell
from Cells.herbivore_cell import HerbivoreCell
from Cells.plant_cell import PlantCell
from Cells.predator_cell import PredatorCell
from Cells.rock_cell import RockCell
from Cells.tree_cell import TreeCell
import yaml

with open('config/plant_config.yaml', 'r') as file:
    plant_config = yaml.safe_load(file)

with open('config/herbivore_config.yaml', 'r') as file:
    herbivore_config = yaml.safe_load(file)

with open('config/predator_config.yaml', 'r') as file:
    predator_config = yaml.safe_load(file)




class CellFactory:
    @staticmethod
    def create_cell(cell_type: str, position: Tuple[int, int], cell_state = True) -> Cell:
        if cell_type == "Basic":
            return BasicCell(is_alive=True, y=position[0], x=position[1], is_reproducible=False)
        elif cell_type == "Empty":
            return BasicCell(is_alive=False, y=position[0], x=position[1], is_reproducible=False)
        elif cell_type == "Plant":
            return PlantCell(TTL=plant_config["PLANTS_STEPS"], is_alive=cell_state, y=position[0], x=position[1])
        elif cell_type == "Herbivore":
            return HerbivoreCell(TTL=herbivore_config["HERBIVORE_LIFE_STEPS"], is_alive=cell_state, y=position[0], x=position[1], sight=herbivore_config["HERBIVORE_SIGHT"])
        elif cell_type == "Predator":
            return PredatorCell(TTL=predator_config["PREDATOR_LIFE_STEPS"], is_alive=cell_state, y=position[0], x=position[1], sight=predator_config["PREDATOR_SIGHT"])
        elif cell_type == "Rock":
            return RockCell(y=position[0], x=position[1])
        elif cell_type == "Tree":
            return TreeCell(y=position[0], x=position[1])
        else:
            raise ValueError(f"Unknown cell type: {cell_type}")
