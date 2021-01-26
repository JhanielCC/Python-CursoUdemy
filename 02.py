"""
Variables y tipos
Una variables es un contenedor de información 
que dentro guardará, un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto.
"""
#Python es debilmente tipado, no hay que indicar el tipo de dato que va a ser solo interpreta el tipo de dato con el contido de este
texto = "Curso de Python"
#texto = 1
texto2 = 'en Udemy'
numero = 2
decimal = 6.7
#print(texto)

"""
Concatenar
Mostrar varias variables juntas
"""
nombre = 'Nombre Usuario'
apellidos = 'C C'
git = 'https://github.com/JhanielCC'
print("Hola yo soy"+nombre+" "+apellidos)
print(f"Hola soy {nombre} {apellidos}")
print("Hola soy {} {} y mi GH es: {}".format(nombre,apellidos,git))

print("-----------------------TIPOS DE DATOS-----------------------------------")
"""
Tipos de datos

"""
nada = None
cadena = "Soy una cadena"
entero = 99
flotante = 4.2
boleano = True #True/False
lista = [00,10,20,30,40,50,60,70,80,90]
listaStr = [12,"Uno",44,"Cien"]
tupla = ("Curso", "en", "Python")#Es una lista de datos que no pueden cambiar
diccionario = {
    "nombre":"Jhaniel",
    "apellido": "CC",
    "edad":26
}#Es un tipo de Array asociativo / Documento json. Colección de datos Clave y Valor 
rango = range(9)
dato_byte = b"Test" 

print(dato_byte)
#Mostrar tipo de dato
print(type(dato_byte))


print("--------------------------CONVERTIR TIPO DE DATO--------------------------------")
"""
Convertir tipo de datos a otro

"""
txt = "Soy un texto"
num = str(5) #Convertir a str
print(type(num))
print(txt+" "+num)

num = int(5) #Convertir a int
print(type(num))
num = float(5) #Convertir afloat
print(type(num))
