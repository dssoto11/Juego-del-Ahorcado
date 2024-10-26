from tkinter import *
import random as random

class JuegoDelAhorcado:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('700x600')
        self.ventana.title('JUEGO DEL AHORCADO')
        self.ventana.configure(bg='yellow')
        self.inicializar()

    def inicializar(self):
        self.ventana_secundaria()




    def ventana_secundaria(self):
        ventana2 = Frame(self.ventana,width=300,height=300,bg='white')
        ventana2.pack(pady=40)


    
    


def main():
    root = Tk()
    app = JuegoDelAhorcado(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
