"""CSE210 W05 - Jumper Game"""

new_section =  "-------------------"
half_section = "- - - - - - - - - -"

class Jumper:
    """A guy with a parachute who's life depends on the player.

    Attributes:
        .entire          | List - Contains string values for each row that displays the Jumper.
        .is_alive        | Boolean - Determines whether the Jumper is alive or not.

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

        self.entire = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        self.is_alive = True

    def print_self(self):
        """Displays the Jumper by printing each row.
        """
        for row in self.entire:
            print(row)

    def remove_line(self, incorect):
        """Removes lines from the Jumper's parachute based on the amount of incorrect answers.
        """
        row_x    = "       " # Replaces a line with a blank.
        row_5x   = "   X   " # Replaces jumper's head with an 'X' instead of a '0'.

        if incorect == 0:
            pass
        elif incorect == 1:
            self.entire[0] = row_x # Replaces row_1 with a blank area.
        elif incorect == 2:
            self.entire[1] = row_x # Replaces row_2 with a blank area.
        elif incorect == 3:
            self.entire[2] = row_x # Replaces row_3 with a blank area.
        elif incorect == 4:
            self.entire[3] = row_x # Replaces row_4 with a blank area.
        elif incorect >= 5:
            self.entire[4] = row_5x # Replaces row_5 with an 'X' instead of a '0'.
            self.is_alive = False
        else:
            pass
    
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

        self.entire = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
        self.is_alive = True
