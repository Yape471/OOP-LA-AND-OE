print("OOP_CIARBSIT_2A.LA#17")
class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage.")
        print(f"{target.name}'s remaining health: {target.health}")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount} health points.")
        print(f"{self.name}'s current health: {self.health}")

player1 = Player("Knight", 100, 20)
player2 = Player("Dragon", 150, 25)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health > 0:
        player2.attack(player1)

if player1.health > 0:
    print(f"{player1.name} wins!")
else:
    print(f"{player2.name} wins!")