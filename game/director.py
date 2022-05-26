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
        print("Jumper Game")
        print("---------------")
        
        self.jumper.print_self()
        self.secret_word.pick_random()


        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """
        """
        # Ask the user for a letter (a-z).
        self.guesser.ask_player()
        guess = self.guesser.guess
        print(guess)
        
        self.secret_word.comparing_word(guess)

    def _do_updates(self):
        """
        """
        # Compare the user's guess with the random word.
        pass
        
    def _do_outputs(self):
        """
        """
        # Display the results of the compare
        pass