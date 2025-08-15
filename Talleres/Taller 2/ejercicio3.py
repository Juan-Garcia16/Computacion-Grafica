import numpy as np
'''
Ejercicio 3: Arrays especiales
Usa funciones de NumPy para:
1. Crear un array de ceros de tamaño (2, 4).
2. Crear un array de unos de tamaño (3, 3).
3. Crear un array con valores del 10 al 50, con paso de 5.
4. Crear un array con 8 valores equidistantes entre 0 y 1.
'''
arr_zeros = np.zeros((2, 4))
arr_unos = np.ones((3, 3))
arr_paso5 = np.arange(10, 51, 5)
arr_equidistante = np.linspace(0, 1, 8)

print("\nArray de ceros (2,4):\n", arr_zeros)
print("\nArray de unos (3,3):\n", arr_unos)
print("\nArray con paso 5:", arr_paso5)
print("Array equidistante:", arr_equidistante)
