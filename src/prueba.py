import random as random
i = 1
palabras_secretas = []
filename = 'palabras.txt'
with open(filename) as archivo_objeto:
    lineas = archivo_objeto.readlines()

#for i in range(len(lineas)):
#    palabras_secretas.add(lineas[i])

palabras_secreta = random.choice(lineas)
print (palabras_secreta) 
