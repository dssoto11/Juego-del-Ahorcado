from tkinter import *
import random as random

class JuegoDelAhorcado:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('900x700')
        self.ventana.title('JUEGO DEL AHORCADO')
        self.ventana.configure(bg='yellow')
        self.intentos_correctos = set()
        self.intentos_incorrectos = set()
        self.num_intentos_incorrectos = 7
        self.inicializar()
        self.botones_del_alfabeto()

    def inicializar(self):
        self.ventana2 = Frame(self.ventana,width=300,height=300,bg='white')
        self.ventana2.pack(pady=20)

        self.mostrar_palabra = Label(self.ventana,text="_" * (len(self.palabra_secreta())),font=('arial',20),bg='white')
        self.mostrar_palabra.pack(pady=10)

    def botones_del_alfabeto(self):
        alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVXYZ'
        self.primera_mitad = alfabeto[:13]
        self.segunda_mitad = alfabeto[13:]

        self.ventana_botones_alfabeto = Frame(self.ventana)
        self.ventana_botones_alfabeto.pack(pady=40)

        self.ventana_primera_mitad = Frame(self.ventana_botones_alfabeto)
        self.ventana_primera_mitad.pack()
        self.ventana_segunda_mitad = Frame(self.ventana_botones_alfabeto)
        self.ventana_segunda_mitad.pack()

        for letra in self.primera_mitad:
            botton = Button(self.ventana_primera_mitad, text=letra, command=lambda l=letra: self.adivinar_letra(l), width=6, height=3,font=('arial',18),fg='black',bg='light green')
            botton.pack(side='left',padx=2,pady=2)

        for letra in self.segunda_mitad:
            botton = Button(self.ventana_segunda_mitad, text=letra, command=lambda l=letra: self.adivinar_letra(l), width=6, height=3,font=('arial',18),fg='black',bg='light green')
            botton.pack(side='left',padx=2,pady=2)
      
        
    def adivinar_letra(self,letra):
        self.letra = letra
        if self.letra in self.palabra_secreta() and self.letra not in self.intentos_correctos:
            self.intentos_correctos.add(self.letra)
        elif self.letra not in self.intentos_incorrectos:
            self.intentos_incorrectos.add(self.letra)
            self.num_intentos_incorrectos -= 1
            self.actualizar_dibujo_ahorcado

        self.actualizar_mostrar_palabra()
        self.chequear_fin_juego ()
    
    def actualizar_mostrar_palabra(self):
        mostrar_palabra = " ".join([letra if letra in self.intentos_correctos else "_" for letra in self.intentos_incorrectos])
        self.mostrar_palabra.config(text=mostrar_palabra)        
       







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
    
