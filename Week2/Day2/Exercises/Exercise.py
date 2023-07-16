my_fav_numbers = {1, 2, 3, 4, 7}
print(my_fav_numbers)
my_fav_numbers.add(5)
my_fav_numbers.add(6)
print(my_fav_numbers)
my_fav_numbers = set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)

friend_fav_numbers = {44, 55, 66, 11}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# tuple is unchangeable

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.pop()
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

num = 1
num_lis = []
while num < 5:
    num += 0.5
    num_lis.append(num)
print(num_lis)

for i in range(1, 21):
    print(i, end=" ")

print()

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print()

my_name = "itay"
user_name = ""
while user_name != my_name:
    user_name = input("What is your name?:\n").lower()

user_fav_fruits = input("What is your favorite fruit? use single space.\n")
user_fruits = user_fav_fruits.split(" ")
fruit_choice = input("Please name a fruit:\n")
if fruit_choice in user_fruits:
    print("You chose one of your favorite fruits! Enjoy!.")
else:
    print("You chose a new fruit. I hope you enjoy")

more_toppings = "more"
toppings = []
while more_toppings == "more":
    user_toppings = input("Enter your toppings. Write \"quit\" when done.\n")
    if user_toppings.lower() != "quit":
        print(f"{user_toppings} added to your pizza.\n")
        toppings.append(user_toppings)
    elif user_toppings.lower() == "quit":
        final = " ".join(toppings)
        bill = 10 + (len(toppings) * 2.5)
        print(f"{final} on your pizza. bill: {bill}")
        more_toppings = "no"

family_count = int(input("How many are you?\n"))
family_ages = []
movie_cost = 0
for i in range(0, family_count):
    age = int(input("What is your age?\n"))
    family_ages.append(age)
    if age < 3:
        movie_cost += 0
    elif 3 <= age < 12:
        movie_cost += 10
    elif age >= 12:
        movie_cost += 12
print(f"Total cost is: {movie_cost}")

names = ['red', 'blue', 'green', 'grey', 'white', 'black']
print(names)
k = 0
for i in range(0, len(names)):
    teen_age = int(input("How old are you?"))
    if not 16 <= teen_age <= 21:
        names.remove(names[i - k])
        k += 1
print(names)

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich",
                   "Chicken sandwich", "Pastrami sandwich"]
print(sandwich_orders)
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    print("In while")
if "Pastrami sandwich" not in sandwich_orders:
    print("Success!\n", sandwich_orders)

finished_sandwiches = []
k = 0
for i in range(0, len(sandwich_orders)):
    print(f"I made your {sandwich_orders[i - k]}")
    finished_sandwiches.append(sandwich_orders[i - k])
    sandwich_orders.remove(sandwich_orders[i - k])
    print(f"finished_sandwiches: {finished_sandwiches}, sandwich_orders: {sandwich_orders}\n")
    k += 1


