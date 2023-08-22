# data_collection.py

import time
import random

def collect_data(filename="soil_moisture_data.txt"):
    with open(filename, 'a') as file:
        for _ in range(10):  # Simulate collecting data for 10 iterations
            moisture_level = random.randint(30, 60)  # Mocked moisture level from the sensor
            file.write(f"{time.ctime()}: {moisture_level}%\n")
            time.sleep(2)  # Wait for 2 seconds before collecting the next data point

if __name__ == "__main__":
    collect_data()
