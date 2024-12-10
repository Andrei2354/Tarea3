import os
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Juego de Traducción - Hiragana")
root.geometry("400x500")
root.resizable(False, False)

directorioImagenes = os.listdir('hiragana')
imagenesSeleccionadas = random.sample(directorioImagenes, 10)
puntos = 0
indiceActual = 0

frameJuego = ttk.Frame(root)
frameJuego.pack(pady=10, padx=10, fill="both", expand=True)

labelTitulo = ttk.Label(frameJuego, text="Traduce el Hiragana", font=("Arial", 18, "bold"))
labelTitulo.pack(pady=10)

labelImagen = ttk.Label(frameJuego)
labelImagen.pack(pady=10)

respuesta = ttk.Entry(frameJuego, font=("Arial", 14), justify="center")
respuesta.pack(pady=10)

labelPuntos = ttk.Label(frameJuego, text=f"Puntos: {puntos}", font=("Arial", 14))
labelPuntos.pack(pady=10)

botonComprobar = ttk.Button(frameJuego, text="Comprobar", command=lambda: comprobarTraduccion())
botonComprobar.pack(pady=10)

labelMensaje = ttk.Label(frameJuego, text="", font=("Arial", 12), foreground="blue")
labelMensaje.pack(pady=10)

# Funciones
def mostrarImagen():
    global indiceActual
    imagenActual = imagenesSeleccionadas[indiceActual]
    imagenPath = os.path.join('hiragana', imagenActual)
    img = Image.open(imagenPath)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    labelImagen.config(image=img_tk)
    labelImagen.image = img_tk

def comprobarTraduccion():
    global indiceActual, puntos

    imagenActual = imagenesSeleccionadas[indiceActual]
    respuestaCorrecta = os.path.splitext(imagenActual)[0]
    traduccionUsuario = respuesta.get().strip()

    if traduccionUsuario.lower() == respuestaCorrecta.lower():
        puntos += 1
        labelMensaje.config(text="¡Correcto!")
    else:
        labelMensaje.config(text=f"Incorrecto. Era: {respuestaCorrecta}")

    labelPuntos.config(text=f"Puntos: {puntos}")
    respuesta.delete(0, tk.END)

    indiceActual += 1
    if indiceActual < len(imagenesSeleccionadas):
        mostrarImagen()
    else:
        finalizarJuego()

def finalizarJuego():
    root.destroy()

    resultados = tk.Tk()
    resultados.title("Resultados Finales")
    resultados.geometry("300x200")
    resultados.resizable(False, False)

    if puntos < 5:
        mensaje = f"Suspenso: {puntos}/10"
        color = "red"
    elif puntos == 5:
        mensaje = f"Suficiente: {puntos}/10"
        color = "orange"
    elif puntos == 6:
        mensaje = f"Bien: {puntos}/10"
        color = "blue"
    elif puntos in [7, 8]:
        mensaje = f"Notable: {puntos}/10"
        color = "purple"
    else:
        mensaje = f"Sobresaliente: {puntos}/10"
        color = "green"

    labelResultado = ttk.Label(resultados, text=mensaje, font=("Arial", 18, "bold"), foreground=color)
    labelResultado.pack(pady=20)

    botonCerrar = ttk.Button(resultados, text="Cerrar", command=resultados.destroy)
    botonCerrar.pack(pady=10)

    resultados.mainloop()

mostrarImagen()
root.mainloop()