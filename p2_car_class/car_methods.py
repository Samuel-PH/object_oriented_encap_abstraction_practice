import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interfaces_abs.abstract_blueprints import VehicleBlueprint
class Car(VehicleBlueprint):
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed