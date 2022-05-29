"""CSE210 W05 - Jumper - director.py"""

from game.jumper import Jumper
from game.guesser import Guesser
from game.secret_word import Secret_word

# TODO: 1) Ask player if they want to play again. If so, reset the hidden word and jumper.

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """
    def __init__(self):
        """Constructs a new Director.
        """
        # Create objects using the following classes: 'Jumper', 'Guesser', 'Secret_Word'.
        self._is_playing = True
        
        self.jumper = Jumper()
        self.guesser = Guesser()
        self.secret_word = Secret_word()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        """
        # Print the into to the game.
        print("-------------------------")
        print("       Jumper Game       ")
        print("-------------------------")
        print("Try to guess a letter in the hidden word.\n")

        # =======================================

        # Randomly pick a word to be hidden.
        self.secret_word.pick_random()
        
        ### TEST ### print(f"Hint: {self.secret_word.chosen_word}")

        # Print the hidden word for the first time.
        self.secret_word.print_hidden()
        # Print the jumper for the first time.
        self.jumper.print_self()
        
        # =======================================

        # Loop through input, update, and outputs.
        while self._is_playing == True:
            # Check if player is still playing.
            if self._is_playing == True:
                self._get_inputs()
                self._do_updates()
                self._do_outputs()
                # Exit loop if player wants to quit.
            else:
                break

    def _get_inputs(self):
        """
        """
        # Ask the user for a letter (a-z).
        self.guesser.ask_player()
        self.guess = self.guesser.guess
        # Check if the user is trying to exit.
        if self.guess == "":
            self._is_playing = False
        print("-------------------------")

    def _do_updates(self):
        """
        """
        # Compare the player's guess with the random word.
        correct = self.secret_word.comparing_word(self.guess)
        # If 'self.guess' is not in list, remove a line from the jumper.
        if not correct:
            self.jumper.remove_line()
        print("-------------------------\n")

    def _do_outputs(self):
        """
        """
        # Display the results of the compare
        self.secret_word.print_hidden()
        self.jumper.print_self()
        # Check if the secret word has been completely revealed. If so, player wins the game.
        win = self.secret_word.check_if_revealed()
        if win:
            print("Congratulations! You win!\n")
            self._is_playing = False
        # check if the player has made 4 wrong guesses. If so, player loses the game.
        if self.jumper.is_alive == False:
            print("Oh no! Looks like there was not enough parachute left to keep the jumper alive.\n")
            self._is_playing = False