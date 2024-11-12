class Animals:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
    def look(self):
        print(f"The {self.age} y.o. animal weighs {self.weight} and looks around.")

    def breathe(self):
        print(f"The {self.age} y.o. animal weighs {self.weight} and breathes.")

class Fish(Animals):
    def swim(self):
        print(f"The {self.age} y.o. fish weighs {self.weight} and can swim.")

class Mammals(Animals):
    def run(self):
        print(f"The {self.age} y.o. mammal weighs {self.weight} and can run.")

class DomesticDog(Mammals):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print(f"My {self.age} y.o. {self.coat_color} {self.breed} weighs {self.weight} kg and barks.")

    def retrieve(self):
        print(f"My {self.age} y.o. {self.coat_color} {self.breed} weighs {self.weight} kg and retrieves.")

class Birds(Animals):
    def fly(self):
        print(f"The {self.age} y.o. bird weighs {self.weight} kg and can fly.")


my_dog = DomesticDog(10,8,"German boxer", "brindle" )
my_dog.bark()

my_bird = Birds(2, 15)
my_bird.fly()

generic_animal = Animals(150, 30)
generic_animal.breathe()





