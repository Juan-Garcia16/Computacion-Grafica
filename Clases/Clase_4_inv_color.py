import numpy as np
import matplotlib.pyplot as plt
from PIL import Image #Para sumar imagenes de distintos tamanos

#plt ya lee como array, no es necesrio np primero
img = plt.imread('imagenes/charmander.jpg')/255 #/255 para normalizar
    
imgN = 1 - img

plt.subplot(3, 3, 1)
plt.imshow(img)
plt.title("Imagen Original")
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(imgN)
plt.title("Imagen negativa")
plt.axis('off')

#Al sumar dos matrices, se obtiene una nueva matriz donde cada elemento es la suma de los elementos correspondientes de las matrices originales.
img2 = plt.imread('imagenes/pina.webp')/255

img_fus = (img + img2)/2 #sobre 2 ya que al ser del mismo tamano se pasa de 1 la suma, 1+1=2, y se saldria de la normalizacion
plt.subplot(3, 3, 3)
plt.imshow(img_fus)
plt.title("Imagen fusionada")
plt.axis('off')

#DISTINTO TAMANO
#Image ya no abre array, abre PIL
img1 = Image.open('imagenes/gato_nerd.jpg')
img2 = Image.open('imagenes/fondo.jpeg') 

img2_resize = img2.resize(img1.size) #redimensionar la segunda imagen al tamano de la primera   

img1 = np.array(img1)/255
img2_resize = np.array(img2_resize)/255

img_fusionada = (img1 + img2_resize)/2

plt.subplot(3, 3, 4)
plt.imshow(img_fusionada)
plt.title("Imagen fus resize")
plt.axis('off')


#SUMA PONDERADA DE IMAGENES (Una imagen tiene mas relevacion)
factor = 0.2
img_ponderada = img1*factor + img2_resize*(1-factor)
plt.subplot(3, 3, 5)
plt.imshow(img_ponderada)
plt.title("Imagen ponderada")
plt.axis('off')

'''
ESCALA DE GRISES
Tecnica primedio, Igris = (R + G + B) / 3
'''
img_gris1 = (img[:,:,0] + img[:,:,1] + img[:,:,2]) / 3
plt.subplot(3, 3, 6)
#En imshow se debe agregar el parametro cmap = gris para eliminar las 
#3 dimensionas y quedar en una matriz bidimensional 2 dimensiones
plt.imshow(img_gris1, cmap='gray')
plt.title("Imagen gris promedio")
plt.axis('off')

'''
Tecnica de Luminosidad (ojo humano) Igris = 0.299*R + 0.587*G + 0.114*B
'''
img_luminosidad_gris2 = 0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]
plt.subplot(3, 3, 7)
#En imshow se debe agregar el parametro cmap = gris
plt.imshow(img_luminosidad_gris2, cmap='gray')
plt.title("Img gris luminosa")
plt.axis('off')

'''
Tecnica tonalidad (Midgray) Igris = (max(R,G,B) + min(R,G,B)) / 2
'''
img_tonalidad_gris3 = (np.maximum(img[:,:,0], img[:,:,1], img[:,:,2]) + 
                       np.minimum(img[:,:,0], img[:,:,1], img[:,:,2]))/2
plt.subplot(3, 3, 8)
#En imshow se debe agregar el parametro cmap = gris
plt.imshow(img_tonalidad_gris3, cmap='gray')
plt.title("Imagen gris tonalidad")
plt.axis('off')

plt.show()


