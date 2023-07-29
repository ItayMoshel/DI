import random
import json


def get_words_from_file(f_name):
    try:
        with open(f_name, 'r') as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"File not found: {file}")
        return []


def get_random_sentence(length):
    file_path = 'word_list.txt'
    words_list = get_words_from_file(file_path)
    random_words = random.sample(words_list, length)
    sentence = ' '.join(random_words)
    return sentence.lower()


def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program will create a random sentence based on the word list provided.")

    while True:
        try:
            length = int(input("Enter the length of the sentence (between 2 and 20): "))
            if 2 <= length <= 20:
                sentence = get_random_sentence(length)
                print(f"Sentence generated: {sentence}")
                break
            else:
                print("Error: Please enter a valid integer between 2 and 20.")
        except ValueError:
            print("Error: Please enter a valid integer.")


# main()

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

j = json.loads(sampleJson)
print(j["company"]["employee"]["payable"]["salary"])
j["company"]["employee"]["birth_date"] = "28/07/1994"
print(j)
with open("f.txt", "w") as out:
    json.dump(j, out, indent=4)

