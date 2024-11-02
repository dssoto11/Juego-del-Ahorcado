from tkinter import *
import random as random
import unicodedata
from PIL import ImageTk, Image

root = Tk()
root.title('imagen')

imagen = Image.open('ahorcado2.png')
imagen = ImageTk.PhotoImage(imagen)
label1 = Label(image=imagen)
label1.pack()


root.mainloop()












