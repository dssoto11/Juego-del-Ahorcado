"""El clasico juego del ahorcado programado usando python y librerias como tkinter para mostrar 
una interfaz grafica
"""
from tkinter import *
from tkinter.font import *
import random as random
from PIL import ImageTk, Image
import Juego_del_ahorcado_dificil as ja

#Creando la clase principal del juego, donde se define las dimensiones de la ventana raiz del juego,
#el titulo de la misma y el color de background de la misma
class Juego:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('1280x720')      
        self.imagen()

    #Colocacion de la imagen de fondo de la ventana principal
    def imagen(self):
        ima = Image.open('imagenes/ahorcado3.png')
        imagen = ImageTk.PhotoImage(ima)
        self.label1 = Label(self.ventana, image=imagen)
        self.label1.image = imagen
        self.label1.place(x=0,y=0)
    #Creacion de los bonones para elegir el nivel de dificultad conque se desea jugar
        grado_dificultad = ['FACIL', 'MEDIO', 'DIFICIL']
        self.elegirdif = Label(self.label1,text='Elija dificultad',fg='blue',font='Helvetica 80 bold').place(x= 400,y=500)
        
        margen=400
        for dificultad in grado_dificultad:
            self.buttond = Button(self.label1, text=dificultad,width=20, height=5,justify=LEFT, command=lambda l=dificultad: self.elegir_dificultad(l),font=f'Helvetica 80 bold',bg='light green')
            self.buttond.place(x=margen,y=580)
            margen += 300
    #Eleccion del archivo que posee las palabras secretas, segun el nivel de dificultad elegido
    def elegir_dificultad(self,dificultad):
        if dificultad == 'FACIL':
            self.label1.place_forget()
            ja.JuegoDelAhorcado(self.ventana)

        elif dificultad == 'MEDIO':
            self.label1.place_forget()
            ja.JuegoDelAhorcado(self.ventana)
            
        elif dificultad == 'DIFICIL':
            self.label1.place_forget()
            ja.JuegoDelAhorcado(self.ventana)
            
        

def main():
    root = Tk()
    app = Juego(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
