print("OOP_CIARBSIT_2A.LA#4")
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} is a {self.role} hero."

hero = Hero("Layla", "marksman")
print(hero)
