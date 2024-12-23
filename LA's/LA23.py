print("OOP_CIARBSIT_2A.LA#23")
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper():
            print("Introducing")
            func()
            print(f"{self.name} is pogi")
        return wrapper

guko = AnimeCharacter("Guko", "Kaio-Ken")

@guko.introduce
def character_intro():
    print(f"I am {guko.name} and I can use {guko.ability}.")

character_intro()