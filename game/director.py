"""CSE210 W05 - Jumper - director.py"""

from game.jumper import Jumper
from game.guesser import Guesser
from game.secret_word import Secret_word

new_section =  "-------------------"
half_section = "- - - - - - - - - -"

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    """
    def __init__(self):
        """Constructs a new Director.
        """
        # Create objects using the following classes: 'Jumper', 'Guesser', 'Secret_Word'.
        self._is_playing = True
        print("start game.")
        
        self.jumper = Jumper()
        self.guesser = Guesser()
        self.secret_word = Secret_word()
        


    def start_game(self):
        """Starts the game by running the main game loop.
        """
        # Randomly pick a word to be hidden.
        self.secret_word.pick_random()

        # Print the into to the game.
        print(new_section)
        print("Jumper Game")
        print(half_section)
        print("Try to guess a letter in the hidden word.\n")

        # Give a hint. (REMOVE THIS)
        print(f"Hint: {self.secret_word.chosen_word}")
        
        # Print the hidden word for the first time.
        self.secret_word.print_hidden()
        # Print the jumper for the first time.
        self.jumper.print_self()
        
        # Loop through input, update, and outputs.
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """
        """
        # Ask the user for a letter (a-z).
        self.guesser.ask_player()
        self.guess = self.guesser.guess
        
    def _do_updates(self):
        """
        """
        # Compare the user's guess with the random word.
        self.secret_word.comparing_word(self.guess)
        
    def _do_outputs(self):
        """
        """
        # Display the results of the compare
        self.secret_word.print_hidden()
        self.jumper.print_self()