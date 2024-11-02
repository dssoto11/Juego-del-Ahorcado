from tkinter import *
import random as random
import unicodedata
from PIL import ImageTk, Image


class VentanaBienvenida:
        def __init__(self,ventana):
            self.ventana = ventana
            #self.ventana.geometry('900x700')
            self.ventana.title('JUEGO DEL AHORCADO')
            
            imagen = Image.open('ahorcado.png')
            
            #imagen = imagen.resize(200,200)
            imagen_tk = ImageTk.PhotoImage(imagen)
            bienvenida = Label(self.ventana,image=imagen_tk)
            bienvenida.pack()


def main():
    root = Tk()
    bienvenida = VentanaBienvenida(root)
    root.mainloop()


if __name__ == '__main__':
    main()