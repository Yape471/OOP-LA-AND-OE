print("OOP_CIARBSIT_2A.LA#9")
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"This car is a {self.brand}."
my_car = Car("Toyota")

print(my_car)

del my_car

try:
    print(my_car)
except NameError:
    print("The car object has been deleted.")