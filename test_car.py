import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestEngine(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 20000
        capuletengine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capuletengine.engine_should_be_serviced())
    
    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 20000
        capuletengine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capuletengine.engine_should_be_serviced())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 80000
        last_service_mileage = 20000
        capuletengine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(capuletengine.engine_should_be_serviced())
    
    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 70000
        last_service_mileage = 20000
        capuletengine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(capuletengine.engine_should_be_serviced())
    
    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = True
        stermanengine = SternmanEngine(warning_light_is_on)
        self.assertTrue(stermanengine.engine_should_be_serviced())

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        stermanengine = SternmanEngine(warning_light_is_on)
        self.assertFalse(stermanengine.engine_should_be_serviced())


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
