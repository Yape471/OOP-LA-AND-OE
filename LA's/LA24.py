print("OOP_CIARBSIT_2A.LA#24")
from abc import ABC, abstractmethod

class GameCharacter(ABC):

    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")

class Wizard(GameCharacter):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

class Healer(GameCharacter):
    def attack(self):
        print("Casts healing spell on the party!")

warrior = Warrior()
mage = Wizard()
archer = Archer()
healer = Healer()

warrior.attack()
mage.attack()
archer.attack()
healer.attack()