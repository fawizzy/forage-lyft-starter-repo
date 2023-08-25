import unittest
from datetime import datetime
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime


class TestTire(unittest.TestCase):
    def test_carrigan_need_servicing(self):
        tire_sensor_values = [1, 1, 1, 1]
        carrigan = Carrigan(tire_sensor_values)
        self.assertTrue(carrigan.need_servicing())
    
    def test_carrigan_not_need_servicing(self):
        tire_sensor_values = [0, 0, 0, 0]
        carrigan = Carrigan(tire_sensor_values)
        self.assertFalse(carrigan.need_servicing())

    def test_octoprime_need_servicing(self):
        tire_sensor_values = [1, 1, 1, 0]
        octoprime = Octoprime(tire_sensor_values)
        self.assertTrue(octoprime.need_servicing())
    
    def test_octoprime_not_need_servicing(self):
        tire_sensor_values = [1, 1, 0, 0]
        octoprime = Octoprime(tire_sensor_values)
        self.assertFalse(octoprime.need_servicing())



if __name__ == '__main__':
    unittest.main()
