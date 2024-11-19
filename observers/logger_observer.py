from abc import ABC, abstractmethod


class LoggerObserver(ABC):
    @abstractmethod
    def update(self, event: str):
        pass
