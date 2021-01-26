nombre ="Jhaniel"

#FUNCIONESS GENERALES
print(nombre) #print()
print(type(nombre)) #type()

#DETECTAR E TIPADO
comprobar = isinstance(nombre,str) #Se le pasa una varibale y se le dice que compruebe si esa variables es lo que tengo en segundo parametro 
if comprobar==True :
    print("Esa variable es un string")
else:
    print("No es un string")

if not isinstance(nombre,float):
    print("La variable no es un numero con decimales")


#LIMPIAR ESPACIOS
frase = "           Esta es una nueva frase pero con muchos espacios.           "
print(frase)
print(frase.strip())

#ELIMINAR VARIABLES
anio = 2021
print(anio) 
del anio
#print(anio)

#COMPROBAR VARIABLE VACIA 
texto = " ff "
if len(texto)<=0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ",len(texto))

#ENCONTRAR CARACTERES 
frase = "La vida es bella"
print(frase.find("vida"))

#REEEMPLAZAR PALABRAS EN UN STRING
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#MAYUSCULAS Y MINISCULAS 
print(nombre)
print(nombre.lower())
print(nombre.upper())

