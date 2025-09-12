import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def abrir_imagen():
    ruta = filedialog.askopenfilename( #
        title="Seleccione una imagen",
        filetypes=[("Imagenes","*.png;*.jpg;*.jpeg")] #tipos de archivos que se pueden abrir, en este caso imagenes
    )
    if not ruta:
        return

    img = Image.open(ruta) #abrir imagen con PIL
    img_resized = img.resize((400,400)) #redimensionar imagen
    img = ImageTk.PhotoImage(img_resized) #convertir imagen para Tkinter

    lbl.config(image=img) #configurar la etiqueta para que muestre la imagen
    lbl.image = img #guardar referencia de la imagen
    
#Interfaz de una ventana
root = tk.Tk()
root.title("Visualizador de imagenes")
root.geometry("800x600") #tamaño de la ventana
root.resizable(False, False) # Obliga a que no se modifique el tamaño de la ventana

btn = tk.Button(root, text="Abrir imagen", command=abrir_imagen) #(donde va el boton, texto, accion con el click)
btn.place(x = 10, y = 10) #posicion del boton

lbl = tk.Label(root) #etiqueta que se pone en el root
lbl.place(x = 40, y = 40) #posicion de la etiqueta (imagen)
root.mainloop() #mostrar la ventana y que se mantenga abierta