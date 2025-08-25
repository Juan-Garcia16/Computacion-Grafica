import numpy as np
import matplotlib.pyplot as plt

cyan = [0, 1, 1]
white = [1, 1, 1]
red = [1, 0, 0]
magenta = [1, 0, 1]
gray = [0.5, 0.5, 0.5]
green = [0, 1, 0]
yellow = [1, 1, 0]
black = [0, 0, 0]
blue = [0, 0, 1]

matriz_colores = np.array([
    [cyan,   white,  red],
    [magenta, gray,  green],
    [yellow, black,  blue]
])

plt.imshow(matriz_colores)
plt.axis("off") 
plt.title("Matriz de colores")
plt.show()