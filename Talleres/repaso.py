import numpy as np
import matplotlib.pyplot as plt

matriz_colores = np.zeros((10, 10, 3)) #10 filas, 10 columnas y 3 canales (RGB)

matriz_colores[1,2:8,0] = 255 #red
matriz_colores[2,2:8,1] = 255 #green
matriz_colores[3,2:8,2] = 255 #blue

matriz_colores[4:6,2:8,:] = 0.5

matriz_colores[6,2:8,1] = 255 
matriz_colores[6,2:8,2] = 255 #cyan

matriz_colores[7,2:8,0] = 255 
matriz_colores[7,2:8,2] = 255 #magenta

matriz_colores[8,2:8,0] = 255 
matriz_colores[8,2:8,1] = 255 #yellow

matriz_colores[1:9,1,0] = 255 
matriz_colores[1:9,1,1] = 255 
matriz_colores[1:9,1,2] = 255 #white

matriz_colores[1:9,8,0] = 255
matriz_colores[1:9,8,1] = 255 
matriz_colores[1:9,8,2] = 255 #white


plt.imshow(matriz_colores)
plt.axis("off")
plt.title("Figura 1")
plt.show()