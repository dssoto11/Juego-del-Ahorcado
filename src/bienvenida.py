from tkinter import *
import random as random
import unicodedata
from PIL import ImageTk, Image

class Bienvenida:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title('JUEGO DEL AHORCADO')
        imagen = PhotoImage(file='ahorcado2.png')
        label1 = Label(self.ventana, image=imagen)
        label1.image = imagen
        label1.pack()

    def botones_dificultad(self):
        facil = Button(self.ventana,)



def main():
    root = Tk()
    app = Bienvenida(root)
    root.mainloop()

if __name__ == '__main__':
    main()












