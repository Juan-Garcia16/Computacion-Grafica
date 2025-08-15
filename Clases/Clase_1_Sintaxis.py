# ========================================
# 0) IMPRIMIR (print) Y COMENTARIOS (#)
# ========================================

def seccion_0_print_y_comentarios():
    # print muestra cosas en pantalla
    print("Hola, soy Python")
    # Los comentarios (líneas que empiezan con #) NO se ejecutan.
    # Sirven para explicar el código.
    # Puedes imprimir números, textos y resultados de operaciones:
    print(2 + 3)           # suma de números
    print("Hola " * 3)     # repetir texto
    print("Edad:", 25)     # imprimir varias cosas separadas por coma
    input("\nPulsa ENTER para seguir...")


# ========================================
# 1) VARIABLES Y TIPOS BÁSICOS
# ========================================

def seccion_1_variables_y_tipos():
    # Una variable guarda un valor.
    nombre = "Ana"      # texto (string)
    edad = 20           # número entero (int)
    altura = 1.65       # número con decimales (float)
    estudiante = True   # booleano (True/False)

    print("nombre:", nombre)
    print("edad:", edad)
    print("altura:", altura)
    print("estudiante:", estudiante)

    # Saber el tipo de algo:
    print("Tipo de nombre:", type(nombre))
    # Convertir tipos (muy útil):
    edad_texto = str(edad)  # a string
    int(nombre)
    float(numero)
    print("Edad como texto:", edad_texto)

    # OJO: al convertir texto a número, el texto debe ser un número válido
    numero = int("15")      # "15" -> 15
    decimal = float("3.14") # "3.14" -> 3.14
    print("numero:", numero, "decimal:", decimal)
    input("\nPulsa ENTER para seguir...")


# ========================================
# 2) ENTRADA POR TECLADO: input()
# ========================================

def seccion_2_input():
    # input SIEMPRE devuelve TEXTO. Si quieres un número, conviértelo.
    nombre = int(input("¿Cómo te llamas? "))
    print("Hola", nombre)

    # Convertir a número con int() o float()
    edad_texto = input("¿Cuántos años tienes? ")
    # A veces la gente escribe cosas raras: usamos try/except para evitar errores
    try:
        edad = int(edad_texto)
        print("Tu edad + 1 es:", edad + 1)
    except ValueError:
        print("Eso no era un número")

    # Otro ejemplo con float (decimales)
    altura_texto = input("¿Cuánto mides (en metros, ejemplo 1.70)? ")
    try:
        altura = float(altura_texto)
        print("Perfecto, altura guardada:", altura, "m")
    except ValueError:
        print("Eso no era un número con decimales.")
    input("\nPulsa ENTER para seguir...")


# ========================================
# 3) OPERADORES
# ========================================

