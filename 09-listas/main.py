"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podermos usar un indice numerico.
"""
#pelicula = "Batman"
#Definir lista
peliculas = ["Batman","Superman","Linterna Verde","Robin"]
cantantes = list(('2pac','Drake','Jennifer Lopez')) #Creando lista con la funcion list, a la cual le pasamos una tupla y esta la convierte en una lista con los valores que le ingresamos
"""
years = list(range(2000,2021))
variada = ["Usuario",88,4.4,True,'Texto']

print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

#Indices de las listas
print(peliculas) #Todos los elementos
print(peliculas[0]) #Indicando el indice del dato
print(peliculas[-2])    #Indice de forma de retroceso
print(cantantes[0:2])   #Indice de inicio y final
print(peliculas[1:]) #Todos los elementos desde el indice indicado

#Añadir elementos a una lista
print("\n#######################  Añadir a lista  #######################\n")
peliculas[2] = "Wonder Woman" #Modificando elemento dentro de la lista mediante el indice
print(peliculas)
cantantes.append("Jose Jose")
cantantes.append("The Pillows")
print(cantantes)

#Recorrer lista
print("\n#######################  Recorrer lista  #######################\n")
for peli in peliculas:
    print(f"{peli} esta en la posición {peliculas.index(peli)}")

"""
nueva_peli = " "
print("Ingresa 'parar' para terminar de ingresar")
while nueva_peli != "parar":
    nueva_peli = input("Introduce una pelicula: ")
    if peli != "parar":
        peliculas.append(nueva_peli) 
print(peliculas)

"""

#Listas Multidimensionales
print("\n#######################  Listas Multidimensionales  #######################\n")
"""
Una lista multidimensional es una lista que contiene otras listas
"""
print("\n***** LISTADO DE CONTACTOS *****\n")

contactos = [
        [
            'Antonio',
            'antonio@mail.com'
        ],
        [
            'Luis',
            'luis@mail.com'
        ],
        [
            'Jose',
            'jose@mail.com'
        ],
        [
            'Salvador',
            'salvador@mail.com'
        ]
]
#print(contactos)
#print(contactos[1]) # Accediento a la sub lista en el indice 1
#print(contactos[1][1]) # Accediento al elemento 1 de la sub lista en el indice 1 

for contacto in contactos:
    #print(contacto[0])
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre:  "+elemento)
        else:
            print("Email:  "+elemento)
    print("\n")