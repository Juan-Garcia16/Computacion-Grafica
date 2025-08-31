import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envié 2 imágenes y que me
retorne la fusión de las dos imágenes sin ecualizar
'''
def fusion_imagenes(img1, img2):
    imagen_fusionada = (img1 + img2) / 2
    return imagen_fusionada

imagen1 = plt.imread("images_taller/github.webp")/255
imagen2 = plt.imread("images_taller/fondo.jpg")/255
imagen_fusionada = fusion_imagenes(imagen1, imagen2)

plt.subplot(1, 3, 1)
plt.axis("off")
plt.title("Imagen 1")
plt.imshow(imagen1)

plt.subplot(1, 3, 2)
plt.axis("off")
plt.title("Imagen 2")
plt.imshow(imagen2)

plt.subplot(1, 3, 3)
plt.axis("off")
plt.title("Fusionada")
plt.imshow(imagen_fusionada)

plt.show()
