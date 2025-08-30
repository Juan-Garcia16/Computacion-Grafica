import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función en la que le envie por separado las capas
RGB y con base en ellas reconstruya la imagen en colores
'''

def capa_roja(imagen):
    img = imagen.copy()
    img[:,:,1] = 0 #Cancelar capa verde
    img[:,:,2] = 0 #Cancelar capa azul
    return img

def capa_verde(imagen):
    img = imagen.copy()
    img[:,:,0] = 0 #Cancelar capa roja
    img[:,:,2] = 0 #Cancelar capa azul
    return img

def capa_azul(imagen):
    img = imagen.copy()
    img[:,:,0] = 0 # Cancelar capa roja
    img[:,:,1] = 0 # Cancelar capa verde
    return img

def imagen_a_color(capa_roja, capa_verde, capa_azul):
    imagen = capa_roja + capa_verde + capa_azul
    return imagen

img = plt.imread("images_taller/logo_utp.jpg")/255
R = capa_roja(img)
G = capa_verde(img)
B = capa_azul(img)
imagen_construida = imagen_a_color(R, G, B)

plt.subplot(1, 4, 1)
plt.axis("off")
plt.title("Capa roja")
plt.imshow(R)

plt.subplot(1, 4, 2)
plt.axis("off")
plt.title("Capa verde")
plt.imshow(G)

plt.subplot(1, 4, 3)
plt.axis("off")
plt.title("Capa azul")
plt.imshow(B)

plt.subplot(1, 4, 4)
plt.axis("off")
plt.title("Reconstruida")
plt.imshow(imagen_construida)
plt.show()

