import os #Directorios
import shutil

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("El directorio/carpeta ya existe")

#Eliminar Carpeta
#os.rmdir("./mi_carpeta")

#Copiar carpeta
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original,ruta_nueva)
"""
#os.rmdir("./mi_carpeta_COPIADA")

print("Contenido de mi_carpeta")

contenido = os.listdir("./mi_carpeta")
#print(contenido)
for fichero in contenido:
    print("Fichero: "+ fichero)