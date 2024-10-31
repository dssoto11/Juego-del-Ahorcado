from tkinter import *
import random as random
import unicodedata

class JuegoDelAhorcado:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('900x700')
        self.ventana.title('JUEGO DEL AHORCADO')
        self.ventana.configure(bg='yellow')
        self.intentos_correctos = set()
        self.intentos_incorrectos = set()
        self.palabra_secreta = self.elegir_palabra_secreta().upper().strip()
        #self.palabra_secreta = unicodedata.normalize('NFKD', self.palabra_secreta).encode('ASCII', 'ignore')
        

        self.longitud = len(self.palabra_secreta)
        print(self.longitud)
        
        self.num_intentos_incorrectos = 7
        self.inicializar()
        self.botones_del_alfabeto()

    def elegir_palabra_secreta(self):

        filename = 'palabras_facil.txt'
        
        with open(filename) as archivo_objeto:
            lineas = archivo_objeto.readlines()
        palabra_secreta = random.choice(lineas)
        return palabra_secreta
    
    def inicializar(self):
        self.ventana2 = Frame(self.ventana,width=300,height=300,bg='white')
        self.ventana2.pack(pady=20)

        self.mostrar_palabra = Label(self.ventana,text="_" * self.longitud,font=('arial',20),bg='white')
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
        if letra in self.palabra_secreta and letra not in self.intentos_correctos:
            self.intentos_correctos.add(letra)
            print(self.intentos_correctos)
        elif letra not in self.intentos_incorrectos:
            self.intentos_incorrectos.add(letra)
            self.num_intentos_incorrectos -= 1
            #self.actualizar_dibujo_ahorcado ()

        self.actualizar_mostrar_palabra()
        self.chequear_condicion_ganadora()
    
    def actualizar_mostrar_palabra(self):
        mostrar_palabra = " ".join([letra if letra in self.intentos_correctos else "_" for letra in self.palabra_secreta])
        self.mostrar_palabra.config(text=mostrar_palabra)        
    
    def chequear_condicion_ganadora(self): 
        if set(self.palabra_secreta).issubset(self.intentos_correctos):
            self.mostrar_mensajes('FELICIDADES!, HA GANADO EL JUEGO')
        elif self.num_intentos_incorrectos == 0:
            self.mostrar_mensajes('LO SENTIMOS!, HA CONSUMIDO TODOS LOS INTENTOS')


    def mostrar_mensajes(self,mensaje):

        self.ventana_botones_alfabeto.pack_forget() # quitar botones del alfabero para mostrar mensajes

        self.mensajes_fin_juego = Label(self.ventana,text=mensaje,fg= 'red',font=('Arial',30))
        self.mensajes_fin_juego.pack(pady=15)       
              





def main():
    root = Tk()
    app = JuegoDelAhorcado(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
