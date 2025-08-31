import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envié una imagen y que
retorne la imagen en escala de grises con la técnica de La tonalidad
(Midgray)
'''
def midgray_grays(imagen):
    midgray = (np.maximum(img[:,:,0], img[:,:,1], img[:,:,2]) +
               np.minimum(img[:,:,0], img[:,:,1], img[:,:,2]))/2
    return midgray

img = plt.imread("images_taller/logo_utp.jpg")/255
imagen_tonalidad = midgray_grays(img)

plt.axis('off')
plt.title("Tonalidad en escala de grises")
plt.imshow(imagen_tonalidad, cmap='gray')
plt.show()
