import logging
from datetime import datetime

from observers.logger_observer import LoggerObserver


class FileLogger(LoggerObserver):
    def __init__(self, log_dir: str):
        timestamp = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
        log_file_path = f"{log_dir}/{timestamp}.log"
        logging.basicConfig(filename=log_file_path, level=logging.INFO)
        self.logger = logging.getLogger()

    def update(self, event: tuple):
        self.logger.info(event[1])
