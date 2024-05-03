from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Out of fuel, cannot start the vehicle.")



    def move(self, distance):
        # if not self.started:
        #     raise LowFuelError("Vehicle is not started.")

        # if self.fuel <= 0:
        #     raise LowFuelError("Out of fuel, cannot move the vehicle.")

        required_fuel = distance * self.fuel_consumption
        if required_fuel <= self.fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel("Not enough fuel to cover the distance.")
