import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interfaces_abs.abstract_blueprints import ApplianceBlueprint

class Fan(ApplianceBlueprint):
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)

    def set_speed(self, speed):
        if speed in (self.SLOW, self.MEDIUM, self.FAST):
            self.__speed = speed

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def set_on(self, on):
        self.__on = bool(on)

    def get_speed(self): return self.__speed
    def get_radius(self): return self.__radius
    def get_color(self): return self.__color
    def is_on(self): return self.__on

    def display_status(self):
        state = "ON" if self.__on else "OFF"
        print(f"Fan Status -> Speed: {self.__speed}, Radius: {self.__radius}, Color: {self.__color}, Power: {state}")