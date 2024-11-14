
class Cell:
    def __init__(self, is_alive = True):
        self.is_alive = is_alive

    def kill(self):
        self.is_alive = False

    def revival(self):
        self.is_alive = True

    def determine_next_state(self, neighbors):
        raise Exception("Should have implemented this")