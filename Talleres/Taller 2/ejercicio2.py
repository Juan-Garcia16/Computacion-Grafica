import numpy as np
'''
Ejercicio 2: Arrays 2D y propiedades
Crea un array 2D con la siguiente lista de listas:
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
Luego:
1. Muestra el número de elementos (size).
2. Cambia el tipo de datos a float32.
3. Muestra el nuevo array.
'''
lista = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

arr_2d = np.array(lista) 
print("Cantidad de elementos:", arr_2d.size)

arr_float32 = np.array(arr_2d, dtype=np.float32)
print("Nuevo array tipo float32:\n", arr_float32)