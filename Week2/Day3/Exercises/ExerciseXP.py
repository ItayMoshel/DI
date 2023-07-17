def ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age < 12:
        return 10
    elif age >= 12:
        return 15


def family_cost_printer(fam):
    total_cost = 0
    for key, value in fam.items():
        total_cost += ticket_price(value)
        print(f"{key.capitalize()} has to pay {ticket_price(value)}")
    print(f"The totatl cost is {total_cost}")


family1 = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family_cost_printer(family1)

family_count = int(input("How many are you?\n"))
family2 = dict()
for i in range(0, family_count):
    family_member = input("What's the family member's name?\n")
    family_member_age = int(input("What's their age?\n"))
    family2[family_member] = family_member_age
print(family2)
family_cost_printer(family2)

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

print(brand)

brand.pop("creation_date")

print(brand)

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

brand.update(more_on_zara)
print(brand)
print(brand["number_stores"])

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = dict()
disney_users_B = dict()
for i in range(0, len(users)):
    disney_users_A[users[i]] = i
    disney_users_B[i] = users[i]

disney_users_C = {}
k = 0
for i in sorted(users):
    disney_users_C[i] = k
    k += 1

print(disney_users_A)
print(disney_users_B)
print(disney_users_C)

disney_users_One = {}
n = 0
for i in users:
    if "i" in i.lower():
        disney_users_One[i] = n
        n += 1
print(disney_users_One)

disney_users_One = {}
j = 0
for i in users:
    if "m" or "p" in i.lower():
        disney_users_One[i] = j
        j += 1
print(disney_users_One)



