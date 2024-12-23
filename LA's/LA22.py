print("OOP_CIARBSIT_2A.LA#21")
class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.__ingredients = ingredients

    def __str__(self):
        return f"{self.name} is made with: {', '.join(self.__ingredients)}"

    def get_ingredients(self):
        return self.__ingredients

    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients

pizza = FavoriteFood("Pizza", ["dough", "tomato sauce", "cheese", "pepperoni"])
sushi = FavoriteFood("Sushi", ["rice", "seaweed", "fish", "avocado"])
tacos = FavoriteFood("Tacos", ["tortilla", "beef", "lettuce", "cheese", "salsa"])

print(pizza)
print(sushi)
print(tacos)

print(pizza.get_ingredients())

pizza.set_ingredients(["dough", "tomato sauce", "mozzarella", "basil"])
print(pizza)