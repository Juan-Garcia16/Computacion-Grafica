import numpy as np
'''
Ejercicio 7: Números aleatorios
Usa np.random para:
1. Generar 10 números aleatorios entre 0 y 1.
2. Generar una matriz 4x4 con enteros aleatorios entre 50 y 100.
3. Generar 1000 valores con distribución normal y mostrar su promedio y desviación
estándar.
'''

arr_random = np.random.rand(10)
print(arr_random)

matriz_random = np.random.randint(50, 101, size=(4, 4))
print("Matriz Random:\n", matriz_random)

#Distribucion normal (loc->media, scale->desviacion estandar, size->cantidad de valores)
normal = np.random.normal(loc=0, scale=1.0, size=1000)
print("Promedio 1000 valores:", np.mean(normal))
print("Desviacion Estandar:", np.std(normal))

