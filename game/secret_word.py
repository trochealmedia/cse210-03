"""cse210-03 Jumper Game"""
from posixpath import split
import random

class Secret_word:

    def __init__(self):

        self.word_list = ['github','nightmare', 'python', 'javascript','taco']

    def pick_random(self):

        max_words = len(self.word_list) - 1
        word = random.randint(0, max_words)
        self.chosen_word = self.word_list[word].lower()
    
        x = len(self.chosen_word)

        self.spelling = []

        for letter in self.chosen_word:
            self.spelling.append(letter)
        
        self.hidden = []

        for letter in self.chosen_word:
            self.hidden.append('-')

        #print(self.hidden)
        #print(self.spelling)

        for letter in self.hidden:
            print(f"{letter}", end=" ")

        print(f'\n {self.chosen_word}')

    def comparing_word(self, guess):

        if guess in self.spelling:
            for letter in self.spelling:
                if guess == letter:
                    index = str([pos for pos, char in enumerate(self.chosen_word) if char == guess])
                    int_index = int(index)
                    print(index)
                    print(f"Letter found on letter {letter}")

                    #self.hidden[index] = letter
                    print(self.hidden[int_index])

        else:
            print("No")

    


