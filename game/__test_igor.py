import random

class Game:
    def __init__(self):
        self.secret_word = Secret_Word()
        self.parachute_guy = Jumper()
    def start_jumper(self):
        while True:
            self.secret_word.print_puzzle()           # self is a default parameter for my methods
            self.parachute_guy.print_parachute_guy()
            self.secret_word.ask_for_next_letter()
            result = self.secret_word.check_if_the_guess_is_right()
            if result != True:
                self.parachute_guy.remove_row_from_parachute()
            if self.check_game_over():
                break
        self.parachute_guy.print_parachute_guy()
    def check_game_over(self):
        #Check if you found the secret word
        if self.secret_word.found_secret_word():
            return True
        #check if the parachute guy is dead
        if self.parachute_guy.is_dead():
            return True
        else:
            return False
            
# =======================================

class Secret_Word:
    def __init__(self):
        self.secret = random.choice(["water", "raton", "codes"])
        self.puzzle_state = ["_", "_", "_", "_", "_"]
        self.next_guess = ""
    def print_puzzle(self):
      print(self.puzzle_state)
    def ask_for_next_letter(self):
        self.next_guess = input("What is the next letter?")
    def check_if_the_guess_is_right(self):
        result = False
        for i, letter in enumerate(self.secret):
            if letter == self.next_guess:
                result = True
                self.puzzle_state[i] = self.next_guess
        if result:
            print(f"Letter {self.next_guess} is in the secret word")
        else:
            print(f"Sorry, letter {self.next_guess} is not in the secret word ")
        return result
    def found_secret_word(self):
        if "_" in self.puzzle_state:
            return False
        else:
            return True
# my_secret = Secret_Word()
# my_secret.print_puzzle()
# my_secret.ask_for_next_letter()
# my_secret.check_if_the_guess_is_right()
# my_secret.print_puzzle()
# my_secret.ask_for_next_letter()
# my_secret.check_if_the_guess_is_right()
# my_secret.print_puzzle()
# my_secret.ask_for_next_letter()
# my_secret.check_if_the_guess_is_right()
# my_secret.print_puzzle()

# =======================================

class Jumper:
    def __init__(self):
        row1   =  "  ___ "
        row2   =  " /___\ "
        row3   =  " \   / "
        row4   =  "  \ / "
        row5   =  "   0  "
        row6   =  "  /|\ "
        row7   =  "  / \ "
        row8   =  "^^^^^^^^^^"
        self.parachute_rows = [row1, row2, row3, row4, row5, row6, row7, row8]
    def print_parachute_guy(self):
        for row in self.parachute_rows:
            print(row)
    def remove_row_from_parachute(self):
        self.parachute_rows.pop(0)
        if self.is_dead():
            self.parachute_rows[0] = "   X"
    def is_dead(self):
        if len(self.parachute_rows) <= 4:
            return True
        else:
            return False
# my_parachute = Jumper()
# my_parachute.print_parachute_guy()
# my_parachute.remove_row_from_parachute()
# my_parachute.print_parachute_guy()

# =======================================

jumper_game = Game()
jumper_game.start_jumper()