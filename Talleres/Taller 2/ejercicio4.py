import numpy as np
'''
Ejercicio 4: Operaciones matemáticas
Crea dos arrays 1D:
- a con valores [2, 4, 6, 8, 10]
- b con valores [1, 3, 5, 7, 9]
Realiza y muestra:
1. Suma
2. Resta
3. Multiplicación elemento a elemento
4. División elemento a element
'''
a = np.arange(2, 11, 2)
b = np.arange(1, 10, 2)

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)