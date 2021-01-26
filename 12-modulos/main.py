"""
MODULOS 
python modules index
https://docs.python.org/3/py-modindex.html

Un modulo son funcionalidades ya hechas para reutilizar.
"""
##########################
"""
#import mimodulo        #Importando todo el contenido de mimodulo

#print(mimodulo.holamundo("Jhaniel"))
#print(mimodulo.calculadora(88,2,True))
#___________________________________________________________
#from mimodulo import holamundo  #Importando solo la funcion holamundo de mimodulo
from mimodulo import *  #De esta forma tambien importamos todo el contenido

print(holamundo("Jhaniel"))
print(calculadora(88,2,True))
"""
###########################
#MODULO FECHAS
import datetime 

print(datetime.date.today()) #Fecha actual

fecha_completa = datetime.datetime.now()
print(fecha_completa)#Fecha completa
print(fecha_completa.year)#Año 
print(fecha_completa.month)#Mes
print(fecha_completa.day)#Día

#Fecha personalizada
fecha_personalizada  = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S") #%d dia %m mes %Y año %H hora %M minutos %S segundos
print("Mi fecha:     "+fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

###########################
#MODULO MATEMATICAS
import math

#Raíz cuadrada de un número
print("Raiz cuadrada de 10: ",math.sqrt(10))
print("Número PI:   ", math.pi)
print("Redodear 6.6587:    ", math.ceil(6.6587))
print("Redodear a la baja 6.6587:    ", math.floor(6.6587))

###########################
#MODULO ALEATORIO
import random

print("Número aleatorio entre 15 y 67:  ",random.randint(15,67))