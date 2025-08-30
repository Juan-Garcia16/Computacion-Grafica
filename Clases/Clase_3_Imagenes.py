import numpy as np
import matplotlib.pyplot as plt #para imagenes

img = np.array(plt.imread('imagenes/gato_nerd.jpg')) #leer la imagen
print(img) #imagen matricial
print(img.shape) #tamano imagen

plt.subplot(2, 2, 1) #lienzo que quiero generar, (filas, columnas, posicion de la imagen)
plt.imshow(img)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Imagen original")

'''CAPA ROJA'''
plt.subplot(2,2,2)
imgR = np.copy(img)
imgR[:,:,1] = 0 #Cancelar capa verde
imgR[:,:,2] = 0 #Cancelar capa azul
plt.imshow(imgR)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Capa roja")

'''CAPA VERDE'''
plt.subplot(2,2,3)
imgG = np.copy(img)
imgG[:,:,0] = 0 #Cancelar capa roja
imgG[:,:,2] = 0 #Cancelar capa azul
plt.imshow(imgG)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Capa verde")

'''CAPA AZUL'''
plt.subplot(2,2,4)
imgB = np.copy(img)
imgB[:,:,0] = 0 #Cancelar capa roja
imgB[:,:,1] = 0 #Cancelar capa verde
plt.imshow(imgB)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Capa azul")
plt.show() #SOLO DEBE MOSTRARSE UNA VEZ AL FINAL

#------------

'''CAPA CYAN'''
plt.subplot(1,3,1)
imgC = np.copy(img)
imgC[:,:,0] = 0 #Cancelar capa roja
plt.imshow(imgC)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Capa Cian")

'''CAPA MAGENTA'''
plt.subplot(1,3,2)
imgM = np.copy(img)
imgM[:,:,1] = 0 #Cancelar capa verde
plt.imshow(imgM)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Capa Magenta")

'''CAPA AMARILLA'''
plt.subplot(1,3,3)
imgY = np.copy(img)
imgY[:,:,2] = 0 #Cancelar capa azul
plt.imshow(imgY)
plt.axis('off') #para quitar las medidas de visualizacion
plt.title("Capa amarilla")
plt.show()







