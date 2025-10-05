
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# def rotateImg(a, ang):
#     """
#     Rota una imagen en sentido antihorario por un ángulo dado.
#     Parámetros:
#     a (numpy.ndarray): Imagen de entrada representada como un arreglo 2D.
#     ang (float): Ángulo de rotación en grados. Debe estar en el rango (0, π] radianes.
#     Devuelve:
#     numpy.ndarray: Imagen rotada con el mismo tipo de datos que la imagen de entrada.
#     Excepciones:
#     ValueError: Si el ángulo está fuera del rango esperado (0 < ang <= π).
#     Notas:
#     - La función convierte el ángulo de grados a radianes internamente.
#     - La imagen de salida tendrá dimensiones ajustadas para contener la imagen rotada.
#     - La rotación se realiza en sentido antihorario.
#     """
#     ang = np.radians(ang)  # Convertir a radianes
#     m, n = a.shape
#     cos_ang = np.cos(ang)
#     sin_ang = np.sin(ang)

#     if ang > 0 and ang <= np.pi / 2:
#         c = int(round(m * sin_ang + n * cos_ang)) + 1
#         d = int(round(m * cos_ang + n * sin_ang)) + 1
#         b = np.zeros((c, d), dtype=a.dtype)
#         for i in range(c):
#             for j in range(d):
#                 iii = i - int(n * sin_ang) - 1
#                 ii = int(round(j * sin_ang - iii * cos_ang))
#                 jj = int(round(j * cos_ang + iii * sin_ang))
#                 if 0 <= ii < m and 0 <= jj < n:
#                     b[i, j] = a[ii, jj]
#     elif ang > np.pi / 2 and ang <= np.pi:
#         c = int(round(m * sin_ang - n * cos_ang)) + 1
#         d = int(round(m * cos_ang + n * sin_ang)) + 1
#         e = -n * cos_ang
#         b = np.zeros((c, d), dtype=a.dtype)
        
#         for i in range(c):
#             iii = c - i - 1
#             for j in range(d):
#                 jjj = d - j - 1
#                 ii = int(round(jjj * sin_ang + iii * cos_ang))
#                 jj = int(round(jjj * cos_ang - iii * sin_ang))
#                 if 0 <= ii < m and 0 <= jj < n:
#                     b[i, j] = a[ii, jj]
#     else:
#         raise ValueError("Ángulo fuera del rango esperado (0 < ang <= π)")

#     return b


def rotateImg(a, ang):
    ang = np.radians(ang)
    m, n = a.shape
    cos_ang = np.cos(ang)
    sin_ang = np.sin(ang)

    # Calcular dimensiones del nuevo lienzo
    c = int(abs(m * sin_ang) + abs(n * cos_ang)) + 1
    d = int(abs(m * cos_ang) + abs(n * sin_ang)) + 1

    # Crear nueva imagen vacía
    b = np.zeros((c, d), dtype=a.dtype)

    # Centro de la imagen original y la nueva
    cx, cy = m / 2, n / 2
    ncx, ncy = c / 2, d / 2

    # Transformación inversa
    for i in range(c):
        for j in range(d):
            # Coordenadas relativas al centro de la nueva imagen
            x = i - ncx
            y = j - ncy

            # Rotación inversa (antihorario)
            ii =  cos_ang * x + sin_ang * y
            jj = -sin_ang * x + cos_ang * y

            # Volver a coordenadas de la imagen original
            ii = int(round(ii + cx))
            jj = int(round(jj + cy))

            # Si está dentro del rango original
            if 0 <= ii < m and 0 <= jj < n:
                b[i, j] = a[ii, jj]

    return b


img = plt.imread("images_taller/github.webp")/255
if img.ndim == 3:
    img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

# === Lista de ángulos notables ===
angulos = [0, 30, 45, 60, 90, 120, 135, 150, 180]

# === Mostrar resultados ===
fig, axes = plt.subplots(3, 3, figsize=(12, 12))
fig.suptitle("Rotación en ángulos notables", fontsize=16)

for idx, ang in enumerate(angulos):
    rotada = rotateImg(img, ang)
    ax = axes[idx // 3, idx % 3]
    ax.imshow(rotada, cmap='gray')
    ax.set_title(f"{ang}°")
    ax.axis("off")

plt.tight_layout()
plt.show()

img = plt.imread("images_taller/github.webp")/255
if img.ndim == 3:
    img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

# === Lista de ángulos notables ===
angulos = [210, 225, 240, 270, 300, 315, 330, 360]

# === Mostrar resultados ===
fig, axes = plt.subplots(3, 3, figsize=(12, 12))
fig.suptitle("Rotación en ángulos notables", fontsize=16)

for idx, ang in enumerate(angulos):
    rotada = rotateImg(img, ang)
    ax = axes[idx // 3, idx % 3]
    ax.imshow(rotada, cmap='gray')
    ax.set_title(f"{ang}°")
    ax.axis("off")

plt.tight_layout()
plt.show()