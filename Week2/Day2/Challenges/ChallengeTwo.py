from datetime import date

user_birth = input("Enter your birthday: DD/MM/YYYY\n").split("/")
Day, Month, Year = int(user_birth[0]), int(user_birth[1]), int(user_birth[2])
today = date.today()
age = today.year - Year - ((today.month, today.day) < (Month, Day))
last_num = int(str(age)[-1])
print(age)
print(f"""
      ___{"i" * last_num}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
""")

if (Year % 400 == 0) and (Year % 100 == 0):
    print("{0} is a leap year".format(Year))
elif (Year % 4 == 0) and (Year % 100 != 0):
    print("{0} is a leap year".format(Year))
else:
    print("{0} is not a leap year".format(Year))
