
import numpy as np
import matplotlib.pyplot as plt
# Cargar imagen
img = plt.imread('images_taller/logo_utp.jpg')
#Asegurar que los valores estén entre 0-255
if img.max() <= 1.0:
    img = (img * 255).astype(np.uint8)
    
#Separar canales
R = img[..., 0]
G = img[..., 1]
B = img[..., 2]

#Crear figura para mostrar los histogramas por canal
plt.figure(figsize=(10, 6))
    
# Histograma canal rojo
plt.subplot(3, 1, 1)
plt.hist(R.ravel(), bins=256, color='red', alpha=0.7)
plt.title('Histograma del canal Rojo')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')

# Histograma canal verde
plt.subplot(3, 1, 2)
plt.hist(G.ravel(), bins=256, color='green', alpha=0.7)
plt.title('Histograma del canal Verde')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')

# Histograma canal azul
plt.subplot(3, 1, 3)
plt.hist(B.ravel(), bins=256, color='blue', alpha=0.7)
plt.title('Histograma del canal Azul')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()