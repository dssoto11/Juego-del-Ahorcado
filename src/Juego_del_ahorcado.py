from tkinter import *
import random as random

class JuegoDelAhorcado:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('700x600')
        self.ventana.title('JUEGO DEL AHORCADO')
        self.ventana.configure(bg='yellow')
        self.intentos_correctos = set()
        self.intentos_incorrectos = set()
        self.num_intentos_incorrectos = 7
        self.inicializar()

    def inicializar(self):
        self.ventana2 = Frame(self.ventana,width=300,height=300,bg='white')
        self.ventana2.pack(pady=40)

        self.mostrar_palabra = Label(self.ventana,text="_" * (len(self.palabra_secreta())),font=('arial',20),bg='white')
        self.mostrar_palabra.pack(expand=True,pady=10)

    def botones_del_alfabeto(self):
        pass







    def palabra_secreta(self):
        filename = 'palabras.txt'
        with open(filename) as archivo_objeto:
            lineas = archivo_objeto.readlines()
        palabra_secreta = random.choice(lineas)
        return palabra_secreta
        
              


    
    


def main():
    root = Tk()
    app = JuegoDelAhorcado(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
