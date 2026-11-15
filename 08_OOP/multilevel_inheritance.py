class Vehicle:
    def vehicle_info(self):
        print("This is a Vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a Car")

class ElectricCar(Car):
    def electric_info(self):
        print("This is an Electric Car")

obj = ElectricCar()

obj.vehicle_info()
obj.car_info()
obj.electric_info()
