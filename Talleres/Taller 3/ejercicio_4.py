import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envie de una imagen retorne su capa Roja
'''
def capa_roja(imagen):
    capa = imagen.copy()
    capa[:,:,1] = 0 #Cancelar capa verde
    capa[:,:,2] = 0 #Cancelar capa azul
    return capa

img = plt.imread("images_taller/logo_utp.jpg")/255
plt.subplot(1,2,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

capa_roja = capa_roja(img)
plt.subplot(1,2,2)
plt.axis('off') 
plt.title("Capa roja")
plt.imshow(capa_roja)

plt.show()

