"""CSE210 W05 - Jumper - director.py"""

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
        
    def start_game(self):
        """Starts the game by running the main game loop.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """
        """
        # Ask the user for a letter (a-z).
        pass

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