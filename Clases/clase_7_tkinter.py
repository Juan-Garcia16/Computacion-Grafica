import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import imgPro as ip

# Variable global
imagen_actual = None

def abrir_imagen():
    global imagen_actual
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imágenes","*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"), ("Todos","*.*")]
    )
    if not ruta:
        return
    imagen_actual = Image.open(ruta).resize((400,300))
    mostrar_imagen(imagen_actual)

def mostrar_imagen(img):
    foto = ImageTk.PhotoImage(img)
    lbl.config(image=foto)
    lbl.image = foto

def aplicar_brillo_btn():
    global imagen_actual
    if imagen_actual is None:
        return
    try:
        valor = float(entry.get())  # lee el valor del Entry
    except ValueError:
        print("Ingresa un número válido")
        return

    # Convertir PIL a numpy
    img_np = np.array(imagen_actual, dtype=np.float32)
    # Usar directamente la función de brillo
    img_np = ip.bright(img_np, valor)
    # Convertir numpy a PIL
    imagen_actual = Image.fromarray(img_np.astype(np.uint8))

    mostrar_imagen(imagen_actual)

# -------- Interfaz --------
root = tk.Tk()
root.title("Visor de imágenes con brillo")
root.geometry("600x450")

btn = tk.Button(root, text="Abrir imagen...", command=abrir_imagen)
btn.place(x=10,y=10)

separate_text = tk.Label(root, text="-------------------")
separate_text.place(x=10,y=30, width=10)

lbl_texto = tk.Label(root, text="Brillo:")
lbl_texto.place(x=10,y=40)

entry = tk.Entry(root)          #Caja para ingresar el texto
entry.place(x=50,y=40, width=60)
entry.insert(0,"0.1") #valor por defecto

btn_brillo = tk.Button(root, text="Aplicar brillo", command=aplicar_brillo_btn)
btn_brillo.place(x=10,y=70)

# lbl_contraste = tk.Label(root, text="(contraste")
# lbl_contraste.place(x=150,y=60)

lbl = tk.Label(root)
lbl.place(x=150,y=60)

root.mainloop()