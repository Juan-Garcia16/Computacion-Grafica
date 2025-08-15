import numpy as np

def ejercicio1():
    '''
    Ejercicio 1: Creación de arrays
    Crea un array 1D con los valores [12, 45, 78, 34, 56] y:
    1. Muestra el array.
    2. Muestra su tipo de datos (dtype).
    3. Muestra el número de dimensiones (ndim) y su forma (shape).
    '''
    print("\n--- EJERCICIO 1 ---")
    arr_1d = np.array([12, 45, 78, 34, 56])
    print("Array:", arr_1d)
    print("Tipo de datos:", arr_1d.dtype)
    print("Dimension:", arr_1d.ndim)
    print("Forma (shape):", arr_1d.shape)

def ejercicio2():
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
    print("\n--- EJERCICIO 2 ---")
    lista = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    arr_2d = np.array(lista) 
    print("Cantidad de elementos:", arr_2d.size)

    arr_float32 = np.array(arr_2d, dtype=np.float32)
    print("Nuevo array tipo float32:\n", arr_float32)

def ejercicio3():
    '''
    Ejercicio 3: Arrays especiales
    Usa funciones de NumPy para:
    1. Crear un array de ceros de tamaño (2, 4).
    2. Crear un array de unos de tamaño (3, 3).
    3. Crear un array con valores del 10 al 50, con paso de 5.
    4. Crear un array con 8 valores equidistantes entre 0 y 1.
    '''
    print("\n--- EJERCICIO 3 ---")
    arr_zeros = np.zeros((2, 4))
    arr_unos = np.ones((3, 3))
    arr_paso5 = np.arange(10, 51, 5)
    arr_equidistante = np.linspace(0, 1, 8)

    print("\nArray de ceros (2,4):\n", arr_zeros)
    print("\nArray de unos (3,3):\n", arr_unos)
    print("\nArray con paso 5:", arr_paso5)
    print("Array equidistante:", arr_equidistante)

def ejercicio4():
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
    print("\n--- EJERCICIO 4 ---")
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

def ejercicio5():
    '''
    Ejercicio 5: Funciones de agregación
    Crea un array con valores enteros del 1 al 20 y calcula:
    1. La suma total.
    2. El valor máximo y mínimo.
    3. El promedio.
    4. La desviación estándar (np.std()).
    '''
    print("\n--- EJERCICIO 5 ---")
    arr = np.arange(1, 21)
    print("Suma total:", np.sum(arr))
    print("Valor maximo:", np.max(arr))
    print("Valor minimo:", np.min(arr))
    print("Promedio:", np.mean(arr))
    print("Desviacion estandar:", np.std(arr))

def ejercicio6():
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
    print("\n--- EJERCICIO 6 ---")
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

def ejercicio7():
    '''
    Ejercicio 7: Números aleatorios
    Usa np.random para:
    1. Generar 10 números aleatorios entre 0 y 1.
    2. Generar una matriz 4x4 con enteros aleatorios entre 50 y 100.
    3. Generar 1000 valores con distribución normal y mostrar su promedio y desviación
    estándar.
    '''
    print("\n--- EJERCICIO 7 ---")
    arr_random = np.random.rand(10)
    print(arr_random)

    matriz_random = np.random.randint(50, 101, size=(4, 4))
    print("Matriz Random:\n", matriz_random)

    #Distribucion normal (loc->media, scale->desviacion estandar, size->cantidad de valores)
    normal = np.random.normal(loc=0, scale=1.0, size=1000)
    print("Promedio 1000 valores:", np.mean(normal))
    print("Desviacion Estandar:", np.std(normal))

def mostrar_menu():
    print("\n" + "="*50)
    print("     MENÚ DE EJERCICIOS - TALLER 2 NUMPY")
    print("="*50)
    print("1. Ejercicio 1 - Creación de arrays")
    print("2. Ejercicio 2 - Arrays 2D y propiedades")
    print("3. Ejercicio 3 - Arrays especiales")
    print("4. Ejercicio 4 - Operaciones matemáticas")
    print("5. Ejercicio 5 - Funciones de agregación")
    print("6. Ejercicio 6 - Indexación y slicing")
    print("7. Ejercicio 7 - Números aleatorios")
    print("8. Ejecutar todos los ejercicios")
    print("0. Salir")
    print("="*50)

def ejecutar_todos():
    print("\n" + "="*50)
    print("     EJECUTANDO TODOS LOS EJERCICIOS")
    print("="*50)
    ejercicios = [ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5, ejercicio6, ejercicio7]
    for ejercicio in ejercicios:
        ejercicio()
        print("\n" + "-"*30)

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSelecciona una opción (0-8): "))
            
            if opcion == 0:
                print("\n¡Hasta luego!")
                break
            elif opcion == 1:
                ejercicio1()
            elif opcion == 2:
                ejercicio2()
            elif opcion == 3:
                ejercicio3()
            elif opcion == 4:
                ejercicio4()
            elif opcion == 5:
                ejercicio5()
            elif opcion == 6:
                ejercicio6()
            elif opcion == 7:
                ejercicio7()
            elif opcion == 8:
                ejecutar_todos()
            else:
                print("\n❌ Opción no válida. Por favor, selecciona un número del 0 al 8.")
        
        except ValueError:
            print("\n❌ Por favor, ingresa un número válido.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
