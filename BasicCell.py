from Cell import Cell

class BasicCell(Cell):
    def __init__(self, is_alive):
        super().__init__(is_alive)

    def determine_next_state(self, neighbors):
        alive_neighbors = sum([1 for neighbor in neighbors if neighbor.is_alive()])

        if self.is_alive() and (alive_neighbors < 2 or alive_neighbors > 3):
                self.toggle_state() # change to die

        elif alive_neighbors == 3:
            self.toggle_state() # change to alive
