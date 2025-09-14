import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envie de una imagen retorne su capa azul
'''
def capa_azul(imagen):
    capa = imagen.copy()
    capa[:,:,0] = 0 # Cancelar capa roja
    capa[:,:,1] = 0 # Cancelar capa verde
    return capa

img = plt.imread("images_taller/logo_utp.jpg")/255
plt.subplot(1,2,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

capa_azul = capa_azul(img)
plt.subplot(1,2,2)
plt.axis("off")
plt.title("Capa azul")
plt.imshow(capa_azul)

plt.show()
    