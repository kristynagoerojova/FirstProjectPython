class Animal:
    total_weight = 0

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        Animal.total_weight += weight

    def look(self):
        print(f"The {self.age} y.o. animal weighs {self.weight} kg and looks around.")

    def breathe(self):
        print(f"The {self.age} y.o. animal weighs {self.weight} kg and breathes.")

    @classmethod
    def get_total_weight(cls):
        print(f"Total weigh of animals is {cls.total_weight}")

class Fish(Animal):
    def swim(self):
        print(f"The {self.age} y.o. fish weighs {self.weight} kg and can swim.")

class Mammal(Animal):
    def run(self):
        print(f"The {self.age} y.o. mammal weighs {self.weight} kg and can run.")

class DomesticDog(Mammal):
    def __init__(self, weight, age, breed, coat_color):
        super().__init__(weight, age)
        self.breed = breed
        self.coat_color = coat_color

    def bark(self):
        print(f"My {self.age} y.o. {self.coat_color} {self.breed} weighs {self.weight} kg and barks.")

    def retrieve(self):
        print(f"My {self.age} y.o. {self.coat_color} {self.breed} weighs {self.weight} kg and retrieves.")

class Bird(Animal):
    def fly(self):
        print(f"The {self.age} y.o. bird weighs {self.weight} kg and can fly.")


my_dog = DomesticDog(10,8,"German boxer", "brindle" )
# my_dog.bark()
#
my_bird = Bird(2, 15)
# my_bird.fly()

generic_animal = Animal(150, 30)
# generic_animal.breathe()

zvire = Animal(250, 30)

Animal.get_total_weight()







