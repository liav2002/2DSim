import os
import csv
from datetime import datetime
from consts.data_files import GENERATION_STATUS_DATA_FILE, EVENTS_DATA_FILE

from observers.data_collector_observer import DataCollectorObserver


class DataCollector(DataCollectorObserver):
    def __init__(self, data_dir: str):
        timestamp = datetime.now().strftime("%d-%m-%y_%H-%M-%S")
        self.data_dir = f"{data_dir}/{timestamp}/"
        self.init_data_dir()
        self.init_generations_status_file()
        self.init_events_file()

    def init_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def init_generations_status_file(self):
        file_path = f'{self.data_dir}/{GENERATION_STATUS_DATA_FILE}'
        if not os.path.exists(file_path):
            with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['date', 'time', 'generation_id', 'num_of_plants',
                                 'num_of_herbivores', 'num_of_predators'])

    def init_events_file(self):
        file_path = f'{self.data_dir}/{EVENTS_DATA_FILE}'
        if not os.path.exists(file_path):
            with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['date', 'time', 'generation_id', 'num_of_plants_died', 'num_of_herbivores_died',
                                 'num_of_predators_died', 'num_of_herbivores_reproduce'])

    def update(self, event: str):
        pass
