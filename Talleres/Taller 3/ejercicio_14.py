import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envié una imagen y que
retorne la imagen en escala de grises con la técnica de Luminosidad
(Luminosity)
'''

def luminosity_grays(imagen):
    return 0.299*imagen[:,:,0] + 0.587*imagen[:,:,1] + 0.114*imagen[:,:,2]

img = plt.imread("images_taller/logo_utp.jpg")/255
imagen_luminosidad = luminosity_grays(img)

plt.axis("off")
plt.title("Escala de grises (Luminosity)")
plt.imshow(imagen_luminosidad, cmap='gray')
plt.show()

