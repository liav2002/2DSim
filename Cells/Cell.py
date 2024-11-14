
class Cell:
    def __init__(self, is_alive = True):
        self.is_alive = is_alive

    def toggle_state(self):
        self.is_alive = not self.is_alive

    def determine_next_state(self, neighbors):
        raise Exception("Should have implemented this")