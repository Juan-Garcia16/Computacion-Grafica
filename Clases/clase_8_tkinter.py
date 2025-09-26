import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import imgPro as ip

imagen_original = None  

# def brillo(img, valor):
#     img_cop = np.copy(img)
#     img_cop = img_cop + valor * 255
#     img_cop = np.clip(img_cop, 0, 255)
#     return img_cop

def aplicar_brillo(valor):
    if imagen_original is None:
        return
    try:
        val = float(valor)
    except ValueError:
        val = 0.0
    img_np = np.array(imagen_original, dtype=np.float32)
    img_np = ip.bright(img_np, val)
    img_pil = Image.fromarray(img_np.astype(np.uint8))
    mostrar_imagen(img_pil)
    
def aplicar_contraste(valor):
    if imagen_original is None:
        return
    try:
        val = float(valor)
    except ValueError:
        val = 0.0
    img_np = np.array(imagen_original, dtype=np.float32)
    print(img_np)
    img_np = ip.contraste_dark(img_np, val)
    img_pil = Image.fromarray(img_np.astype(np.uint8))
    mostrar_imagen(img_pil)
    
def aplicar_canales():
    if imagen_original is None:
        return
    img_np = np.array(imagen_original, dtype=np.float32)
    
    if img_np.ndim == 3 and img_np.shape[2] >= 3:
        if not r_var.get():
            img_np[:,:,0] = 0
        if not g_var.get():
            img_np[:,:,1] = 0
        if not b_var.get():
            img_np[:,:,2] = 0

    img_pil = Image.fromarray(img_np.astype(np.uint8))
    mostrar_imagen(img_pil)


def abrir_imagen():
    global imagen_original
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"), ("Todos", "*.*")]
    )
    if not ruta:
        return
    imagen_original = Image.open(ruta).resize((400, 300))
    mostrar_imagen(imagen_original)


def mostrar_imagen(img):
    foto = ImageTk.PhotoImage(img)
    lbl.config(image=foto)
    lbl.image = foto  

# def aplicar_brillo_btn():
#     global imagen_original
#     if imagen_original is None:
#         return
#     try:
#         val = float(entry.get())
#     except ValueError:
#         val = 0.0
#     img_np = np.array(imagen_original, dtype=np.float32)
#     img_np = brillo(img_np, val)
#     img_pil = Image.fromarray(img_np.astype(np.uint8))
#     mostrar_imagen(img_pil)

root = tk.Tk()
root.title("Visor de imágenes")
root.geometry("650x1080")

btn = tk.Button(root, text="Abrir imagen...", command=abrir_imagen)
btn.place(x=10, y=10)

# tk.Label(root, text="Brillo:").place(x=150, y=15)

# entry = tk.Entry(root)
# entry.place(x=200, y=15, width=60)
# entry.insert(0, "0.5")  

# btn_brillo = tk.Button(root, text="Aplicar brillo", command=aplicar_brillo_btn)
# btn_brillo.place(x=270, y=10)

lbl = tk.Label(root)
lbl.place(x=100, y=60)

tk.Label(root, text="Brillo:").place(x=140, y=415)
slider_brillo = tk.Scale(root, from_=-1, to=1, resolution=0.01, orient=tk.HORIZONTAL, length=220, command=aplicar_brillo)
slider_brillo.set(0.0)  # Valor inicial
slider_brillo.place(x=215,y=400)

tk.Label(root, text="Contraste:").place(x=140, y=465)
slider_contraste = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, length=220, command=aplicar_contraste)
slider_contraste.set(0.0)  # Valor inicial
slider_contraste.place(x=215,y=450)


'''checkbox'''
r_var = tk.BooleanVar(value=True)
g_var = tk.BooleanVar(value=True)
b_var = tk.BooleanVar(value=True)

chk_r = tk.Checkbutton(root, text="Rojo", variable=r_var, command=aplicar_canales)
chk_g = tk.Checkbutton(root, text="Verde", variable=g_var, command=aplicar_canales)
chk_b = tk.Checkbutton(root, text="Azul", variable=b_var, command=aplicar_canales)

chk_r.place(x=200, y=520)
chk_g.place(x=260, y=520)
chk_b.place(x=320, y=520)




root.mainloop()