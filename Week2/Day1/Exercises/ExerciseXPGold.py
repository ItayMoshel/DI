print(
    "Hello world\nHello world\nHello world\nHello world\nI love python\nI love python\nI love python\nI love python\n")

# print("Hello world\n" * 4, "I love python\n" * 4)

month = int(input("Insert a number for a month (1-12):\n"))
if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Fall")
elif month == 12 or 1 <= month <= 2:
    print("Winter")
else:
    print("ValueError. Please in put a number in said range.")
