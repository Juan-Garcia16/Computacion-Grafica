import numpy as np
import matplotlib.pyplot as plt
import Clases.imgPro as proImg

# Cargar imágenes
img1 = plt.imread('images_taller/github.webp') / 255
img2 = plt.imread('images_taller/fondo.jpg') / 255
img3 = plt.imread('images_taller/silksong.jpeg') / 255

print("=== DIMENSIONES ===")
print(f"img1: {img1.shape}")
print(f"img2: {img2.shape}") 
print(f"img3: {img3.shape}")

# ===== PRUEBAS DE FUNCIONES =====

print("\n=== PROBANDO FUNCIONES ===")

# 1. Filtros de color
cyan_img = proImg.cyan(img3)
magenta_img = proImg.magenta(img3)
yellow_img = proImg.yellow(img3)

# 2. Capas individuales
red_layer = proImg.layer(img3, 0)
green_layer = proImg.layer(img3, 1)
blue_layer = proImg.layer(img3, 2)

# 3. Conversión a escala de grises
gray_average = proImg.average(img3)
gray_luminosity = proImg.luminosity(img3)
gray_midgray = proImg.midgray(img3)

# 4. Ajustes de brillo y contraste
bright_img = proImg.bright(img3, 0.3)
dark_img = proImg.bright(img3, -0.3)
contrast_dark_img = proImg.contrast_dark(img3, 1.5)
contrast_light_img = proImg.contrast_light(img3, 2.0)

# 5. Efectos especiales
inverted_img = proImg.reverse(img3)
binary_img = proImg.binarize(img3, 0.5)

# 6. Transformaciones geométricas
cropped_img = proImg.crop(img3, 100, 400, 50, 350)
low_res_img = proImg.lower_resolution(img3, 3)
translated_img = proImg.trasnslation(img3, 50, 30)

# 7. Fusión de imágenes (solo si tienen el mismo tamaño)
try:
    fused_img = proImg.fusion_images_ecualized(img1, img2, 0.7)
    print("✅ Fusión exitosa")
except ValueError as e:
    print(f"❌ Error en fusión: {e}")

# ===== VISUALIZACIÓN =====

# Crear figura grande con múltiples subplots
fig, axes = plt.subplots(4, 4, figsize=(16, 16))
fig.suptitle('Pruebas de funciones imgPro', fontsize=16)

# Lista de imágenes y títulos para mostrar
images_to_show = [
    (img3, "Original"),
    (cyan_img, "Cyan"),
    (magenta_img, "Magenta"), 
    (yellow_img, "Yellow"),
    (red_layer, "Capa Roja"),
    (green_layer, "Capa Verde"),
    (blue_layer, "Capa Azul"),
    (gray_average, "Gris Promedio"),
    (gray_luminosity, "Gris Luminosidad"),
    (gray_midgray, "Gris Medio"),
    (bright_img, "Más Brillante"),
    (dark_img, "Más Oscura"),
    (contrast_dark_img, "Contraste Oscuro"),
    (inverted_img, "Invertida"),
    (binary_img, "Binaria"),
    (cropped_img, "Recortada")
]

# Mostrar imágenes
for idx, (img, title) in enumerate(images_to_show):
    row = idx // 4
    col = idx % 4
    axes[row, col].imshow(img, cmap='gray' if len(img.shape) == 2 else None)
    axes[row, col].set_title(title, fontsize=10)
    axes[row, col].axis('off')

plt.tight_layout()
plt.show()

# ===== PRUEBAS ESPECÍFICAS =====

# Probar brillo por capa
print("\n=== PROBANDO BRILLO POR CAPA ===")
bright_red = proImg.bright_layer(img3, 0.3, 0)  # Aumentar canal rojo
bright_green = proImg.bright_layer(img3, 0.3, 1)  # Aumentar canal verde
bright_blue = proImg.bright_layer(img3, 0.3, 2)  # Aumentar canal azul

plt.figure(figsize=(15, 4))
plt.subplot(1, 4, 1)
plt.imshow(img3)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(bright_red)
plt.title("Brillo Rojo +0.3")
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(bright_green) 
plt.title("Brillo Verde +0.3")
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(bright_blue)
plt.title("Brillo Azul +0.3")
plt.axis('off')

plt.tight_layout()
plt.show()

