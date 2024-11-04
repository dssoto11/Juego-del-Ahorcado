from tkinter import *
from tkinter.font import *
import random as random
from PIL import ImageTk, Image



  
class JuegoDelAhorcado:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('1280x720')
        self.ventana.title('JUEGO DEL AHORCADO')        
        self.ventana.configure()
        self.ventana.configure(bg='yellow')
        self.inicializar()
    
    def inicializar(self):
        self.intentos_correctos = set()
        self.intentos_incorrectos = set()     
        self.num_intentos_incorrectos = 7
        self.imagen()
           
    def imagen(self):
        fuente = Font(family="Roboto Cn", size=30)



        ima = Image.open('ahorcado2.png')
        #new_ima = ima.resize((900,506))
        imagen = ImageTk.PhotoImage(ima)
        self.label1 = Label(self.ventana, image=imagen)
        self.label1.image = imagen
        self.label1.place(x=0,y=0)
    
        grado_dificultad = ['FACIL', 'MEDIO', 'DIFICIL']
        
        self.elegirdif = Label(self.label1,text='Elija dificultad',fg='blue',font='Helvetica 80 bold').place(x= 400,y=500)
        
        margen=400
        for dificultad in grado_dificultad:
            self.buttond = Button(self.label1, text=dificultad,width=20, height=5,justify=LEFT, command=lambda l=dificultad: self.elegir_dificultad(l),font=f'Helvetica 80 bold',bg='light green')
            self.buttond.place(x=margen,y=600)
            margen += 300
        
    def elegir_dificultad(self,dificultad):
        if dificultad == 'FACIL':
            filename = 'palabras_facil.txt'

        elif dificultad == 'MEDIO':
            filename = 'palabras_medio.txt'
            
        elif dificultad == 'DIFICIL':
            filename = 'palabras_dificil.txt'
    
        self.elegir_palabra_secreta(filename)

    def elegir_palabra_secreta(self,filename):
        with open(filename) as archivo_objeto:
            lineas = archivo_objeto.readlines()
            palabra_secreta = random.choice(lineas)
            self.palabra_secreta = palabra_secreta.upper().strip() 
            self.longitud = len(self.palabra_secreta) 
            
        self.label1.place_forget()
        #self.buttond_frame.pack_forget()

        self.ventana_dibujo()
        

    def ventana_dibujo (self):
        self.ventana2 = Frame(self.ventana,width=400,height=400,bg='white')
        self.ventana2.pack(pady=20)

        self.mostrar_palabra = Label(self.ventana,text=" _ " * self.longitud,font=('arial',30),bg='white')
        self.mostrar_palabra.pack(pady=10)
        
        self.botones_del_alfabeto()

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
            self.mostrar_mensajes(f'LO SENTIMOS!, HA CONSUMIDO TODOS LOS INTENTOS, LA PALABRA SECRETA ERA {self.palabra_secreta}')


    def mostrar_mensajes(self,mensaje):

        self.ventana_botones_alfabeto.pack_forget() # quitar botones del alfabero para mostrar mensajes

        self.mensajes_fin_juego = Label(self.ventana,text=mensaje,fg= 'red')
        self.mensajes_fin_juego.pack(pady=15)    
              

def main():
    root = Tk()
    app = JuegoDelAhorcado(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
