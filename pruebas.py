import numpy as np
import matplotlib.pylab as plt
import imgPro as im

img = plt.imread("imagenes/charmander.jpg")/255

if img.ndim == 3:
    img = np.dot(img[..., :3], [0.299, 0.587, 0.114])

rot30 = im.rotarImg(img, 30)
rot60 = im.rotarImg(img, 60)
rot90 = im.rotarImg(img, 90)
rot120 = im.rotarImg(img, 120)
rot150 = im.rotarImg(img, 150)
rot180 = im.rotarImg(img, 180)
# rot210 = im.rotarImg(img, 210)
# rot240 = im.rotarImg(img, 240)
# rot270 = im.rotarImg(img, 270)
# rot300 = im.rotarImg(img, 300)
# rot330 = im.rotarImg(img, 330)
# rot360 = im.rotarImg(img, 360)

plt.figure(figsize=(18, 8))
plt.subplot(3, 4, 1)
plt.imshow(rot30, cmap='gray')
plt.title("30°")
plt.axis('off')

plt.subplot(3, 4, 2)
plt.imshow(rot60, cmap='gray')
plt.title("60°")
plt.axis('off')

plt.subplot(3, 4, 3)
plt.imshow(rot90, cmap='gray')
plt.title("90°")
plt.axis('off')

plt.subplot(3, 4, 4)
plt.imshow(rot120, cmap='gray')
plt.title("120°")
plt.axis('off')

plt.subplot(3, 4, 5)
plt.imshow(rot150, cmap='gray')
plt.title("150°")
plt.axis('off')

plt.subplot(3, 4, 6)
plt.imshow(rot180, cmap='gray')
plt.title("180°")
plt.axis('off')

# plt.subplot(3, 4, 7)
# plt.imshow(rot210)
# plt.title("210°")
# plt.axis('off')

# plt.subplot(3, 4, 8)
# plt.imshow(rot240)
# plt.title("240°")
# plt.axis('off')

# plt.subplot(3, 4, 9)
# plt.imshow(rot270)
# plt.title("270°")
# plt.axis('off')

# plt.subplot(3, 4, 10)
# plt.imshow(rot300)
# plt.title("300°")
# plt.axis('off')

# plt.subplot(3, 4, 11)
# plt.imshow(rot330)
# plt.title("330°")
# plt.axis('off')

# plt.subplot(3, 4, 12)
# plt.imshow(rot360)
# plt.title("360°")
# plt.axis('off')

plt.show()