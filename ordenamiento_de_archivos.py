# Importar modulo os, shutil y el archivo lectura de archivos, de la rama
import os
import shutil
from lectura_de_archivos import ruta_destino_completa

# listar todos los archivos presentes


def seleccionar_archivos(nombre_carpeta):
    lista_archivos = os.listdir(nombre_carpeta)
    return lista_archivos


# Guardarlos en una variable
archivos = seleccionar_archivos(ruta_destino_completa)

# variable que contendra un boolean, que significa si esa carpeta existe o no
documentos = os.path.exists("documentos")
fotos = os.path.exists("fotos")
videos = os.path.exists("videos")
musica = os.path.exists("musica")
otros = os.path.exists("otros")

# bucle para crear las carpetas
while True:
    if documentos == False:
        os.mkdir("documentos")
        continue
    if fotos == False:
        os.mkdir("fotos")
        continue
    if videos == False:
        os.mkdir("videos")
        continue
    if musica == False:
        os.mkdir("musica")
        continue
    if otros == False:
        os.mkdir("otros")
        break
