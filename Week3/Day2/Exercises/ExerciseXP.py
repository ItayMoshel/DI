class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal = Bengal("Ben", 10)
chartreux = Chartreux("Char", 8)
siamese = Siamese("Siam", 6)
all_cats = [bengal, chartreux, siamese]

saras_pets = Pets(all_cats)
print(saras_pets.walk())


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        one = self.run_speed() * self.weight
        two = other_dog.run_speed() * other_dog.weight
        if one > two:
            return f"{self.name} is the winner\t{one} > {two}"
        return f"{other_dog.name} is the winner\t{two} > {one}"


dog_one = Dog("a", 10, 20)
dog_two = Dog("b", 12, 18)
dog_three = Dog("c", 15, 30)


def run(*dogs):
    for dog in dogs:
        print(dog.bark())
        print(dog.run_speed())


run(dog_one, dog_two, dog_three)

print(dog_one.fight(dog_two))
print(dog_two.fight(dog_three))
print(dog_three.fight(dog_one))
