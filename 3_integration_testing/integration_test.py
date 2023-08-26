# integration_test.py
import unittest
from main_script import AgriSense
class MockSoilSensor:
    def __init__(self):
        self.moisture = 50  # Initial moisture level
    
    def get_moisture(self):
        self.moisture -= 1  # Decrease moisture level for simulation
        return self.moisture

class TestAgriSenseIntegration(unittest.TestCase):
    def setUp(self):
        self.agrisense = AgriSense()
        self.sensor = MockSoilSensor()
    def test_integration_with_sensor(self):
        sensor_moisture = self.sensor.get_moisture()
        agrisense_moisture = self.agrisense.get_real_time_soil_moisture()
        self.assertEqual(sensor_moisture, agrisense_moisture, "Moisture levels from AgriSense and sensor should match.")
if __name__ == "__main__":
    unittest.main()
