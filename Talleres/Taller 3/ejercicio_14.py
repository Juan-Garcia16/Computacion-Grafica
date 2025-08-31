import numpy as np
import matplotlib.pyplot as plt
'''
Elaborar una función a la que se le envie una imagen y que
retorne la imagen con la Técnica de promedio (Average)
'''
def promedio_imagen(imagen):
    return (imagen[:,:,0] + imagen[:,:,1] + imagen[:,:,2]) / 3


img = plt.imread("images_taller/logo_utp.jpg")/255
imagen_promedio = promedio_imagen(img)

plt.axis("off")
plt.title("Imagen con Técnica de promedio")
plt.imshow(imagen_promedio)
plt.show()