print("✅ ¡Todas las pruebas completadas!")
import numpy as np
import matplotlib.pyplot as plt
import Clases.imgPro as proImg

# Cargar imágenes
img1 = plt.imread('images_taller/github.webp') / 255
img2 = plt.imread('images_taller/fondo.jpg') / 255
img3 = plt.imread('images_taller/silksong.jpeg') / 255

print("=== DIMENSIONES ===")
print(f"img1: {img1.shape}")
print(f"img2: {img2.shape}") 
print(f"img3: {img3.shape}")

# ===== PRUEBAS DE FUNCIONES =====

print("\n=== PROBANDO FUNCIONES ===")

# 1. Filtros de color
cyan_img = proImg.cyan(img3)
magenta_img = proImg.magenta(img3)
yellow_img = proImg.yellow(img3)

# 2. Capas individuales
red_layer = proImg.layer(img3, 0)
green_layer = proImg.layer(img3, 1)
blue_layer = proImg.layer(img3, 2)

# 3. Conversión a escala de grises
gray_average = proImg.average(img3)
gray_luminosity = proImg.luminosity(img3)
gray_midgray = proImg.midgray(img3)

# 4. Ajustes de brillo y contraste
bright_img = proImg.bright(img3, 0.3)
dark_img = proImg.bright(img3, -0.3)
contrast_dark_img = proImg.contrast_dark(img3, 1.5)
contrast_light_img = proImg.contrast_light(img3, 2.0)

# 5. Efectos especiales
inverted_img = proImg.reverse(img3)
binary_img = proImg.binarize(img3, 0.5)

# 6. Transformaciones geométricas
cropped_img = proImg.crop(img3, 100, 400, 50, 350)
low_res_img = proImg.lower_resolution(img3, 3)
translated_img = proImg.trasnslation(img3, 50, 30)

# 7. Fusión de imágenes (solo si tienen el mismo tamaño)
try:
    fused_img = proImg.fusion_images_ecualized(img1, img2, 0.7)
    print("✅ Fusión exitosa")
except ValueError as e:
    print(f"❌ Error en fusión: {e}")

# ===== VISUALIZACIÓN =====

# Crear figura grande con múltiples subplots
fig, axes = plt.subplots(4, 4, figsize=(16, 16))
fig.suptitle('Pruebas de funciones imgPro', fontsize=16)

# Lista de imágenes y títulos para mostrar
images_to_show = [
    (img3, "Original"),
    (cyan_img, "Cyan"),
    (magenta_img, "Magenta"), 
    (yellow_img, "Yellow"),
    (red_layer, "Capa Roja"),
    (green_layer, "Capa Verde"),
    (blue_layer, "Capa Azul"),
    (gray_average, "Gris Promedio"),
    (gray_luminosity, "Gris Luminosidad"),
    (gray_midgray, "Gris Medio"),
    (bright_img, "Más Brillante"),
    (dark_img, "Más Oscura"),
    (contrast_dark_img, "Contraste Oscuro"),
    (inverted_img, "Invertida"),
    (binary_img, "Binaria"),
    (cropped_img, "Recortada")
]

# Mostrar imágenes
for idx, (img, title) in enumerate(images_to_show):
    row = idx // 4
    col = idx % 4
    axes[row, col].imshow(img, cmap='gray' if len(img.shape) == 2 else None)
    axes[row, col].set_title(title, fontsize=10)
    axes[row, col].axis('off')

plt.tight_layout()
plt.show()

# ===== PRUEBAS ESPECÍFICAS =====

# Probar brillo por capa
print("\n=== PROBANDO BRILLO POR CAPA ===")
bright_red = proImg.bright_layer(img3, 0.3, 0)  # Aumentar canal rojo
bright_green = proImg.bright_layer(img3, 0.3, 1)  # Aumentar canal verde
bright_blue = proImg.bright_layer(img3, 0.3, 2)  # Aumentar canal azul

plt.figure(figsize=(15, 4))
plt.subplot(1, 4, 1)
plt.imshow(img3)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(bright_red)
plt.title("Brillo Rojo +0.3")
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(bright_green) 
plt.title("Brillo Verde +0.3")
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(bright_blue)
plt.title("Brillo Azul +0.3")
plt.axis('off')

plt.tight_layout()
plt.show()

print("✅ ¡Todas las pruebas completadas!")