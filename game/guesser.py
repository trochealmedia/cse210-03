"""CSE210 W05 - Jumper - guesser.py"""

# TODO: Complete

class Guesser:
    """The player who tries to guess the letters in the hidden random word.

    Attributes:
        .times_guessed   | Int - Holds the value of the amount of valid attemps/guesses.
        .guess           | Str - Holds the player input which contains a single letter (a-z).

    Methods:
        ask_player()     | Ask the player for a string input (a-z). Store the guess within the object.
    """
    def __init__(self):
        """Constructs the Guesser.
        """
        self.times_guessed = 0
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.guess = ""

    def ask_player(self):
        """Asks the player for a letter (a-z). Ask again if the player enters an invalid input.
        """
        self.__quit = False
        # Loop if the user's input is invalid.
        while self.__quit == False:
            guess = input(f"({self.times_guessed}) Guess a letter [a-z]: ")
            guess_lower = guess.lower()
            # Check if the user is wanting to quit.
            if guess_lower == "0" or guess_lower == "quit" or guess_lower == 'exit':
                self.guess = ""
                self.__quit == True
                print("-------------------------")
                print("Exiting...\n")
                print("Thanks for playing!")
                break
            # Check if input is a letter in the alphabet or if there multiple characters were entered.
            if guess_lower not in self.alphabet or len(guess_lower) > 1:
                print(f"Error: '{guess}' is not an acceptable input. Please try again or type '0' to quit.")
            else:
                # Store guess in object.
                self.times_guessed += 1
                self.guess = guess_lower
                break
    
    

