import numpy as np
import matplotlib.pylab as plt
import imgPro as im

img = plt.imread("imagenes/charmander.jpg")

capa = im.layer(img, 0)

plt.imshow(capa)
plt.show()
