from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class carFactory:
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery =SpindlerBattery(last_service_date)
        car = Car(battery, engine)
        return car
    
    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def create_pallindrome(last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        car = Car(battery, engine)
        return car
    
    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(battery, engine)
        return car
    
    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(battery, engine)
        return car  