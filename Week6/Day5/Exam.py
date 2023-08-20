import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set

# c

# Using a list comprehension,
# generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.
squares_of_evens = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares_of_evens)

# Using the range function, create a list of numbers from 1 to 10,
# then print numbers that are divisible by both 2 and 3.
lst = list(range(1, 11))
numb = [num for num in lst if num % 2 == 0 and num % 3 == 0]
print(numb)

# Loop through the provided list of dictionaries and print the names and ages:
student_list = [
    {
        "name": "John",
        "age": 24
    },
    {
        "name": "Anna",
        "age": 22
    },
    {
        "name": "Mike",
        "age": 25
    }
]

for i in student_list:
    print(i["name"], i["age"])


# Write a function combine_words that accepts any number of positional arguments and key-value arguments.
# The function should return a single sentence combining all the words provided.
# Example:
def combine_words(*args, **kwargs):
    words1 = args
    words2 = [kwargs['first'], kwargs['second'], kwargs['third']]
    words = list(words1) + list(words2)
    sentence = " ".join(words)
    return sentence


result = combine_words("Hello", "world", second="is", third="great!", first="Python")
print(result)
# Expected Output:
"Hello world. Python is great!"


# Create a class Vehicle with string attributes type,
# brand, and integer attribute year.
# Ensure instances of the vehicle cannot be created
# if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.
class Vehicle:
    def __init__(self, type, brand, year):
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"


vehicle1 = Vehicle("Car", "Toyota", 2022)
vehicle2 = Vehicle("Motorcycle", "Honda", 2020)

print(vehicle1)
print(vehicle2)


# Create a class Car with string attributes brand,
# model, and integer attribute mileage.
# Implement a method to return the car’s details.
class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def car_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage} miles"


car1 = Car("Toyota", "Camry", 30000)

details = car1.car_details()
print(details)


# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity.
# Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value
# and @battery_capacity.setter to modify the battery capacity only if the new value is positive.

class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity):
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity
        else:
            print("Battery capacity must be a positive value.")

    def car_details(self):
        details = super().car_details()
        return f"{details}, Battery Capacity: {self.__battery_capacity} kWh"


electric_car = ElectricCar("Tesla", "Model S", 10000, 75.5)

details = electric_car.car_details()
print(details)

electric_car.battery_capacity = 80.0

details = electric_car.car_details()
print(details)


# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder.
# Implement methods to deposit, withdraw, and view the balance.
# Include a class method to track accounts created and a static method for a bank policy message.
# Ensure the balance is non-negative.

class BankAccount:
    __accounts_created = 0

    def __init__(self, account_holder, initial_balance=0.0):
        self._account_holder = account_holder
        self._balance = initial_balance
        BankAccount.__accounts_created += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount:.2f} dollars.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount:.2f} dollars.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def view_balance(self):
        print(f"Account holder: {self._account_holder}")
        print(f"Balance: {self._balance:.2f} dollars")

    @classmethod
    def accounts_created(cls):
        return cls.__accounts_created

    @staticmethod
    def bank_policy_message():
        return "Welcome to our bank! Please follow our bank policies."


account1 = BankAccount("Alice", 1000.0)
account2 = BankAccount("Bob", 500.0)

account1.deposit(200)
account1.withdraw(100)
account1.view_balance()

account2.deposit(300)
account2.withdraw(700)
account2.view_balance()

print("Total accounts created:", BankAccount.accounts_created())
print(BankAccount.bank_policy_message())

# Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().
arr_2d = np.arange(1, 10).reshape(3, 3)
print(arr_2d)

# Provided pandas DataFrame df:
# Replace non-numeric values in column “A” with the mean of numeric values.
# Plot a histogram of the “A” column using matplotlib.


df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})

df['A'] = pd.to_numeric(df['A'], errors='coerce')
mean_A = df['A'].mean()
df['A'].fillna(mean_A, inplace=True)

plt.hist(df['A'], bins=10, alpha=0.7, color='blue', edgecolor="black")
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Column A')
plt.show()

# Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.
df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})
df['A'] = pd.to_numeric(df['A'], errors='coerce')

plt.plot(df['A'], label='Column A')
plt.plot(df['B'], label='Column B')
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Plot of Columns A and B')
plt.legend()

plt.show()
