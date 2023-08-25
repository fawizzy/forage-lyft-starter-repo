from tire.tire import Tire
from typing import List

class Octoprime(Tire):
    def __init__(self, sensor_values: List) -> None:
        self.sensor_values = sensor_values
    
    def need_servicing(self):
        sum_values = sum(self.sensor_values)
        if sum_values >= 3:
            return True
        else:
            return False
        