print("OOP_CIARBSIT_2A.LA#6")
class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def laptop_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

my_laptop = Laptop("Dell", "XPS 13")

my_laptop.laptop_info()

print(my_laptop.laptop_info)