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
    def create_cell(cell_type: str) -> Cell:
        if cell_type == "Basic":
            return BasicCell(is_alive=True)
        elif cell_type == "Empty":
            return BasicCell(is_alive=False)
        elif cell_type == "Plant":
            return PlantCell(TTL=config["PLANTS_STEPS"])
        elif cell_type == "Herbivore":
            return HerbivoreCell(TTL=config["HERBIVORE_STEPS"])
        elif cell_type == "Predator":
            return PredatorCell(TTL=config["PREDATOR_STEPS"])
        elif cell_type == "Rock":
            return RockCell()
        elif cell_type == "Tree":
            return TreeCell()
        else:
            raise ValueError(f"Unknown cell type: {cell_type}")