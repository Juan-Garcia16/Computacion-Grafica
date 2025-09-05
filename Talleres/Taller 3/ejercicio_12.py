import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envié 2 imágenes y que me
retorne la fusión de las dos imágenes ecualizadas
'''
def fusion_imagenes_ecualizadas(img1, img2):
    factor = 0.4
    imagen_fusionada = ((img1 + img2) * factor)/ 2
    return imagen_fusionada


imagen1 = plt.imread("images_taller/github.webp")/255
imagen2 = plt.imread("images_taller/fondo.jpg")/255

plt.subplot(1, 3, 1)
plt.axis("off")
plt.title("Imagen 1")
plt.imshow(imagen1)

plt.subplot(1, 3, 2)
plt.axis("off")
plt.title("Imagen 2")
plt.imshow(imagen2)

imagen_ecualizada = fusion_imagenes_ecualizadas(imagen1, imagen2)
plt.subplot(1, 3, 3)
plt.title("Imagen ecualizada")
plt.axis('off')
plt.imshow(imagen_ecualizada)
plt.show()