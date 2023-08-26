
import unittest
from main_script import AgriSense
class TestAgriSense(unittest.TestCase):
    def setUp(self):
        self.agrisense = AgriSense()
    def test_get_real_time_soil_moisture(self):
        moisture = self.agrisense.get_real_time_soil_moisture()
        self.assertTrue(0 <= moisture <= 100, "Soil moisture level should be between 0% and 100%.")
def test_provide_irrigation_advice(self):
    self.agrisense.soil_moisture_level = 30  # Simulate a moisture level below 40%
    advice_dry = self.agrisense.provide_irrigation_advice()

    self.agrisense.soil_moisture_level = 50  # Simulate a moisture level above 40%
    advice_adequate = self.agrisense.provide_irrigation_advice()

    self.assertNotEqual(advice_dry, advice_adequate, "Advice should differ based on moisture level.")

if __name__ == "__main__":
    unittest.main()
