# integration_test.py
import unittest
from main_script import AgriSense
class MockSoilSensor:
    def get_moisture(self):
        return 45  # Mocked moisture level from the sensor
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
