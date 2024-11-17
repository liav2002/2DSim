from typing import List, Tuple
from Cells.cell import *
import random


class PredatorCell(MovableCell):
    def __init__(self, TTL: int, y: int, x: int, sight: int, is_alive=True, cell_type="Predator") -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, sight=sight, cell_type=cell_type)
        self.TTL = TTL

    def determine_next_state(self, neighbors: List[Cell]):
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"
                return

    def determine_next_pos(self, sub_grid: List[List[Cell]]) -> None:
        self.move = True
        valid_moves = self.get_valid_moves(sub_grid)
        herbivores_moves = self.find_herbivores_moves(sub_grid, valid_moves)

        if herbivores_moves:
            self.next_y, self.next_x = random.choice(herbivores_moves)
        else:
            self.next_y, self.next_x = random.choice(valid_moves)

    def get_valid_moves(self, sub_grid: List[List[Cell]]) -> List[Tuple[int, int]]:
        moves = [
            (self.y - 1, self.x),
            (self.y + 1, self.x),
            (self.y, self.x - 1),
            (self.y, self.x + 1),
            (self.y - 1, self.x - 1),
            (self.y - 1, self.x + 1),
            (self.y + 1, self.x - 1),
            (self.y + 1, self.x + 1)
        ]

        valid_moves = [
            (row, col) for row, col in moves
            if 0 <= row < len(sub_grid) and 0 <= col < len(sub_grid[0]) and (
                        not sub_grid[row][col].is_alive or sub_grid[row][col].cell_type == "Plant")
        ]

        return valid_moves

    @staticmethod
    def find_herbivores_moves(sub_grid: List[List[Cell]], valid_moves: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        herbivores_moves = []
        closest_distance = float('inf')

        for move_y, move_x in valid_moves:
            for row_idx, row in enumerate(sub_grid):
                for col_idx, cell in enumerate(row):
                    if cell.cell_type == "Herbivore" and cell.is_alive:
                        # Calculate Manhattan distance to the plant
                        distance = abs(row_idx - move_y) + abs(col_idx - move_x)
                        if distance < closest_distance:
                            closest_distance = distance
                            herbivores_moves = [(move_y, move_x)]
                        elif distance == closest_distance:
                            herbivores_moves.append((move_y, move_x))

        return herbivores_moves
