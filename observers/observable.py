from typing import Tuple

class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, event: Tuple[int, int]):
        for observer in self.observers:
            observer.update(event)
