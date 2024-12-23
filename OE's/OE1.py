class Hero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"{self.name} is a {self.role} hero with {self.damage_type} damage."

def describe_team(heroes):
    for hero in heroes:
        print(hero)

hero1 = Hero("Layla", "Marksman", "Physical")
hero2 = Hero("Gusion", "Assassin", "Magic")
hero3 = Hero("Tigreal", "Tank", "Physical")
hero4 = Hero("Nana", "Support", "Magic")
hero5 = Hero("Lancelot", "Assassin", "Physical")

team = [hero1, hero2, hero3, hero4, hero5]

describe_team(team)
