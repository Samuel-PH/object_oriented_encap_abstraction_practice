from abc import ABC, abstractmethod

class ApplianceBlueprint(ABC):
    @abstractmethod
    def display_status(self):
        pass

class VehicleBlueprint(ABC):
    @abstractmethod
    def accelerate(self):
        pass
        
    @abstractmethod
    def brake(self):
        pass