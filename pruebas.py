texto = "Hola Mundo  "
print("Original:", repr(texto))
print("Longitud:", len(texto))
print("Minuscula:", texto.lower())
print("Mayuscula:", texto.upper())
print("Sin espacio:", texto.strip())
print("split", texto.split())

lista = ["hola", "mundo", 27]
print("find('Mun'):", texto.find("Mun"))

frase = "uno,dos,tres"
partes = frase.split(",")                # ['uno', 'dos', 'tres']
print("\n\nsplit(',') ->", partes)
unido = " - ".join(partes)               # "uno - dos - tres"
print("join ->", unido)

unido2 = ": ".join(partes)
print("join ->", unido2)

s = "Python"
print("\n\ns[0:2] ->", s[0:2])   # 'Py' (desde 0 hasta 2 sin incluirlo)
print("s[:3]  ->", s[:3])    # 'Pyt'
print("s[3:]  ->", s[3:])    # 'hon'
#Primer taller entregado
