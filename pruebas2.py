import matplotlib.pyplot as plt
import numpy as np
import Clases.imgPro as proImg

# img1 = plt.imread('images_taller/github.webp') / 255
# img2 = plt.imread('images_taller/fondo.jpg') / 255
# img3 = plt.imread('images_taller/silksong.jpeg') / 255

# print(img1.shape)
# print(img2.shape)

# img_a = img3
# img_b = proImg.zoom(img3, 5)


# print()
# print(img_a.shape)
# print(img_b.shape)


# plt.figure(figsize=(12, 6))  # 12 pulgadas de ancho, 6 de alto
# plt.subplot(1,2,1)
# plt.imshow(img_a)
# plt.axis('off')

# plt.subplot(1,2,2)
# plt.imshow(img_b)
# plt.axis('off')

# plt.show()


#===============================================

    # # Leer y normalizar la imagen
    # img1 = plt.imread('images_taller/silksong.jpeg') / 255
    # # Coordenadas para recortar el centro (por ejemplo, un recorte de 100x100)
    # h, w = img1.shape[:2]
    # zoom_area = 100
    # start_row = h // 2 - zoom_area // 2
    # end_row = h // 2 + zoom_area // 2
    # start_col = w // 2 - zoom_area // 2 
    # end_col = w // 2 + zoom_area // 2
    # # Recortar región central
    # recorte = img1[start_row: end_row, start_col:end_col]
    # # Aumentar tamaño del recorte (ampliación)
    # zoom_factor = 5
    # zoomed = np.kron(recorte, np.ones((zoom_factor, zoom_factor, 1)))
    # # Mostrar resultados
    # plt.figure("Zoom hacia adentro")
    # plt.subplot(1, 2, 1)
    # plt.title("Imagen Original")
    # plt.imshow(img1)
    # plt.axis('off')
    # plt.subplot(1, 2, 2)
    # plt.title("Zoom sobre región central")
    # plt.imshow(zoomed)
    # plt.axis('off')
    # plt.show()

#===============================================

# img = plt.imread('images_taller/silksong.jpeg') / 255
# # img = plt.imread('images_taller/github.webp') / 255

# if img.max() <= 1.0:
#     img = (img * 255).astype(np.uint8)
    
# if img.ndim == 3:
#     gray = np.dot(img[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
# else:
#     gray = img
    
# proImg.mhist(gray, tipo='n', color='red')

#===============================================
