import matplotlib.pyplot as plt
import numpy as np
import Clases.imgPro as proImg

img1 = plt.imread('images_taller/github.webp') / 255
img2 = plt.imread('images_taller/fondo.jpg') / 255
img3 = plt.imread('images_taller/silksong.jpeg') / 255

print(img1.shape)
print(img2.shape)
print(img3.shape)


img_a = proImg.crop(img3, 430, 150, 750, 400)
img_b = img3

img_c = proImg.bright_layer(img3, -1, 2)

print()
print(img_a.shape)
print(img_b.shape)


plt.figure(figsize=(12, 6))  # 12 pulgadas de ancho, 6 de alto
plt.subplot(1,3,1)
plt.imshow(img_a)
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(img_b)
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(img_c)
plt.axis('off')

plt.show()