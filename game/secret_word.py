"""cse210-03 Jumper Game"""
from posixpath import split
import random

# TODO: 1) Encapsulate the self.word_list so nothing outside of the class can find out which words could be selected.
#       2) Encapsulate the self.spelling list so nothing outside of the class can find out how to spell the random word.
#       3) In comparing_word() method, if the player's guess does not match any letters in the random word, remove a line in Jumper.
#       4) In check_spelling() method, check if all the letters in 'self.hidden' match 'self.spelling'

class Secret_word:
    """A hidden word to be revealed by the player as they guess each letter in the word.

    Methods:
        pick_random()       | Picks a random word, spells the word, and hides the word.
        comparing_word()    | Compares player's guess with each letter in the word.
        print_hidden()      | Displays the hidden word. (ex. '- - - -')
        check_spelling()    | Checks if the revealed hidden word matches the random word.

    Lists:
        self.word_list=[]   | Contains all possible secret words.
        self.spelling=[]    | Contains each letter of the secret word.
        self.hidden=[]      | Holds placeholder letters that are marked as '-'.
    """
    def __init__(self):
        """Constructs a new instance of Secret_word.
        """
        self.word_list = ['github','nightmare', 'python', 'javascript','taco']

    def pick_random(self):
        """Selects a random word from the self.word_list. Creates two lists.
        """
        # Select a random word from the list.
        max_words = len(self.word_list) - 1
        word = random.randint(0, max_words)
        self.chosen_word = self.word_list[word].lower()
        # Create an empty list, appent it with each letter in the random word.
        self.spelling = []
        for letter in self.chosen_word:
            self.spelling.append(letter)
        # Create an empty list, append it with '-' for each letter.
        self.hidden = []
        for letter in self.chosen_word:
            self.hidden.append('-')

    def comparing_word(self, guess):
        """Compares each letter of the random word with the player's guess.
        """
        # Check if the guessed letter matches any letters in the random word.
        if guess in self.spelling:
            for letter in self.spelling:
                if guess == letter:
                    index = [pos for pos, char in enumerate(self.chosen_word) if char == guess]
                    #self.hidden[index] = letter
                    self.hidden[index[0]] = letter
            print("         Correct!         ")
        else:
            print("        Incorrect!        ")

    def print_hidden(self):
        """Displays the hidden random word.
        """
        for letter in self.hidden:
            print(f"{letter}", end=" ")
        print("\n")

    def check_spelling(self):
        """Compares the 'self.hidden' list with 'self.spelling' list.
        If the player guesses all letters, they will win the game.
        """
        pass
