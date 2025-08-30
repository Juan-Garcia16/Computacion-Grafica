import numpy as np
import matplotlib.pyplot as plt 
'''
Elaborar una función a la que se le envié de una imagen y retorne la imagen en Magenta
'''
def magenta(imagen):
    imagen[:,:,1] = 0 # Cancelar capa verde
    return imagen

img = plt.imread("images_taller/logo_utp.jpg")/255
plt.subplot(1,2,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

imagen_magenta = magenta(img)
plt.subplot(1,2,2)
plt.axis("off")
plt.title("En magenta")
plt.imshow(imagen_magenta)

plt.show()