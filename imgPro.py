import numpy as np

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
    img_copia = np.copy(img)
    return img_copia + brillo

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