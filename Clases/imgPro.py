import numpy as np
import matplotlib.pyplot as plt

def layer(img, capa):
    img_capa = np.zeros_like(img)
    img_capa[:,:,capa] = img[:,:, capa]
    return img_capa

def cyan(img):
    image_cyan = img.copy()
    image_cyan[:,:,0] = 0 # Cancelar capa roja
    return image_cyan

def magenta(img):
    image_magenta = img.copy()
    image_magenta[:,:,1] = 0 # Cancelar capa verde
    return image_magenta

def yellow(img):
    image_yellow = img.copy()
    image_yellow[:,:,2] = 0 # Cancelar capa azul
    return image_yellow

def reverse(img):
    image_reverse = 1 - img
    return image_reverse

def remove_layer(img, capa):
    img_copia = np.copy(img)
    img_copia[:,:,capa] = 0
    return img_copia

def fusion_images(img1, img2):
    img_fusionada = (img1 + img2) / 2
    return img_fusionada

def fusion_images_ecualized(img1, img2, factor):
    img_fusionada = factor * img1 + (1 - factor) * img2
    return img_fusionada

def average(img):
    img_copia = np.copy(img)
    return (img_copia[:,:,0] + img_copia[:,:,1] + img_copia[:,:,2]) / 3

def luminosity(img):
    img_copia = np.copy(img)
    return 0.299*img_copia[:,:,0] + 0.587*img_copia[:,:,1] + 0.114*img_copia[:,:,2]

def midgray_grays(img):
    img_copia = np.copy(img)
    midgray = (np.maximum(img_copia[:,:,0], img_copia[:,:,1], img_copia[:,:,2]) +
               np.minimum(img_copia[:,:,0], img_copia[:,:,1], img_copia[:,:,2]))/2
    return midgray

def bright(img, brillo):
    img_cop = np.copy(img)
    img_cop = img_cop + brillo * 255
    img_cop = np.clip(img_cop, 0, 255)
    return img_cop

def bright_layer(img, brillo, capa):
    img_capa = np.copy(img)
    img_capa[:,:,capa] = img[:,:,capa] + brillo
    return img_capa

def contraste_dark(img, contraste):
    img_copia = np.copy(img)
    return contraste * np.log10(1 + img_copia)

def contraste_light(img, contraste):
    img_copia = np.copy(img)
    return contraste * np.exp(img_copia - 1)

def binarize(img, umbral):
    img_copia = np.copy(img)
    img_gris = (img_copia[:,:,0] + img_copia[:,:,1] + img_copia[:,:,2]) / 3
    img_binaria = (img_gris > umbral)
    return img_binaria

def crop(img, xini, xfin, yini, yfin):
    img_copia = np.copy(img)
    return img_copia[xini:xfin, yini:yfin]

def lower_resolution(img, zoom_factor):
    img_copia = np.copy(img)
    return img_copia[::zoom_factor, ::zoom_factor]

def trasnslation(img, dx, dy):
    """
    Traslada una imagen dx píxeles en x y dy píxeles en y.
    Los píxeles que salen del borde se rellenan con negro.
    """
    trasladada = np.zeros_like(img)

    # Calcular límites válidos para el copiado
    h, w = img.shape[:2]
    x_origen_inicio = 0
    x_origen_fin = w - dx
    y_origen_inicio = 0
    y_origen_fin = h - dy

    # Asignar los valores trasladados
    trasladada[dy:h, dx:w] = img[y_origen_inicio:y_origen_fin, x_origen_inicio:x_origen_fin]

    return trasladada

def rotarImg(a, ang):
    """
    Rota una imagen en sentido antihorario por un ángulo dado.
    Parámetros:
    a (numpy.ndarray): Imagen de entrada representada como un arreglo 2D.
    ang (float): Ángulo de rotación en grados. Debe estar en el rango (0, π] radianes.
    Devuelve:
    numpy.ndarray: Imagen rotada con el mismo tipo de datos que la imagen de entrada.
    Excepciones:
    ValueError: Si el ángulo está fuera del rango esperado (0 < ang <= π).
    Notas:
    - La función convierte el ángulo de grados a radianes internamente.
    - La imagen de salida tendrá dimensiones ajustadas para contener la imagen rotada.
    - La rotación se realiza en sentido antihorario.
    """
    ang = np.radians(ang)  # Convertir a radianes
    m, n = a.shape
    cos_ang = np.cos(ang)
    sin_ang = np.sin(ang)

    if ang > 0 and ang <= np.pi / 2:
        c = int(round(m * sin_ang + n * cos_ang)) + 1
        d = int(round(m * cos_ang + n * sin_ang)) + 1
        b = np.zeros((c, d), dtype=a.dtype)
        for i in range(c):
            for j in range(d):
                iii = i - int(n * sin_ang) - 1
                ii = int(round(j * sin_ang + iii * cos_ang))
                jj = int(round(j * cos_ang - iii * sin_ang))
                if 0 <= ii < m and 0 <= jj < n:
                    b[i, j] = a[ii, jj]
    elif ang > np.pi / 2 and ang <= np.pi:
        c = int(round(m * sin_ang - n * cos_ang)) + 1
        d = int(round(m * sin_ang - n * cos_ang)) + 1
        e = -n * cos_ang
        b = np.zeros((c, d), dtype=a.dtype)
        for i in range(c):
            iii = c - i - 1
            for j in range(d):
                jjj = d - j - 1
                ii = int(round(jjj * sin_ang + iii * cos_ang))
                jj = int(round(jjj * cos_ang - iii * sin_ang))
                if 0 <= ii < m and 0 <= jj < n:
                    b[i, j] = a[ii, jj]
    else:
        raise ValueError("Ángulo fuera del rango esperado (0 < ang <= π)")

    return b