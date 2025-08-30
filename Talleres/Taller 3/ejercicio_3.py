import numpy as np
import matplotlib.pyplot as plt

'''Elaborar una función que invierta los colores de una imagen'''
def invertir_colores(imagen):
    return 1 - imagen

img_original = plt.imread("images_taller/logo_utp.jpg")/255
img_invertida = invertir_colores(img_original)

plt.subplot(1, 2, 1)
plt.imshow(img_original)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_invertida)
plt.title("Invertida")
plt.axis("off")

plt.show()

