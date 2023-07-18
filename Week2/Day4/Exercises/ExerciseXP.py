import random


def display_message():
    print("FULLSTACK DEVELOPMENT, Python, React")


display_message()


def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("one piece")


def describe_city(city, country="Israel"):
    print(f"{city.capitalize()} is in {country.capitalize()}")


describe_city("herzliya")


def guess(num: int):
    rand = random.randint(1, 100)
    if rand == num:
        return "Success"

    return f"Worng.\nYour number:{num}, Computers number: {rand}"


print(guess(45))


def make_shirt(size="L", text="I Love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")


make_shirt()
make_shirt("M")
make_shirt("S", "Logo")
make_shirt(text="Somthing", size="L")

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(lst):
    for i in lst:
        print(i)


def make_great(lst):
    for i in range(0, len(lst)):
        lst[i] += " The Great"


show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)


def get_random_temp(season):
    if season.lower() == 'winter':
        lower_limit = -10
        upper_limit = 16
    elif season.lower() == 'spring':
        lower_limit = 16
        upper_limit = 24
    elif season.lower() == 'summer':
        lower_limit = 24
        upper_limit = 32
    elif season.lower() == 'autumn' or season.lower() == 'fall':
        lower_limit = 32
        upper_limit = 40
    else:
        raise ValueError("Invalid season. Please choose 'winter', 'spring', 'summer', or 'autumn' (or 'fall').")

    return random.uniform(lower_limit, upper_limit)


def main():
    month = int(input("Enter the number of the month (1-12): "))

    if month == 12 or month <= 2:
        season = 'winter'
    elif month <= 5:
        season = 'spring'
    elif month <= 8:
        season = 'summer'
    elif month <= 11:
        season = 'autumn'
    else:
        raise ValueError("Invalid month. Please enter a number between 1 and 12.")

    temperature = get_random_temp(season)
    print(f"The temperature right now is {temperature:.1f} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature < 24:
        print("Pleasant weather. Enjoy your day!")
    elif temperature < 32:
        print("It's getting warm. Stay hydrated.")
    else:
        print("Hot weather! Find some shade and keep cool.")


main()

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def play_game(questions):
    random.shuffle(questions)
    num_questions = len(questions)
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for i, question in enumerate(questions):
        user_answer = input(f"Question {i + 1}/{num_questions}: {question['question']} ")
        if user_answer.lower() == question["answer"].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": question["question"],
                "user_answer": user_answer,
                "correct_answer": question["answer"]
            })

    print_results(correct_answers, incorrect_answers, wrong_answers)


def print_results(correct, incorrect, wrong_answers):
    print("\n===== RESULTS =====")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

    if incorrect > 0:
        print("\n=== WRONG ANSWERS ===")
        for wrong_answer in wrong_answers:
            print("Question:", wrong_answer["question"])
            print("Your answer:", wrong_answer["user_answer"])
            print("Correct answer:", wrong_answer["correct_answer"])
            print("--------------------")

    if incorrect > 3:
        print("\nYou had more than 3 wrong answers. Please play again.")
        play_again = input("Do you want to play again? (yes/no): ")

        if play_again.lower() == "yes":
            play_game(data)


play_game(data)
