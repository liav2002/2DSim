from abc import ABC, abstractmethod


class DataCollectorObserver(ABC):
    @abstractmethod
    def update(self, event: str):
        pass