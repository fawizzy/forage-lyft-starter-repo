import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine



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


    





if __name__ == '__main__':
    unittest.main()
