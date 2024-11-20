import os
import time

import yaml
import pandas as pd
import matplotlib.pyplot as plt

from looger.file_logger import FileLogger
from enums.enums import CELL_CHARACTER, CELL_TYPE
from data_collector.data_collector import DataCollector
from game_manager.grid import Grid

with open('./config/game_config.yaml', 'r') as file:
    game_config = yaml.safe_load(file)

with open('./input/patterns.yaml', 'r') as file:
    patterns = yaml.safe_load(file)


class Game:
    def __init__(self):
        self.width = game_config['WIDTH']
        self.height = game_config['HEIGHT']
        self.total_generations = game_config['TOTAL_GENERATIONS']
        self.delay_between_generations = game_config['DELAY_BETWEEN_GENERATIONS']
        self.pattern = patterns['TEMPLATE_PATTERN']

        self.grid = Grid(width=self.width, height=self.height, cells_map=self.pattern,
                         file_logger_observer=FileLogger('./logs'), data_collector_observer=DataCollector("./data"))

        self.print_grid()
        print("Generation: 0.")
        input("press any key to start...")

    def next_generation(self, _id: int) -> None:
        self.grid.update_generation()
        self.print_grid()
        print(f"Generation: {_id}.")
        # input("DEBUG:press any key to continue...")

    def print_grid(self) -> None:
        print("\n" + " " * 50 + "=" * 60)
        for row in self.grid.cells:
            print(" " * 50, end="")
            for cell in row:
                print(chr(CELL_CHARACTER[cell.cell_type]) if cell.is_alive else chr(CELL_CHARACTER[CELL_TYPE["Empty"]]),
                      end=" ")
            print("\n")
        print(" " * 50 + "=" * 60)

    @staticmethod
    def generate_statistics(output_dir: str) -> None:
        # Identify the latest data folder
        data_dir = "./data"
        folders = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
        latest_folder = os.path.join(data_dir, sorted(folders)[-1]) if folders else None

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_dir = os.path.join(output_dir, latest_folder.split("\\")[1])
        print(f"DEBUG: output_dir = {output_dir}")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Read data from the CSV files
        events_file = os.path.join(latest_folder, "events.csv")
        generation_status_file = os.path.join(latest_folder, "generation_status.csv")
        events_data = pd.read_csv(events_file)
        generation_status_data = pd.read_csv(generation_status_file)

        # Plot 1: Number of alive organisms over time
        plt.figure(figsize=(10, 6))
        plt.plot(generation_status_data['generation_id'], generation_status_data['num_of_plants'], label='Plants')
        plt.plot(generation_status_data['generation_id'], generation_status_data['num_of_herbivores'],
                 label='Herbivores')
        plt.plot(generation_status_data['generation_id'], generation_status_data['num_of_predators'], label='Predators')
        plt.xlabel('Generation')
        plt.ylabel('Count')
        plt.title('Number of Alive Organisms Over Time')
        plt.legend()
        plt.grid()
        plt.savefig(os.path.join(output_dir, "alive_organisms_over_time.png"))
        plt.close()

        # Plot 2: Herbivore reproductions over time
        plt.figure(figsize=(10, 6))
        reproduction_counts = events_data.groupby('generation_id')['num_of_herbivores_reproduce'].sum()
        plt.plot(reproduction_counts.index, reproduction_counts.values, label='Herbivore Reproductions', color='green')
        plt.xlabel('Generation')
        plt.ylabel('Reproductions')
        plt.title('Herbivore Reproductions Over Time')
        plt.grid()
        plt.savefig(os.path.join(output_dir, "herbivore_reproductions.png"))
        plt.close()

        # Plot 3: Timeline of interesting events
        plt.figure(figsize=(10, 6))
        plt.stackplot(
            events_data['generation_id'],
            events_data['num_of_plants_eaten_by_herbivores'],
            events_data['num_of_herbivores_eaten_by_predators'],
            labels=['Plants Eaten by Herbivores', 'Herbivores Eaten by Predators']
        )
        plt.xlabel('Generation')
        plt.ylabel('Event Counts')
        plt.title('Timeline of Interesting Events')
        plt.legend()
        plt.grid()
        plt.savefig(os.path.join(output_dir, "interesting_events_timeline.png"))
        plt.close()

        print(f"Statistics and plots saved to '{output_dir}'.")

    def run(self) -> None:
        for generation in range(self.total_generations):
            self.next_generation(_id=generation + 1)
            time.sleep(self.delay_between_generations)

        print("\n\nDONE!\n\n")

        self.generate_statistics(output_dir="./output")
