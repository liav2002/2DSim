
class Cell:
    def __init__(self, is_alive = True):
        self.is_alive = is_alive
        self.next_state = None

    def kill(self):
        self.is_alive = False

    def revival(self):
        self.is_alive = True

    def update_state(self):
        if self.next_state == "kill":
            self.kill()
        elif self.next_state == "revival":
            self.revival()

    def determine_next_state(self, neighbors):
        raise Exception("Should have implemented this")