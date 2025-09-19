import numpy as np
import matplotlib.pyplot as plt

'''PATRONES IZQUIERDA'''
matriz_colores = np.zeros((10, 10, 3)) 

#Seccion vertical izquierda
matriz_colores[1:9,0,0] = 1 #rojo
matriz_colores[1:9,1,1] = 1 #verde
matriz_colores[1:9,2,2] = 1 #azul

#Seccion superior derecha
matriz_colores[1:4,3:5,0] = 1
matriz_colores[1:4,3:5,1] = 1 #amarillo

matriz_colores[1:4,5:8,0] = 1
matriz_colores[1:4,5:8,2] = 1 #magenta

matriz_colores[1:4,8:10,1] = 255
matriz_colores[1:4,8:10,2] = 255 #cyan

#Seccion horizontal inferior derecha
for i in range(5):
    matriz_colores[4 + i, 3:] = 0.9 - i * 0.1 #escala de grises entre 0.9 y 0.5

plt.figure("Figura 1")
plt.imshow(matriz_colores)
plt.axis("off")
plt.title("Patrón Izquierda")
plt.show()