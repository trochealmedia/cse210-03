"""cse210-03 Jumper Game"""
from posixpath import split
import random

class Secret_word:

    def __init__(self):

        self.word_list = ['Github','Nightmare', 'Python', 'Javascript','Taco']

    def pick_random(self):

        max_words = len(self.word_list) - 1
        word = random.randint(0, max_words)
        chosen_word = self.word_list[word]
    
        x = len(chosen_word)

        self.spelling = []

        for letter in chosen_word:
            self.spelling.append(letter)
        
        self.hidden = []

        for letter in chosen_word:
            self.hidden.append('-')

        print(self.hidden)
        print(self.spelling)


test = Secret_word()

test.pick_random()
