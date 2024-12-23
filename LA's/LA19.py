print("OOP_CIARBSIT_2A.LA#19")
class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.__ingredients = ingredients

    def __str__(self):
        return f"{self.name} is made with: {', '.join(self.__ingredients)}"

pizza = FavoriteFood("Pizza", ["dough", "tomato sauce", "cheese", "pepperoni"])
sushi = FavoriteFood("Sushi", ["rice", "seaweed", "fish", "avocado"])
tacos = FavoriteFood("Tacos", ["tortilla", "beef", "lettuce", "cheese", "salsa"])

print(pizza)
print(sushi)
print(tacos)

try:
    print(pizza.__ingredients)
except AttributeError as e:
    print(e)