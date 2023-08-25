from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        pass
