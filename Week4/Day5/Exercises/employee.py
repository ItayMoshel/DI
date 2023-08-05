class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "position": self.position,
            "salary": self.salary
        }
