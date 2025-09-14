import numpy as np
import matplotlib.pyplot as plt 
'''
Elaborar una función a la que se le envié de una imagen y
retorne la imagen en Amarillo
'''
def amarillo(imagen):
    imagen_copia = imagen.copy()
    imagen_copia[:,:,2] = 0 # Cancelar capa azul
    return imagen_copia

img = plt.imread("images_taller/logo_utp.jpg")/255
plt.subplot(1,2,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

imagen_amarillo = amarillo(img)
plt.subplot(1,2,2)
plt.axis("off")
plt.title("En amarillo")
plt.imshow(imagen_amarillo)

plt.show()