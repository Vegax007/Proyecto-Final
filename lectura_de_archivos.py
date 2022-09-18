import os
import shutil
import os.path
#ingresan 
Ubicacion_carpeta_origen="Downloads"
ubicacion_carpeta_destino="Downloads"
carpeta_origen="prueba_origen"
carpeta_destino="prueba_destino"

#definicion rutas
ruta_base=os.getcwd()
ruta_origen=os.path.join(ruta_base,Ubicacion_carpeta_origen,carpeta_origen)

ruta_destino=carpeta_destino
archivos=os.listdir(ruta_origen)
cantidad=len(archivos)

   


#comprobar carpeta y mover
if os.path.exists(carpeta_origen)==True:
  if os.path.exists(carpeta_destino)==True:
   for g in archivos:
    ruta_origen_completa=os.path.join(ruta_origen,archivos[g])
    ruta_destino_completa=os.path.join(ruta_base,ubicacion_carpeta_destino,ruta_destino)
    shutil.move(ruta_origen_completa, ruta_destino_completa)
  else:
   nombre_carpeta=carpeta_destino
   os.mkdir(nombre_carpeta) 
   for g in archivos:
    ruta_origen_completa=os.path.join(ruta_origen,archivos[g])
    ruta_destino_completa=os.path.join(ruta_base,ubicacion_carpeta_destino,ruta_destino)
    shutil.move(ruta_origen_completa, ruta_destino_completa)
else:
 print ("la carpeta de origen no existe")




     
    