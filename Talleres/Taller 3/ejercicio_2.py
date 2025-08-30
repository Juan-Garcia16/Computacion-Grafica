import numpy as np
import matplotlib.pyplot as plt

matriz_colores = np.zeros((7, 11, 3))
#yellow
matriz_colores[0:5,0,0] = 255
matriz_colores[0:5,0,1] = 255
#cian
matriz_colores[0:5,1:3,1] = 255
matriz_colores[0:5,1:3,2] = 255
#green
matriz_colores[0:5,3:5,1] = 255
#magenta
matriz_colores[0:5,5:7,0] = 255
matriz_colores[0:5,5:7,2] = 255
#red
matriz_colores[0:5,7:9,0] = 255
#blue
matriz_colores[0:5,9:11,2] = 255

for i in range(11):
    incremento = 1 - ((i + 1) / 11)
    matriz_colores[5:7,i:i+1,0] = incremento 
    matriz_colores[5:7,i:i+1,1] = incremento
    matriz_colores[5:7,i:i+1,2] = incremento

plt.imshow(matriz_colores)
plt.axis("off")
plt.title("Figura 2")
plt.show()