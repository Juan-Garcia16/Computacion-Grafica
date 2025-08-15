import numpy as np
'''
Ejercicio 6: Indexación y slicing
Dado el array:
[[5, 10, 15],
[20, 25, 30],
[35, 40, 45],
[50, 55, 60]]
Realiza:
1. Extrae la primera columna.
2. Extrae la tercera fila.
3. Obtén una submatriz de las últimas dos filas y las últimas dos columnas.
'''

lista = [[5, 10, 15],
        [20, 25, 30],
        [35, 40, 45],
        [50, 55, 60]]

arr_2d = np.array(lista)
arr_columna1 = arr_2d[:, 0]
arr_fila3 = arr_2d[2, :]
submatriz = arr_2d[2:, 1:]

print("Primera columna:", arr_columna1)
print("Tercera fila:", arr_fila3)
print("Submatriz:\n", submatriz)


