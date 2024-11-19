import os
from datetime import datetime

from observers.data_collector_observer import DataCollectorObserver


class DataCollector(DataCollectorObserver):
    def __init__(self, data_dir: str):
        timestamp = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
        self.data_dir = f"{data_dir}/{timestamp}/"
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)


    def update(self, event: str):
        self.logger.info(event)
