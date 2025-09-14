import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envié una imagen y que
retorne la imagen en escala de grises con la técnica de promedio
(Average)
'''
def average_grays(imagen):
    return (imagen[:,:,0] + imagen[:,:,1] + imagen[:,:,2]) / 3


img = plt.imread("images_taller/logo_utp.jpg")/255
imagen_promedio = average_grays(img)

plt.axis("off")
plt.title("Escala de grises (Average)")
plt.imshow(imagen_promedio, cmap='gray')
plt.show()