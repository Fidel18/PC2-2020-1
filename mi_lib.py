#FUNCION PARA GENERAR UN ARREGLO DE LISTA 2D
m=int(input("Ingrese número de filas: "))
n=int(input("Ingrese número de columnas: "))

from numpy import random
x = random.randint(100, size=(m,n))

print(x)

#FUNCION PARA MOVER COLUMNA

import numpy as np

print(np.sort(x, axis= 1))