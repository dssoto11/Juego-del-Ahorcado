"""Juego del Ahorcado con interfaz grafica """
import tkinter as tk
import random

class HangmanGame:
    def __init__(self,master):
        self.master = master
        self.master.title("Juego del Ahoracdo")
        self.master.geometry("900x600")
        self.word_list = ["PYTHON","JAVASCRIPT","KOTLIN","JAVA"]
        self.secret_world = self.choose_secret_word() #para cada vez que se inicie el juego cambie de palabra
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7
        self.initialize_gui()

    def choose_secret_word (self):
        return random.choice(self.word_list)

    #Creacion del lienzo hangman_canvas de 300x300 pix y fondo blanco   
    def initialize_gui(self):
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
    #incorporando whidgets de etiquetas para mostrar guiones con el numero de letras de la palabra secreta
        self.word_display = tk.Label(self.master, text="_" * len(self.secret_word), font=("Helvetica",30))
        self.word_display.pack(pady=(40,20))
    #Agregando botones de letras del alfabeto y vinculandolos a un metodo de manejo de conjeturas
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)#Widget de marco para agrupar los botones del alfabeto
        self.setup_alphabet_buttons() #botones para cada letra del alfabeto
    
    #Metodo para actualizar el dibujo en funcion de conjeturas incorrectas
    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")#borra el lienzo y vuelve a dibujar el la figura
        incorrect_guesses_count = len(self.incorrect_guesses)
        if incorrect_guesses_count >= 1:
            self.hangman_canvas.create_line(50, 180, 150, 180)





#definicion de funcion para crear la ventana raiz de tkinter
#e iniciar el bucle de eventos de tkinter
def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()



