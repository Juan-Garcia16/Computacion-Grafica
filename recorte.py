import numpy as np
import matplotlib.pyplot as plt

# def crop(img, xIni, yIni, xFin, yFin):
#     """
#     Deja una sección rectangular de la imagen definida por las coordenadas
#     (xIni, yIni) y (xFin, yFin), siendo esquina superior izquierda y esquina inferior derecha respectivamente.
#     """
#     temp = yIni
#     yIni = xIni
#     xIni = temp
    
#     temp = yFin
#     yFin = xFin
#     xFin = temp
    
#     img_copia = np.copy(img)
#     return img_copia[xIni:xFin, yIni:yFin]
def crop(img, xIni, yIni, xFin, yFin):
    """
    Recorta la imagen con coordenadas cartesianas (xIni, yIni) y (xFin, yFin),
    donde (xIni, yIni) es la esquina superior izquierda y (xFin, yFin) la inferior derecha.
    """
    img_copia = np.copy(img)
    # En numpy: primero van las filas (y), luego las columnas (x)
    return img_copia[yIni:yFin, xIni:xFin]


img = plt.imread('images_taller/silksong.jpeg') / 255
print(img.shape)
recorte = crop(img, 0, 0, 300, 300)
plt.figure("Recorte de imagen")
plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(img)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title("Recorte")
plt.imshow(recorte)
plt.axis('off')
plt.show()