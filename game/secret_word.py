"""cse210-03 Jumper Game"""
from posixpath import split
import random

# TODO: 1) *DONE* Encapsulate the self.word_list so nothing outside of the class can find out which words could be selected.
#       2) *DONE* Encapsulate the self.spelling list so nothing outside of the class can find out how to spell the random word.

class Secret_word:
    """A hidden word to be revealed by the player as they guess each letter in the word.

    Attributes:
        .chosen_word        | The random word picked from the '.word_list'.

    Methods:
        pick_random()       | Picks a random word, spells the word, and hides the word.
        comparing_word()    | Compares player's guess with each letter in the word.
        print_hidden()      | Displays the hidden word. (ex. '- - - -')
        check_if_revealed() | Checks if the revealed hidden word matches the random word.

    Lists:
        self.word_list=[]   | Contains all possible secret words.
        self.spelling=[]    | Contains each letter of the secret word.
        self.hidden=[]      | Holds placeholder letters that are marked as '-'.
    """
    def __init__(self):
        """Constructs a new instance of Secret_word.
        """
        self.__word_list = ['github','nightmare', 'python', 'java', 'taco', 'banana', '']

    def pick_random(self):
        """Selects a random word from the self.word_list. Creates two lists.
        """
        # Select a random word from the list.
        max_words = len(self.__word_list) - 1
        word = random.randint(0, max_words)
        self.__chosen_word = self.__word_list[word].lower()
        # Create an empty list, appent it with each letter in the random word.
        self.__spelling = []
        for letter in self.__chosen_word:
            self.__spelling.append(letter)
        # Create an empty list, append it with '-' for each letter.
        self.hidden = []
        for letter in self.__chosen_word:
            self.hidden.append('-')

    def comparing_word(self, guess):
        """Compares each letter of the random word with the player's guess.
        """
        index = -1
        # Check if the guessed letter matches any letters in the random word.
        if guess in self.__spelling:
            for letter in self.__spelling:
                index += 1
                if guess == letter:
                    self.hidden[index] = letter
                    #position = [pos for pos, char in enumerate(self.chosen_word) if char == guess]
                    #self.hidden[position[0]] = letter
            print("         Correct!         ")
            return True
        else:
            print("        Incorrect!        ")
            return False

    def print_hidden(self):
        """Displays the hidden random word.
        """
        for letter in self.hidden:
            print(f"{letter}", end=" ")
        print("\n")

    def check_if_revealed(self):
        """Checks the 'self.hidden' list to see if any '-' items still remain.
        If there are no '-' items in the list, then the secret word would be fully revealed.
        """
        remaining = 0
        for letter in self.hidden:
            if letter == "-":
                remaining += 1
        # If all letters have been guessed in the word, return True.
        if remaining > 0:
            return False
        else:
            return True
