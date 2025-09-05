import numpy as np
import matplotlib.pyplot as plt
'''AJUSTE DE BRILLO (sobre las 3 capas)
Sumarle un valor numerico a cada pixel'''
img = plt.imread('imagenes/charmander.jpg')/255

plt.subplot(3,3,1)
plt.title('Imagen normal')
plt.axis('off')
plt.imshow(img)

brillo = 0.3
img_brillo = img + brillo
plt.subplot(3,3,2)
plt.title('Imagen con brillo')
plt.axis('off')
plt.imshow(img_brillo)

#brillo solo en la capa roja
img_copia = np.copy(img)
capa = 0 #roja

img_copia[:,:,capa] = img[:,:,capa] + brillo
plt.subplot(3,3,3)
plt.title("Brillo en capa roja")
plt.axis("off")
plt.imshow(img_copia)

'''CONTRASTE'''
contraste = 0.5
img_contraste = contraste * np.log10(1 + img)
plt.subplot(3,3,4)
plt.axis('off')
plt.title("Contraste z oscura")
plt.imshow(img_contraste)

img_contraste = contraste * np.exp(img - 1)
plt.subplot(3,3,5)
plt.axis('off')
plt.title("Contraste z clara")
plt.imshow(img_contraste)

'''Binarizar imagen'''
#Si el valor del pixel es mayor a un umbral, se pone en blanco (1), si es menor, se pone en negro (0)
img_gris = (img[:,:,0] + img[:,:,1] + img[:,:,2]) / 3
umbral = 0.5
img_binaria = (img_gris > umbral)
plt.subplot(3,3,6)
plt.axis('off')
plt.title("Imagen binaria")
plt.imshow(img_binaria, cmap='gray')

'''Recortar una imagen'''
# Definir las coordenadas del recorte
xini = 100
xfin = 420
yini = 280
yfin = 520

img_recortada = img[xini:xfin, yini:yfin]

plt.subplot(3,3,7)
plt.axis('off')
plt.title("Imagen recortada")
plt.imshow(img_recortada)

'''Bajar resolucion'''
zoom_factor = 10
zoomed = img[::zoom_factor, ::zoom_factor]
print('tamaño imagen original: ', img.shape)
print('tamaño imagen con menor resolucion: ', zoomed.shape)

plt.subplot(3,3,8)
plt.axis('off')
plt.title("Menor resolucion")
plt.imshow(zoomed)


plt.show()

