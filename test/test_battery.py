import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestBattery(unittest.TestCase):
    
    
    def test_nubbine_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year-4)
        nubbinbattery = NubbinBattery(last_service_date)
        self.assertTrue(nubbinbattery.battery_should_be_serviced())
    
    def test_nubbine_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year-3)
        nubbinbattery = NubbinBattery(last_service_date)
        self.assertFalse(nubbinbattery.battery_should_be_serviced())
    
    def test_spindler_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year-2)
        spindlerbattery = SpindlerBattery(last_service_date)
        self.assertTrue(spindlerbattery.battery_should_be_serviced())
    
    def test_spindler_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year-1)
        spindlerbattery = SpindlerBattery(last_service_date)
        self.assertFalse(spindlerbattery.battery_should_be_serviced())

if __name__ == '__main__':
    unittest.main()