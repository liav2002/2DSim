import os
import csv
from typing import Tuple
from datetime import datetime

from enums.enums import EVENT
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

    def update_generations_status_file(self, event: str, file_path: str):
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = list(csv.reader(csv_file))
            last_row = reader[-1]

        new_row = last_row[:]

        # update date and time
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')
        new_row[0] = current_date
        new_row[1] = current_time

        # update generation_id
        new_row[2] = str(int(new_row[1]) + 1)

        # update other fields
        if event == EVENT['PLANT_DIED']:
            new_row[3] = str(int(new_row[3]) - 1)  # Decrease num_of_plants

        elif event == EVENT['HERBIVORE_DIED']:
            new_row[4] = str(int(new_row[4]) - 1)  # Decrease num_of_herbivores

        elif event == EVENT['PREDATOR_DIED']:
            new_row[5] = str(int(new_row[5]) - 1)  # Decrease num_of_predators

        elif event == EVENT['HERBIVORE_REPRODUCE']:
            new_row[4] = str(int(new_row[4]) + 1)  # Increase num_of_herbivores

        with open(self.file_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_row)

    def update_events_file(self, event: str, file_path: str):
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = list(csv.reader(csv_file))
            last_row = reader[-1]

        new_row = last_row[:]

        # update date and time
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')
        new_row[0] = current_date
        new_row[1] = current_time

        # update generation_id
        new_row[2] = str(int(new_row[1]) + 1)

        # update other fields
        if event == EVENT['PLANT_DIED']:
            new_row[3] = str(int(new_row[3]) + 1)  # Increase num_of_plants_died

        elif event == EVENT['HERBIVORE_DIED']:
            new_row[4] = str(int(new_row[4]) + 1)  # Increase num_of_herbivores_died

        elif event == EVENT['PREDATOR_DIED']:
            new_row[5] = str(int(new_row[5]) + 1)  # Increase num_of_predators_died

        elif event == EVENT['HERBIVORE_REPRODUCE']:
            new_row[4] = str(int(new_row[6]) + 1)  # Increase num_of_herbivores_reproduce

        with open(self.file_path, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_row)

    def update(self, event: Tuple[int, int]):
        events_file_path = f'{self.data_dir}/{EVENTS_DATA_FILE}'
        status_file_path = f'{self.data_dir}/{GENERATION_STATUS_DATA_FILE}'

        self.update_generations_status_file(event=event[0], file_path=status_file_path)
        self.update_events_file(event=event[0], file_path=events_file_path)
