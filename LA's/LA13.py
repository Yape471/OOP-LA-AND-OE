print("OOP_CIARBSIT_2A.LA#13")
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        print(f"Name: {self.name}, Type: {self.type}")

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim

my_fish = Fish("Goldfish", "Aquatic", True)

print(f"Can swim: {my_fish.can_swim}")