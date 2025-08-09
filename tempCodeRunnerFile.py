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
    
    print("\nEl número total de palabras:", num_palabras)
    print("El número total de letras:", num_letras)
    print("La palabra más larga:", palabra_larga)