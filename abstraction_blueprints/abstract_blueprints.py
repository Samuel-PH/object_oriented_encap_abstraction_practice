from abc import ABC, abstractmethod

class ApplianceBlueprint(ABC):
    @abstractmethod
    def display_status(self):
        pass

