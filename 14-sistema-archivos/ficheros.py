from io import open #crear abrir
import pathlib  #rutas
import shutil   #editar modificar
import os   #eliminar
import os.path #si existe

#Abrir archivo
#archivo = open("fichero_texto.txt","a+")

ruta = str(pathlib.Path().absolute())+"/fichero_texto.txt"
archivo = open(ruta,"a+")

#Escribir en el archivo
archivo.write("******* Soy un texto desde Python *******\n")

#Cerrar archivo
archivo.close()
####################################################################################
#Abrir archivo para lectura
ruta = str(pathlib.Path().absolute())+"/fichero_texto.txt"
archivo_lectura = open(ruta,"r")

#Leer contenido
contenido = archivo_lectura.read()
#print(contenido)
#for elemento in contenido:
#    print(elemento)

#Leer contenido  y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
#print(lista)
for linea in lista:
    lista_frase = linea.split()
    print(lista_frase)
    if not linea.isnumeric():
        print("- "+linea.upper())
        #print("- "+linea.center(10)) Centrar el texto
####################################################################################
#Copiar archivo 
"""
ruta_original = str(pathlib.Path().absolute())+"/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/fichero_copiado.txt"
#ruta_alterna = "../14-sistema-archivos/fichero_copiado.txt"

ruta_alterna = str(pathlib.Path().absolute())+"/../14-sistema-archivos/fichero_copiado.txt"

#shutil.copyfile(ruta_original,ruta_nueva)
#shutil.copyfile(ruta_original,ruta_alterna)
"""
####################################################################################
#Mover
"""
ruta_original = str(pathlib.Path().absolute())+"/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""

####################################################################################
#Eliminar
"""
ruta_nueva = str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""
####################################################################################
#Verificar si existe
#print(os.path.abspath("./")) #Ruta absoluta
ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
ruta_comprobar2 = "./fichero_texto.txt"

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo existe")