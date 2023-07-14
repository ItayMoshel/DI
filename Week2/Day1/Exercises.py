print("""Hello World
Hello World
Hello World
Hello World
""")

print(99**3*8)

# False, True, False, TypeError, False

comp_brand = "Apple"

print(f"I have a {comp_brand} computer")

name = "Itay"
last_name = "Moshel"
age = 28
print(f"Hey, My name is {name} {last_name}. i am {age} years old.")
a = 10
b = 9
if a > b:
    print("Hello World")

user_input = int(input("Input a number:\n"))
if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")

user_name = input("What is your name?:\n")
if user_name.lower() == name.lower():
    print("Same")
else:
    print("Diff")


user_height = input("How tall are you in inch?:\n")
user_height_cm = int(user_height) * 2.54

if user_height_cm >= 145:
    print("Can")
else:
    print("Can't")

