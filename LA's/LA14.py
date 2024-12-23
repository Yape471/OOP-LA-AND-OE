print("OOP_CIARBSIT_2A.LA#14")
class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

tobey_spiderman = Tobey("tobey", 46, "Spider-Man")
andrew_spiderman = Andrew("andrew", 40, "The Amazing Spider-Man")
tom_spiderman = Tom("tom", 28, "Spider-Man: Homecoming")

print(f"{tobey_spiderman.name.upper()} starred in {tobey_spiderman.movieTitle}")
print(f"{andrew_spiderman.name.upper()} starred in {andrew_spiderman.movieTitle}")
print(f"{tom_spiderman.name.upper()} starred in {tom_spiderman.movieTitle}")