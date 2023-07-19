class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Mark", 67)
cat2 = Cat("Wahlberg", 57)
cat3 = Cat("Cuban", 77)


def oldest(*cats):
    old = 0
    oldest_cat = ""
    for cat in cats:
        if cat.age > old:
            old = cat.age
            oldest_cat = cat
    return f"The oldest cat is {oldest_cat.name}, and he is {oldest_cat.age} years old."


print(oldest(cat1, cat3, cat2))


class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes WOOF!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} high!")


davids_dog = Dog("Rex", 50)
print(f"{davids_dog.name} {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"{sarahs_dog.name} {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()


def tallest(*dogs):
    mx = 0
    jumps_high = ""
    for i in dogs:
        if i.height > mx:
            mx = i.height
            jumps_high = i
    return jumps_high.name


print(tallest(davids_dog, sarahs_dog))


class Song:
    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_a_song(self):
        for i in self.lyrics:
            print(i)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_a_song()


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for i in self.animals:
            if i == self.animals[-1]:
                print(i)
            else:
                print(i, end=" ")



    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self) -> dict:
        sorted_animals = sorted(self.animals)
        animals_dict = {}
        for i in sorted_animals:
            first_letter = i[0].lower()

            if first_letter not in animals_dict:
                animals_dict[first_letter] = [i]
            else:
                animals_dict[first_letter].append(i)

        return animals_dict

    def get_groups(self):
        for key, value in self.sort_animals().items():
            print(f"In group '{key}' we have ", *value)


ramat_gan = Zoo("Zootopia")

ramat_gan.add_animal("Ape")
ramat_gan.add_animal("Baboon")
ramat_gan.add_animal("Bear")
ramat_gan.add_animal("Cat")
ramat_gan.add_animal("Cougar")
ramat_gan.add_animal("Eel")
ramat_gan.add_animal("Emu")
ramat_gan.add_animal("Dog")

ramat_gan.get_animals()
ramat_gan.sell_animal("Dog")
ramat_gan.get_animals()
print(ramat_gan.sort_animals())
ramat_gan.get_groups()