def seccion_3_operadores():
    a = 10
    b = 3
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", a / b)   # resultado con decimales
    print("División entera:", a // b)
    print("Módulo (resto):", a % b)
    print("Potencia:", a ** b)

    # Comparación (da True o False)
    print("a == b ?", a == b)
    print("a > b  ?", a > b)
    print("a <= b ?", a <= b)

    # Lógicos
    print("True and False ->", True and False)
    print("True or False  ->", True or False)
    print("not True       ->", not True)
    input("\nPulsa ENTER para seguir...")


# ========================================
# 4) STRINGS (textos) — MÉTODOS IMPORTANTES
# ========================================

def seccion_4_strings():
    texto = "  Hola Mundo  "
    print("Original:", repr(texto))
    print("len ->", len(texto))               # largo del texto
    print("lower ->", texto.lower())          # todo minúsculas
    print("upper ->", texto.upper())          # todo mayúsculas
    print("strip ->", texto.strip())          # quitar espacios al inicio/fin

    # Buscar y reemplazar
    print("find('Mun') ->", texto.find("Mun"))     # posición o -1 si no está
    print("replace('Mundo','Python') ->", texto.replace("Mundo", "Python"))

    # Partir y unir
    frase = "uno,dos,tres"
    partes = frase.split(",")                # ['uno', 'dos', 'tres']
    print("split(',') ->", partes)
    unido = " - ".join(partes)               # "uno - dos - tres"
    print("join ->", unido)

    # Slices (trozos)

    #[inicio:fin:paso]
    s = "Python"
    print("s[0:2] ->", s[0:2])   # 'Py' (desde 0 hasta 2 sin incluirlo)
    print("s[:3]  ->", s[:3])    # 'Pyt'
    print("s[3:]  ->", s[3:])    # 'hon'

    input("\nPulsa ENTER para seguir...")


# ========================================
# 5) LISTAS — MÉTODOS IMPORTANTES
# ========================================

def seccion_5_listas():
    numeros = [5, 2, 9]
    print("Lista:", numeros)
    numeros.append(7)       # agrega al final
    print("append(7) ->", numeros)
    numeros.insert(1, 10)   # inserta en posición 1
    print("insert(1,10) ->", numeros)
    numeros.remove(9)       # elimina el primer 9
    print("remove(9) ->", numeros)
    ultimo = numeros.pop()  # saca y devuelve el último
    print("pop() -> saca", ultimo, "lista ahora:", numeros)
    numeros.sort()          # ordena
    print("sort() ->", numeros)
    numeros.reverse()       # invierte
    print("reverse() ->", numeros)
    print("len(lista) ->", len(numeros))  # tamaño
    print("Acceso por índice [0] ->", numeros[0])  # primer elemento
    print("Slice [0:2] ->", numeros[0:2])          # sublista

    # Recorrer la lista
    print("Recorriendo con for:")
    for n in numeros:
        print(" -", n)
    input("\nPulsa ENTER para seguir...")


# ========================================
# 6) TUPLAS (como listas, pero NO cambian)
# ========================================

def seccion_6_tuplas():
    punto = (3, 4)
    print("Tupla:", punto)
    print("punto[0] ->", punto[0])
    # punto[0] = 10  # Esto DA ERROR porque la tupla es INMUTABLE
    input("\nPulsa ENTER para seguir...")


# ========================================
# 7) DICCIONARIOS — MÉTODOS IMPORTANTES
# ========================================

def seccion_7_diccionarios():
    persona = {"nombre": "Ana", "edad": 20}
    print("Diccionario:", persona)
    print("Acceso por clave ['nombre'] ->", persona["nombre"])
    print("get('altura', 'no existe') ->", persona.get("altura", "no existe"))

    persona["ciudad"] = "Bogotá"    # agregar/actualizar
    print("Agregar clave ciudad ->", persona)

    # keys, values, items
    print("keys() ->", list(persona.keys()))
    print("values() ->", list(persona.values()))
    print("items() ->", list(persona.items()))

    # update y pop
    persona.update({"edad": 21})
    print("update({'edad':21}) ->", persona)
    quitado = persona.pop("ciudad")
    print("pop('ciudad') ->", quitado, "ahora:", persona)
    input("\nPulsa ENTER para seguir...")


# ========================================
# 8) CONJUNTOS (sets) — SIN REPETIDOS
# ========================================

def seccion_8_sets():
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("a =", a)
    print("b =", b)
    a.add(2)         # ya estaba, no se duplica
    a.add(10)
    print("a.add(10) ->", a)
    # union, intersección, diferencia
    print("a | b (unión)       ->", a | b)
    print("a & b (intersección)->", a & b)
    print("a - b (diferencia)  ->", a - b)
    input("\nPulsa ENTER para seguir...")


# ========================================
# 9) IF / ELIF / ELSE (decisiones)
# ========================================

def seccion_9_if():
    try:
        n = int(input("Escribe un número: "))
    except ValueError:
        print("No era un número.")
        return

    if n > 0:
        print("Es positivo")
    elif n == 0:
        print("Es cero")
    else:
        print("Es negativo")
    input("\nPulsa ENTER para seguir...")


# ========================================
# 10) BUCLES (for y while)
# ========================================

def seccion_10_bucles():
    print("for con range(1, 6):")
    for i in range(1, 6):
        print(i, end=" ")
    print()

    print("while contando hasta 5:")
    x = 1
    while x <= 5:
        print(x, end=" ")
        x += 1
    print()

    print("Uso de break y continue:")
    for i in range(1, 10):
        if i == 3:
            continue  # salta el 3
        if i == 8:
            break     # se corta en 8
        print(i, end=" ")
    print()
    input("\nPulsa ENTER para seguir...")


# ========================================
# 11) FUNCIONES (reutilizar código)
# ========================================

def seccion_11_funciones():
    # Definir una función con parámetros y valor por defecto
    def saludar(nombre="alguien"):
        return "Hola, " + nombre

    print(saludar())            # usa el valor por defecto
    print(saludar("Carla"))     # con argumento

    # Función que calcula un cuadrado
    def cuadrado(n):
        return n * n

    print("cuadrado(5) ->", cuadrado(5))
    input("\nPulsa ENTER para seguir...")


# ========================================
# 12) ARCHIVOS (guardar y leer)
# ========================================

def seccion_12_archivos():
    # Escribir un archivo
    with open("mi_archivo.txt", "w", encoding="utf-8") as f:
        f.write("Hola desde un archivo!\nSegunda línea.")

    # Leer un archivo
    with open("mi_archivo.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
        print("Contenido del archivo:")
        print(contenido)
    input("\nPulsa ENTER para seguir...")


# ========================================
# 13) ERRORES (try / except)
# ========================================

def seccion_13_errores():
    # try/except evita que el programa se rompa por un error
    texto = input("Escribe un número para convertir a entero: ")
    try:
        n = int(texto)
        print("¡Convertido! n =", n)
    except ValueError:
        print("Eso no era un entero, pero seguimos :)")
    input("\nPulsa ENTER para seguir...")


# ========================================
# MENÚ PRINCIPAL
# ========================================

def menu():
    opciones = {
        "0": ("Print y comentarios", seccion_0_print_y_comentarios),
        "1": ("Variables y tipos", seccion_1_variables_y_tipos),
        "2": ("input()", seccion_2_input),
        "3": ("Operadores", seccion_3_operadores),
        "4": ("Strings (métodos clave)", seccion_4_strings),
        "5": ("Listas (métodos clave)", seccion_5_listas),
        "6": ("Tuplas", seccion_6_tuplas),
        "7": ("Diccionarios (métodos clave)", seccion_7_diccionarios),
        "8": ("Conjuntos (sets)", seccion_8_sets),
        "9": ("Decisiones: if/elif/else", seccion_9_if),
        "10": ("Bucles: for y while", seccion_10_bucles),
        "11": ("Funciones", seccion_11_funciones),
        "12": ("Archivos", seccion_12_archivos),
        "13": ("Errores: try/except", seccion_13_errores),
        "Q": ("Salir", None)
    }

    def mostrar_menu():
        print("\n" + "="*55)
        print("PYTHON PRINCIPIANTES — MENÚ")
        for k in ["0","1","2","3","4","5","6","7","8","9","10","11","12","13"]:
            titulo = opciones[k][0]
            print(f"{k}) {titulo}")
        print("Q) Salir")
        print("="*55)

    while True:
        mostrar_menu()
        op = input("Elige una opción: ").strip().upper()
        if op == "Q":
            print("¡Gracias por aprender Python!")
            break
        if op in opciones and opciones[op][1]:
            try:
                opciones[op][1]()
            except Exception as e:
                print("Ocurrió un error:", e)
                input("Pulsa ENTER...")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario. Adiós.")