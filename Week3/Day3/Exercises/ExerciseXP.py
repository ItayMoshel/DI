import random
import string
from datetime import datetime
from faker import Faker


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}" + ("s" if self.amount != 1 else "")

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        else:
            raise TypeError("Unsupported operand type for +=")

        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
# print(c1 + c3)


def roll_and_check(user_number):
    if not (1 <= user_number <= 100):
        print("Please enter a number between 1 and 100.")
        return

    random_number = random.randint(1, 100)
    print(f"Computer rolled: {random_number}")

    if user_number == random_number:
        print("Congratulations! It's a match!")
    else:
        print("Better luck next time.")


user_input = int(input("Enter a number between 1 and 100: "))
roll_and_check(user_input)


def generate_random_string(length=5):
    characters = string.ascii_letters
    rand_string = ''.join(random.choice(characters) for _ in range(length))
    return rand_string


random_string = generate_random_string(5)
print(random_string)


def display_current_date():
    current_date = datetime.now().date()
    print("Current date:", current_date)


display_current_date()


def time_left_until_january_1st():
    current_date = datetime.now()
    january_1st = datetime(current_date.year + 1, 1, 1)

    time_left = january_1st - current_date
    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    print(f"The 1st of January is in {days_left} days and {hours_left:02}:{minutes_left:02}:{seconds_left:02} hours.")


time_left_until_january_1st()


def minutes_lived(birthdate):
    try:
        birthdate_datetime = datetime.strptime(birthdate, "%Y-%m-%d")
        current_datetime = datetime.now()

        time_lived = current_datetime - birthdate_datetime
        minutes = int(time_lived.total_seconds() / 60)

        print(f"You have lived approximately {minutes} minutes.")
    except ValueError:
        print("Invalid date format. Please provide the date in the format 'YYYY-MM-DD'.")


birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
minutes_lived(birthdate_input)

fake = Faker()
users = []


def add_user():
    user_detail = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code(),
    }
    users.append(user_detail)


for _ in range(5):
    add_user()

for user in users:
    print(user)
