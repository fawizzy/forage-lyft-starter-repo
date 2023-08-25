from tire.tire import Tire
from typing import List

class Carrigan(Tire):
    def __init__(self, sensor_values: List) -> None:
        self.sensor_values = sensor_values
    
    def need_servicing(self):
        max_value = max(self.sensor_values)
        if max_value >= 0.9:
            return True
        else:
            return False