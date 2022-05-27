"""CSE210 W05 - Jumper - director.py"""

from game.jumper import Jumper
from game.guesser import Guesser
from game.secret_word import Secret_word

# TODO: 1) in '._do_updates()' method, check if an error was made, remove a line from the Jumper.
#       2) in '._do_updates()' method, check if the hidden word is completed and matches the random word's spelling.
#       3) End the game if the word is spelled correctly or if the player makes 4 errors.
#       4) Ask player if they want to play again.

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

        # Give a hint. (REMOVE THIS)
        print(f"Hint: {self.secret_word.chosen_word}")
        
        # Print the hidden word for the first time.
        self.secret_word.print_hidden()
        # Print the jumper for the first time.
        self.jumper.print_self()
        
        # =======================================

        # Loop through input, update, and outputs.
        while self._is_playing == True:
            self._get_inputs()
            # Check if player is still playing.
            if self._is_playing == True:
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
        self.secret_word.comparing_word(self.guess)
        # If 'self.guess' is not in list, remove a line from the jumper.
        
        # Check if the hidden word is completed/revealed.
         
        print("-------------------------\n")

    def _do_outputs(self):
        """
        """
        # Display the results of the compare
        self.secret_word.print_hidden()
        self.jumper.print_self()