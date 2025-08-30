import numpy as np
import matplotlib.pyplot as plt 
'''
Elaborar una función a la que se le envié de una imagen y
retorne la imagen en Cyan
'''
def cyan(imagen):
    imagen[:,:,0] = 0 # Cancelar capa roja
    return imagen

img = plt.imread("images_taller/logo_utp.jpg")/255
plt.subplot(1,2,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

imagen_cyan = cyan(img)
plt.subplot(1,2,2)
plt.axis("off")
plt.title("En cyan")
plt.imshow(imagen_cyan)

plt.show()