
#Problemas de Aplicación
'''
Problema 1: Calculadora básica
Haz un programa que pida dos números y luego pregunte qué operación (+, -, *, /) desea
realizar. Muestra el resultado de la operación elegida.
'''
def ejercicio1():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    print("Qué operación desea realizar (seleccione por numero): ")
    print("1. Suma(+) \n2. Resta(-) \n3. Multiplicación(*) \n4. División(/)")
    option = int(input())
    
    if option == 1:
        print (num1 + num2)
    elif option == 2:
        print(num1 - num2)
    elif option == 3:
        print(num1 * num2)
    elif option == 4:
        print(num1 / num2)
    
    
'''
Problema 2: Gestor de tareas
Crea un programa que permita al usuario ingresar tareas una por una hasta que escriba
'salir'. Al final, muestra todas las tareas ingresadas.
'''
def ejercicio2():
    tareas = input('Ingrese una tarea o escriba "salir" para terminar: ')
    tareas = tareas.capitalize() #Para dejar el primer caracter mayus y todo lo demás minus
    lista_tareas = []
    
    while tareas != "Salir":
        lista_tareas.append(tareas)
    
    if tareas == "Salir":
        for tarea in lista_tareas:
            print(tarea)

'''
Problema 3: Contador de palabras
Pide al usuario que escriba una frase y muestra:
- El número total de palabras.
- El número total de letras.
- La palabra más larga.
'''

def ejercicio3():
    frase = input("Ingrese una frase: ")
    frase = frase.strip() #Elimina espacios al inicio y al final
    
    palabras = frase.split() #Envuelve las palabras en una lista
    num_palabras = len(palabras)
    
    letras = frase.replace(" ", "")
    num_letras = len(letras)
    
    palabra_larga = max(palabras, key=len) #Busca el mayor elemento en una lista, en este caso asigno un key para comparar con respecto a la longitud 
    
    print("El número total de palabras:", num_palabras)
    print("El número total de letras:", num_letras)
    print("La palabra más larga:", palabra_larga)
    

'''
Problema 4: Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.
'''
def ejercicio4():
    num = int(input("Ingrese un número: "))
    print("La tabla de multiplicar del 1 al 10 del número", num, "es:\n")
    
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)
    
    
'''
Problema 5: Contador de vocales
Pide una frase al usuario y cuenta cuántas vocales contiene. Muestra también el conteo de
cada vocal por separado.
'''
def ejercicio5():
    frase = input("Ingrese una frase: ")
    vocales = ["a", "e", "i", "o", "u"]
    conteo_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letra in frase:
        for vocal in vocales:
            if letra == vocal:
                if vocal == "a":
                    conteo_vocales["a"] += 1
                elif vocal == "e":
                    conteo_vocales["e"] += 1
                elif vocal == "i":
                    conteo_vocales["i"] += 1
                elif vocal == "o":
                    conteo_vocales["o"] += 1
                elif vocal == "u":
                    conteo_vocales["u"] += 1
    
    print("a =", conteo_vocales["a"])
    print("e =", conteo_vocales["e"])
    print("i =", conteo_vocales["i"])
    print("o =", conteo_vocales["o"])
    print("u =", conteo_vocales["u"])
    

def main():
    option = int(input("Ingrese el ejercicio a consultar: "))
    if option == 1:
        ejercicio1()
    elif option == 2:
        ejercicio2()
    elif option == 3:
        ejercicio3()
    elif option == 4:
        ejercicio4()
    elif option == 5:
        ejercicio5()
        
if __name__ == "__main__":
    main()

