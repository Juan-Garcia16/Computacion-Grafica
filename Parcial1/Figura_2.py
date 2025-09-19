import numpy as np
import matplotlib.pyplot as plt

'''PATRONES DERECHA'''
matriz_colores = np.zeros((13, 13, 3)) 

#Linea vertical central
matriz_colores[0:,6,2] = 1 #azul

#linea horizontal central
matriz_colores[6,0:,1] = 1 #verde

#Cuadro rojo central
matriz_colores[5:8,5:8,0] = 1 
matriz_colores[5:8,5:8,1] = 0 
matriz_colores[5:8,5:8,2] = 0 #rojo

#Cuadro blanco central
matriz_colores[6,6] = 1 #blanco

#Cuadro superior izquierdo
matriz_colores[1:5,1:5,1] = 1
matriz_colores[1:5,1:5,2] = 1 #cyan

#Cuadro inferior izquierdo
matriz_colores[8:12,1:5,0] = 1
matriz_colores[8:12,1:5,1] = 1 #amarillo

#Cuadro superior derecho
matriz_colores[1,8:12] = 0.5
matriz_colores[4,8:12] = 0.5 #grises horizontales

matriz_colores[2:4,8] = 0.8
matriz_colores[2:4,11] = 0.8 #grises verticales

#Cuadro inferior derecho
matriz_colores[8:12,8:12,0] = 1
matriz_colores[8:12,8:12,2] = 1 #magenta

plt.figure("Figura 2")
plt.imshow(matriz_colores)
plt.axis("off")
plt.title("Patrón Derecha")
plt.show()