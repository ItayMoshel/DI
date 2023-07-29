import string
import nltk
from nltk.corpus import stopwords


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words_list = self.text.split()
        word_count = words_list.count(word)
        if word_count == 0:
            return None
        return word_count

    def most_common_word(self):
        words_list = self.text.split()
        word_counts = {}
        for word in words_list:
            word_counts[word] = word_counts.get(word, 0) + 1

        if not word_counts:
            return None

        most_common = max(word_counts, key=word_counts.get)
        return most_common

    def unique_words(self):
        words_list = self.text.split()
        unique_words = list(set(words_list))
        return unique_words

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            text_content = file.read()
        return cls(text_content)


text_instance = Text.from_file('the_stranger.txt')

word_to_check = "stranger"
frequency = text_instance.word_frequency(word_to_check)
if frequency:
    print(f"The word '{word_to_check}' appears {frequency} time(s) in the text.")
else:
    print(f"The word '{word_to_check}' is not found in the text.")

common_word = text_instance.most_common_word()
if common_word:
    print(f"The most common word in the text is: '{common_word}'")
else:
    print("The text is empty.")

unique_words_list = text_instance.unique_words()
print("Unique words in the text:", sorted(unique_words_list))
