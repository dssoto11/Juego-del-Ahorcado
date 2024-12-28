"""Juego del Ahorcado con interfaz grafica """
import tkinter as tk
import random


class HangmanGame:
    def __init__(self,master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("900x650")
        self.master.configure(bg='light blue')#Fondo de color azul claro a la ventana principal
        self.word_list = ["PYTHON","JAVASCRIPT","KOTLIN","JAVA"]
        self.secret_word = self.choose_secret_word() #para cada vez que se inicie el juego cambie de palabra
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7 
        #self.master.iconbitmap('ahoracdo.ico')
        self.initialize_gui()

    

    #Creacion del lienzo hangman_canvas de 300x300 pix y fondo blanco   
    def initialize_gui(self):
        
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("Helvetica",20,"bold")
        self.hangman_canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.hangman_canvas.pack(pady=20)
    #incorporando whidgets de etiquetas para mostrar guiones con el numero de letras de la palabra secreta
        self.word_display = tk.Label(self.master, text= " _ " * len(self.secret_word), font=("Arial", 20), bg='light blue')
        self.word_display.pack(pady=(40,20))
            
        #Agregando botton de reinicio del juego a la interfaz grafica
        self.reset_button = tk.Button(self.master, text="Reiniciar Juego", command=self.reset_game, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.reset_button.pack(pady=(10, 0))

        #Agregando botones de letras del alfabeto y vinculandolos a un metodo de manejo de conjeturas
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=20)#Widget de marco para agrupar los botones del alfabeto
        self.setup_alphabet_buttons() #botones para cada letra del alfabeto

    #conexion de botones a la funcion guess_letter
    #para crear botones interactivos para cada letra del alfabeto.
    def setup_alphabet_buttons(self):
        #Personalizando la apariencia de los botones
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("helvetica",14,"bold")

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        upper_row = alphabet[:13] #1ra mitad, fila superior
        lower_row = alphabet[13:] # 2da mitad, fila inferior

        #creacion de dos marcos para cada fila del alfabeto
        upper_frame = tk.Frame(self.buttons_frame)
        upper_frame.pack()
        lower_frame = tk.Frame(self.buttons_frame)
        lower_frame.pack()
         
        # Asociacion de cada botón con el método guess_letter usando una función lambda, 
        # lo que permite que el juego reaccione a las conjeturas del jugador 
        # comparando la letra elegida con la palabra secreta, actualizando el estado del 
        # juego y refrescando la GUI.
        for letter in upper_row:
            button = tk.Button(upper_frame, text=letter, command=lambda l=letter: self.guess_letter(l),width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side="left", padx=2, pady=2)

        for letter in lower_row:
            button = tk.Button(lower_frame, text=letter, command=lambda l=letter: self.guess_letter(l),width=4, height=2, bg=button_bg, fg=button_fg, font=button_font)
            button.pack(side='left', padx=2, pady=2)

    def choose_secret_word (self):
        return random.choice(self.word_list)
    
    #Metodo para actualizar el dibujo en funcion de conjeturas incorrectas
    def update_hangman_canvas(self):
        self.hangman_canvas.delete("all")#borra el lienzo y vuelve a dibujar el la figura
        #creamos un metodo para dibujar cada parte del ahorcado
        #a medida que aumenta el numero de desaciertos
        stages = [self.draw_head, self.draw_body, self.draw_left_arm, self.draw_right_arm, self.draw_left_leg, self.draw_right_leg, self.draw_face]
        for i in range(len(self.incorrect_guesses)):
            if i < len(stages):
                stages[i]()

    #Metodos para dibujar detalladamente cada parte del ahorcado
    def draw_head(self):
        self.hangman_canvas.create_oval(125, 50, 185, 110, outline="black")

    def draw_body(self): 
        self.hangman_canvas.create_line(155, 110, 155, 170, fill="black")

    def draw_left_arm(self):
        self.hangman_canvas.create_line(155, 130, 125, 150, fill="black")

    def draw_right_arm(self): 
        self.hangman_canvas.create_line(155, 130, 185, 150, fill="black")

    def draw_left_leg(self): 
        self.hangman_canvas.create_line(155, 170, 125, 200, fill="black")

    def draw_right_leg(self): 
        self.hangman_canvas.create_line(155, 170, 185, 200, fill="black")

    def draw_face(self):
        #Dibujo de los ojos
        self.hangman_canvas.create_line(140, 70, 150, 80, fill="black")
        self.hangman_canvas.create_line(160, 70, 170, 80, fill="black")
        #Dibujo de la boca
        self.hangman_canvas.create_arc(140, 85, 170, 105, star=0, extent=-180, fill="black")
    
     #manejo de letras supuestas
    def guess_letter(self, letter):
        if letter in self.secret_word and letter not in self.correct_guesses:
            self.correct_guesses.add(letter)
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
            self.update_hangman_canvas()

        self.update_word_display()
        self.check_game_over()

     #Actualizando la palabra mostrada, revelando cualquier letra adivinada
    def update_word_display(self):
        displayed_word = " ".join([letter if letter in self.correct_guesses else "_" for letter in self.secret_word])
        self.word_display.config(text=displayed_word)
    
    #chequea si el juego se gano o se perdio, mostrando un mensaje apropiado
    def check_game_over(self):
        if set(self.secret_word).issubset(self.correct_guesses):
            self.display_game_over_message("Felicidades, ha ganado el juego")
        elif self.attempts_left == 0:
            self.display_game_over_message(f"Juego Terminado! La palabra secreta era: {self.secret_word}")

     #Agregando mensajes de fin del juego
    def display_game_over_message(self, message):
        stylish_font = ("Arial 18 italic")
        button_bg = "#4a7a8c"
        button_fg = "white"
        button_font = ("helvetica",12,"bold")

        self.reset_button.pack_forget()#Para ocultar el boton de reinicio del juego
        self.buttons_frame.pack_forget()#oculta los botones del alfabeto

        #widget de etiqueta que muestra el mensaje de fin del juego en el area que antes ocupaban 
        #las letreas del alfabeto
        self.game_over_label = tk.Label(self.master, text=message, font=stylish_font, fg="red", bg='light blue')
        self.game_over_label.pack(pady=(10, 20))
        
        #Añadiendo un boton de reinicio del juego debajo del mensaje de fin del juego
        if not hasattr(self, 'restart_button'):
            self.restart_button = tk.Button(self.master, text="Restar Game", command=self.reset_game, width=20, height=2, bg=button_bg, fg=button_fg, font=button_font)
        self.restart_button.pack(pady=(10, 20))

    #Metodo de reinicio del juego
    def reset_game(self):
        self.secret_word = self.choose_secret_word ()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = 7

        self.hangman_canvas.delete("all")
        self.update_word_display()

        for frame in self.buttons_frame.winfo_children():
            for button in frame.winfo_children():
                button.configure(state=tk.NORMAL)
        
        self.reset_button.pack(pady=(10, 10))

        if hasattr(self,'game_over_label') and self.game_over_label.winfo_exists():
            self.game_over_label.pack_forget()
        if hasattr(self,'restart_button') and self.restart_button.winfo_exists():
            self.restart_button.pack_forget()

        self.buttons_frame.pack()

#definicion de funcion para crear la ventana raiz de tkinter
#e iniciar el bucle de eventos de tkinter
def main():
    raiz = tk.Tk()#ventana raiz
    game = HangmanGame(raiz)
    raiz.mainloop() #bucle de eventos
    

if __name__ == "__main__":
    main()



