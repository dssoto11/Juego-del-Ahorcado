"""Archivo main del proyecto de Juego del Ahorcado con interfaz grafica """
import random

#lista de palabras secretas
word_list = ["python","hangman","programing","challenge"]
#elegir una palabra aleatoriamente
secret_world = random.choice(word_list)
#inicializacion de sets para almacenar intentos correctos e incorrectos de adivinal letras
correct_guesses = set()
incorrect_guesses = set()
#numero de intentos
attempts_left = 6

#funcion del estado del juego
def display_game_state():
    displayed_word = "".join([letter if letter in correct_guesses else "_" for letter in secret_world ])
    print(f"Word: {displayed_word}")
    print(f"Incorrect guesses: {' '.join(incorrect_guesses)}")
    print(f"Attemps left: {attempts_left}")

#bucle principal
while True:
    display_game_state()
    guess = input("Enter your guess:").lower()

    #chequeamos si la letra esta en la palabra secreta
    if guess in secret_world:
        correct_guesses.add(guess)
        #chequeamos si ya ha ganado el juego
        if set(secret_world).issubset(correct_guesses):
            print("Felicidades! has adivinado la palabra")
            break
    
    else:
        incorrect_guesses.add(guess)
        attempts_left -= 1
        #Chequeamos si ya ha perdido
        if attempts_left == 0:
            print("Fin del juego!!!")
            print(f"La palabra secreta era: {secret_world}")
            break
