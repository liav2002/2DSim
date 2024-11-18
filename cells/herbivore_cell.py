import random
from cells.cell import *
from typing import List, Optional, Tuple


class HerbivoreCell(MovableCell):
    def __init__(self, TTL: int, y: int, x: int, sight: int, is_alive=True, cell_type="Herbivore") -> None:
        super().__init__(is_alive=is_alive, y=y, x=x, sight=sight, cell_type=cell_type)
        self.TTL = TTL
        self.spawn_position = None

    def determine_next_state(self, neighbors: List[Cell]) -> None:
        if self.is_alive:
            self.TTL -= 1
            if self.TTL == 0:
                self.next_state = "kill"
                return
            elif any(cell.cell_type == "Predator" and cell.is_alive  for cell in neighbors):
                print(f"DEBUG: Predator eat Herbivore at ({self.y}, {self.x})")
                self.next_state = "kill"

    def try_reproduce(self, neighbors: List[Cell]) -> None:
        if any(cell.cell_type == "Herbivore" and cell.is_alive for cell in neighbors):
            empty_neighbors = [
                (neighbor.y, neighbor.x)
                for neighbor in neighbors
                if not neighbor.is_alive
            ]

            if empty_neighbors:
                spawn_position = random.choice(empty_neighbors)
                self.next_state = "reproduce"
                self.spawn_position = spawn_position  # Store where the new herbivore will spawn

            else:
                self.next_state = "none"

        else:
            return

    def determine_next_pos(self, sub_grid: List[List[Cell]]) -> None:
        self.move = True
        valid_moves = self.get_valid_moves(sub_grid)
        plant_moves = self.find_plant_moves(sub_grid, valid_moves)

        if plant_moves:
            self.next_y, self.next_x = random.choice(plant_moves)
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
            if 0 <= row < len(sub_grid) and 0 <= col < len(sub_grid[0]) and not sub_grid[row][col].is_alive
        ]

        return valid_moves

    @staticmethod
    def find_plant_moves(sub_grid: List[List[Cell]], valid_moves: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        plant_moves = []
        closest_distance = float('inf')

        for move_y, move_x in valid_moves:
            for row_idx, row in enumerate(sub_grid):
                for col_idx, cell in enumerate(row):
                    if cell.cell_type == "Plant" and cell.is_alive:
                        # Calculate Manhattan distance to the plant
                        distance = abs(row_idx - move_y) + abs(col_idx - move_x)
                        if distance < closest_distance:
                            closest_distance = distance
                            plant_moves = [(move_y, move_x)]
                        elif distance == closest_distance:
                            plant_moves.append((move_y, move_x))

        return plant_moves
