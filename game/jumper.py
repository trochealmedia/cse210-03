"""CSE210 W05 - Jumper Game"""

# TODO: Complete

class Jumper:
    """A guy with a parachute who's life depends on the player.

    Attributes:
        .rows            | List - Contains string values for each row that displays the Jumper.
        .is_alive        | Boolean - Determines whether the Jumper is alive or not.
        .mistakes        | Int - Counts the amount of wrong guesses that the player makes.

    Methods:
        print_self()     | Displays the Jumper at his current state.
        remove_line()    | Removes a line off the Jumper's parachute based on the amount of incorrect answers.
        reset_jumper()   | Restores the Jumper back to his original state.
    """
    def __init__(self):
        """Constructs the Jumper.
        """
        row_1  = "  ___  "
        row_2  = " /___\ "
        row_3  = " \   / "
        row_4  = "  \ /  "
        row_5  = "   0   "
        row_6  = "  /|\  "
        row_7  = "  / \  "
        row_8  = "       "
        row_9  = "^^^^^^^" 

        self.rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        self.is_alive = True
        self.mistakes = 0

    def print_self(self):
        """Displays the Jumper by printing each row.
        """
        for row in self.rows:
            print(row)
        print()

    def remove_line(self):
        """Remove a lines from the Jumper's parachute each time player guesses wrong.
        """
        row_5x   = "   X   " # Replaces jumper's head with an 'X' instead of a '0'.
        self.mistakes += 1

        if self.mistakes < 4:
            self.rows.pop(0)
            self.is_alive = True
        elif self.mistakes >= 4:
            self.rows.pop(0)
             # replace Jumper's head with an 'x'.
            self.rows[0] = row_5x
            self.is_alive = False
           
    def reset_jumper(self):
        """Restores the Jumper back to his full glory.
        """
        row_1  = "  ___  "
        row_2  = " /___\ "
        row_3  = " \   / "
        row_4  = "  \ /  "
        row_5  = "   0   "
        row_6  = "  /|\  "
        row_7  = "  / \  "
        row_8  = "       "
        row_9  = "^^^^^^^" 

        self.rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        self.is_alive = True
