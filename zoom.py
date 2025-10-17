import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt
# Leer y normalizar la imagen
img1= plt.imread('images_taller/silksong.jpeg') / 255
# Coordenadas para recortar el centro (por ejemplo, un recorte de 100x100)
import numpy as np

def zoomImg(img, factor=2):
    """
    Realiza un zoom simple centrado en la imagen.
    factor > 1 amplía el recorte (zoom in).
    """
    h, w = img.shape[:2]
    zoom_area_h = int(h / factor)
    zoom_area_w = int(w / factor)

    start_row = h // 2 - zoom_area_h // 2
    end_row = h // 2 + zoom_area_h // 2
    start_col = w // 2 - zoom_area_w // 2
    end_col = w // 2 + zoom_area_w // 2

    cropped = img[start_row:end_row, start_col:end_col]

    # Aumentar tamaño
    zoomed = np.kron(cropped, np.ones((factor, factor, 1)))

    return zoomed
zoomed = zoomImg(img1, factor=1)
# Mostrar resultados
plt.figure("Zoom hacia adentro")
plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(img1)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title("Zoom sobre región central")
plt.imshow(zoomed)
plt.axis('off')
plt.show()

