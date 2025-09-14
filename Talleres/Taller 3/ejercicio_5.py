import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envie de una imagen retorne su capa verde
'''
def capa_verde(imagen):
    capa = imagen.copy()
    capa[:,:,0] = 0 #Cancelar capa roja
    capa[:,:,2] = 0 #Cancelar capa azul
    return capa

img = plt.imread("images_taller/logo_utp.jpg")/255
plt.subplot(1,2,1)
plt.axis("off")
plt.title("Original")
plt.imshow(img)

capa_verde = capa_verde(img)
plt.subplot(1,2,2)
plt.axis('off') 
plt.title("Capa verde")
plt.imshow(capa_verde)

plt.show()