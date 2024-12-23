print("OOP_CIARBSIT_2A.LA#12")
class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        print(f"Toy Name: {self.name}, Price: ${self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

my_car = Car("Hot Wheels", 10.99)

my_car.display_details()