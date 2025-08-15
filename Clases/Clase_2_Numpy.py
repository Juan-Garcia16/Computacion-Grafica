import numpy as np #Para tratamiento de imagenes como matrices

lista = [1,2,3,4,5]
print("Lista (diferente de array):",lista)

arr = np.array(lista) #transformando la lista en array
print("\nArray:",arr)

#lista bidimensional
            #0 1 2
lista_2d = [[1,2,3], #0
            [4,5,6], #1
            [7,8,9]] #2)

print("\nLista 2d (diferente a un array 2d):\n", lista_2d)

arr_2d = np.array(lista_2d)
arr_columna1 = arr_2d[:,1] #todas las filas de la columna 1
arr_fila2 = arr_2d[2,:] #Todas las columnas de la fila 2
#[filas, columnas]

print("\nArray 2d (matriz): \n", arr_2d)
print("\nColumna1: ", arr_columna1)
print("Fila2: ", arr_fila2)

#Imprimir submatriz
print("\nSubmatriz\n",arr_2d[1:,1:]) #IMPORTANTE PARA MANEJO DE IMAGENES

#Metodos de los arrays
print("\nTamano del array: ",arr_2d.shape) #.shape(), tamano de nuestro array, (filas, columnas)
print("Dimension del array: ",arr_2d.ndim) #.ndim(), cantidad de dimensiones
print("Tipo de variables del array:",arr_2d.dtype) #Tipo de variables del array (int64)

arr_int16 = np.array(lista_2d, dtype=np.int16) #pasar a int16
print(arr_int16.dtype)

arr_zeros = np.zeros((2,3)) #generar matriz de ceros
print("\nMatriz de zeros generada:\n", arr_zeros)
arr_ones = np.ones((2,3)) #generar matris de unos
print("\nMatriz de unos generad:\n", arr_ones)

empty = np.empty((2,2))
print("\nMatriz generada con empty: \n", empty)

#Metodos para generar arrays
arr_arange = np.arange(10) #genera un arreglo desde 0 hasta n-1
print(arr_arange)
arr_arange2 = np.arange(10, 21, 2) # (inicio, final, paso)
print(arr_arange2)

linspace = np.linspace(10,21,11) #(inicio, final, cantidad de valores con misma distancia)
print("\nLinspace", linspace)

a = np.linspace(10,20,6)
b = np.linspace(5,25,6)
print("a: ", a)
print("b: ", b)

#Las operaciones se realizan valor a valor
print("\nOperacions entre a y b:")
suma = a + b
resta = a - b
multipliacion = a * b
division = a / b

print("Suma:",suma)
print("Resta:", resta)
print("Multipliacion:", multipliacion)
print("Division:", division)

print("Suma de los elementos de a:", np.sum(a))
print("Maximo de a:", np.max(a))
print("Minimo de a:", np.min(a))
print("Promedio de a:", np.mean(a))

