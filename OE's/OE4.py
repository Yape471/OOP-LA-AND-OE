class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        damage = self.power
        target.health -= damage
        print(f"{self.name} attacked {target.name} for {damage} damage.")
        print(f"{target.name}'s remaining health: {target.health}")

    def special_move(self):
        pass

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.health -= reduced_damage
        print(f"{self.name} defended against {attacker.name}'s attack, reducing damage to {reduced_damage}.")
        print(f"{self.name}'s remaining health: {self.health}")

class Warrior(Character):
    def special_move(self):
        self.power *= 2
        print("Warrior uses Shield Bash! Attack power doubled for the next attack.")

class Mage(Character):
    def special_move(self, target):
        damage = 100
        target.health -= damage
        print("Mage casts Fireball! Deals 100 damage.")
        print(f"{target.name}'s remaining health: {target.health}")

class Archer(Character):
    def special_move(self, target):
        damage = self.power
        target.health -= damage
        print("Archer shoots a Piercing Arrow! Ignores defense and deals direct damage.")
        print(f"{target.name}'s remaining health: {target.health}")

class Monster(Character):
    def special_move(self):
        self.health += 50
        print("Monster roars and gains extra health! Health increased by 50.")
        print(f"{self.name}'s current health: {self.health}")

warrior = Warrior("Warrior", 200, 20)
mage = Mage("Mage", 150, 15)
archer = Archer("Archer", 180, 25)
monster = Monster("Monster", 300, 30)

characters = [warrior, mage, archer]

for character in characters:
    character.attack(monster)
    character.special_move(monster)
    monster.attack(character)
    monster.special_move()

for character in characters + [monster]:
    character.special_move()