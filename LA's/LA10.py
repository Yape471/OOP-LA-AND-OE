print("OOP_CIARBSIT_2A.LA#10")
class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Fuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car = Car("Toyota", "Corolla", "Gasoline")

motorcycle = Motorcycle("Honda", "CBR500R", "Tubig")

car.describeVehicle()
motorcycle.describeVehicle()