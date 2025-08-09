'''
Ejercicio 1: Variables y operadores
Crea un programa que pida al usuario dos números y muestre:
- La suma de los dos números.
- La multiplicación de los dos números.
- Si el primer número es mayor que el segundo.
'''
def ejercicio1():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    suma = num1 + num2
    multiplicacion = num1 * num2
    print(suma)
    print(multiplicacion)
    print(num1 > num2)
    
'''
Ejercicio 2: Condicionales
Pide al usuario su edad y muestra un mensaje indicando si es:
- Niño (edad <= 13)
- Adolescente (13 < edad < 18)
- Adulto (edad >= 18).
'''

def ejercicio2():
    edad = int(input("Ingrese su edad: "))
    if (edad <= 13 and edad > 0):
        print("Usted es un Niño")
    elif (edad > 13 and edad < 18):
        print("Usted es un adolescente")
    else:
        print("Usted es un adulto")

'''
Ejercicio 3: Bucles
Muestra los números del 1 al 20, omitiendo los múltiplos de 3.
'''

def ejercicio3():
    for i in range(1, 21):
        if i % 3 == 0:
            continue
        else:
            print(i)
            
'''
Ejercicio 4: Función saludo
Crea una función que reciba un nombre y una edad, y devuelva un saludo diciendo cuántos
años tendrá en 5 años.
'''

def ejercicio4():
    name = str(input("Ingrese su nombr: "))
    age = int(input("Ingrese su edad: "))
    age_5_years = age + 5
    print("Hola", name, "en 5 años tendrás", age_5_years)



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
        
        
if __name__ == "__main__":
    main()

