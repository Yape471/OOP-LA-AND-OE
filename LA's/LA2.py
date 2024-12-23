class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

hero_instance = Hero("Argus", "Fighter")

print(hero_instance.name)
print(hero_instance.role)