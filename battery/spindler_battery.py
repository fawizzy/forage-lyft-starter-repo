from battery.battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date) -> None:
        self.current_date = datetime.now()
        self.last_service_date: datetime = last_service_date
        

    def battery_should_be_serviced(self):
        return self.current_date.year - self.last_service_date.year >= 2