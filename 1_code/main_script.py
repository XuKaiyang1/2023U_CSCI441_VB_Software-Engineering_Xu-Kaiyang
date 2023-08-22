# main_script.py

import time

class AgriSense:
    def __init__(self):
        self.soil_moisture_level = 50  # Initial moisture level (%)

    def get_real_time_soil_moisture(self):
        # Simulate real-time soil moisture monitoring
        # In reality, you would get this data from a soil moisture sensor
        self.soil_moisture_level -= 1  # Decrease moisture level for simulation
        return self.soil_moisture_level

    def provide_irrigation_advice(self):
        if self.soil_moisture_level < 40:
            return "Soil is getting dry. Consider irrigating the crops soon."
        elif self.soil_moisture_level < 30:
            return "Soil is very dry! Irrigate the crops immediately."
        else:
            return "Soil moisture level is adequate."

    def main_loop(self):
        while True:
            print("\nChecking soil moisture level...")
            moisture = self.get_real_time_soil_moisture()
            print(f"Current soil moisture level: {moisture}%")
            advice = self.provide_irrigation_advice()
            print(advice)
            time.sleep(10)  # Check every 10 seconds for simulation

if __name__ == "__main__":
    agrisense = AgriSense()
    agrisense.main_loop()
