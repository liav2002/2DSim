from typing import Tuple
from abc import ABC, abstractmethod


class LoggerObserver(ABC):
    @abstractmethod
    def update(self, event: Tuple[int, int]):
        pass
