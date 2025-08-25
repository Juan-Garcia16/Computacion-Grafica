import numpy as np
import matplotlib.pyplot as plt

# gold = [0.65, 0.65, 0]
# cyan = [0, 0.65, 0.65]
# green = [0, 0.65, 0]
# magenta = [0.65, 0, 0.65]
# red = [0.65, 0, 0]
# blue = [0, 0, 0.65]
# black0 = [0, 0, 0]
# black1 = [0.05, 0.05, 0.05]
# black2 = [0.1, 0.1, 0.1]
# black3 = [0.15, 0.15, 0.15]
# black4 = [0.2, 0.2, 0.2]
# black5 = [0.25, 0.25, 0.25]
# black6 = [0.3, 0.3, 0.3]
# black7 = [0.35, 0.35, 0.35]
# black8 = [0.4, 0.4, 0.4]
# black9 = [0.45, 0.45, 0.45]
# black10 = [0.5, 0.5, 0.5]

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

# matriz_colores[5:6,0:2,2] = 255
# matriz_colores[5:6,0:3,2] = 255
# matriz_colores[5:6,0:4,2] = 255
# matriz_colores[5:6,0:5,2] = 255
# matriz_colores[5:6,0:6,2] = 255
# matriz_colores[5:6,0:7,2] = 255
# matriz_colores[5:6,0:8,2] = 255
# matriz_colores[5:6,0:9,2] = 255
# matriz_colores[5:6,0:10,2] = 255
# matriz_colores[5:6,0:11,2] = 255




# matriz_colores = np.array([
#     [gold, cyan, cyan, green, green, magenta, magenta, red, red, blue, blue],
#     [gold, cyan, cyan, green, green, magenta, magenta, red, red, blue, blue],
#     [gold, cyan, cyan, green, green, magenta, magenta, red, red, blue, blue],
#     [gold, cyan, cyan, green, green, magenta, magenta, red, red, blue, blue],
#     [gold, cyan, cyan, green, green, magenta, magenta, red, red, blue, blue],
#     [black10, black9, black8, black7, black6, black5, black4, black3, black2, black1, black0]

# ])

plt.imshow(matriz_colores)
plt.axis("off")
plt.title("Figura 2")
plt.show()