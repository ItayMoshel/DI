class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, kind, num=1):
        if kind in self.animals:
            self.animals[kind] += num
        else:
            self.animals[kind] = num

    def get_info(self):
        string = f"{self.name}'s farm\n\n"
        for i in self.animals:
            if i == list(self.animals)[-1]:
                string += f"{i} : {self.animals[i]}\n\n    E-I-E-I-O!"
            else:
                string += f"{i} : {self.animals[i]}\n"

        return string

    def get_animal_types(self):
        animals_list = []
        for i in self.animals:
            animals_list.append(i)
        return sorted(animals_list)

    def get_short_info(self):
        s = f"{self.name}'s has "
        lst = self.get_animal_types()
        for i in lst:
            if i == lst[-1]:
                s += f" {i}."
            elif i == lst[-2]:
                s += f"{i}s and"
            else:
                s += f"{i}s, "
        return s


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())