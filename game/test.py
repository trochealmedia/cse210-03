from distutils.log import error
import random
from turtle import pos

"""
print(" ___\n/   \ \n ---\n\   /\n \ /\n  O \n /|\  \n / \ ")
print("--------------------")
print("\n/   \ \n ---\n\   /\n \ /\n  O \n /|\  \n / \ ")
print("--------------------")
print("\n\   /\n \ /\n  O \n /|\  \n / \ ")
print("--------------------")
print("\n \ /\n  O \n /|\  \n / \ ")
print("--------------------")
print("\n  x \n /|\  \n / \ ")
"""

"""

palabra = random.choice(word)
print(palabra)
word_lenght = len(palabra)
hiden_word = "-" * word_lenght
print(len(palabra))

print("-" * word_lenght)
print(hiden_word[0])
"""

import random
words = ["car", "train", "vaca", "magazine"]

class word:
    
    def __init__(self):
        "This will generate a word from the list"

    def chosenWord(self, word):
        global a_word
        a_word = random.choice(word)
        return a_word
    
    def hidenWord(self):
        word_lenght = len(a_word)
        word_hidden = "-" * word_lenght

        return word_hidden


palabra = word()


"""
"""


# Parachutes
full_parachute = " ___\n/   \ \n ---\n\   /\n \ /\n  O \n /|\  \n / \ "
one_error_parachute = "\n/   \ \n ---\n\   /\n \ /\n  O \n /|\  \n / \ "
second_error_parachute = "\n\   /\n \ /\n  O \n /|\  \n / \ "
third_error_parachute = "\n \ /\n  O \n /|\  \n / \ "
gameOver_parachute = "\n  x \n /|\  \n / \ "


def drawingParachute(errors):
    if errors == 0:
        print(full_parachute)
    elif errors == 1:
        print(one_error_parachute)
    elif errors == 2:
        print(second_error_parachute)
    elif errors == 3:
        print(third_error_parachute)
    else:
        print(gameOver_parachute)
        print("Game OVER")
        

unaPalabra = palabra.chosenWord(words)
largo = str(palabra.hidenWord())

is_playing = True

errors = 0
while is_playing:
    if is_playing == True:

        print(f'\n{largo}\n')

        drawingParachute(errors)

        guessing = input("Say a letter: ")

        posicion_found = [pos for pos, char in enumerate(unaPalabra) if char == guessing]

        if not guessing in unaPalabra:
            print("Esa letra no esta")
            errors += 1
            

        elif guessing in unaPalabra:
                   
            # REEMPLAZANDO LA LETRA ADIVINADA
            b = list(largo)
            b[posicion_found[0]] = guessing
            largo = "".join(b)

            # ESTE IF POR SI HAY MAS DE 2 LETRAS
            if len(posicion_found) == 2:
                b[posicion_found[1]] = guessing
                largo = "".join(b)
            else:
                None
            # IMPRIMIENDO LA NUEVA CADENA DE TEXTO
            # Y TAMBIEN EL PARACHUTE
            print(f'\n{largo}\n')
        
        if errors == 4:
            break
        
        if largo == unaPalabra:
            break

        print(errors)