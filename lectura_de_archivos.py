import os
import shutil
import os.path

def lectura_de_archivos (info:[(str,str)])-> str:
    if os.path.exists(info[a])==True:
     for a in info:
        conenido=os.listdir(a)
        cantidad=len(contenido)
     if os.path.exists(info[b])==True:
       #movimiento_de_archivos(a,b)
       print ("sss")
     else:
      nombre_carpeta=info[b]
      os.mkdir(nombre_carpeta)
      #movimiento_de_archivos   
             
    else:
        print ("la carpeta de origen no existe")
    retorno=""    
    return retorno

def movimiento_de_archivos (archivos[(str,int,str)]):
    