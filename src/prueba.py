import random as random

palabras_secretas = []
filename = 'palabras.txt'
with open(filename) as archivo_objeto:
    lineas = archivo_objeto.readlines()

palabras_secreta = random.choice(lineas)
print (palabras_secreta) 
