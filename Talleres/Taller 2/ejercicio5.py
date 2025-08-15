import numpy as np
'''
Ejercicio 5: Funciones de agregación
Crea un array con valores enteros del 1 al 20 y calcula:
1. La suma total.
2. El valor máximo y mínimo.
3. El promedio.
4. La desviación estándar (np.std()).
'''
arr = np.arange(1, 21)
print("Suma total:", np.sum(arr))
print("Valor maximo:", np.max(arr))
print("Valor minimo:", np.min(arr))
print("Promedio:", np.mean(arr))
print("Desviacion estandar:", np.std(arr))
