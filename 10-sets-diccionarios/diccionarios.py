"""
DICCIONARIOS
Un diccionario es parecido a una lista, almacena un conjunto de valores pero en ligar de tener indices numericos,
tiene indices alfanumericos, se le parece a un array asociativo o objeto json 
"""
persona = {
    "Nombre" : "Usuario",
    "Apellidos" : "US Apellidos",
    "Git": "https://github.com/JhanielCC"
}
"""
print(persona)
print(type(persona))
print(persona["Apellidos"])#Accediendo con el indice
"""

#Lista con diccionarios
contactos = [
    {
    "Nombre" : "Jhaniel",
    "Apellidos" : "C C",
    "Email": "jhaniel@mail.com"
    },
    {
    "Nombre" : "Alejandro",
    "Apellidos" : "S A",
    "Email": "alejandro@mail.com"
    },
    {
    "Nombre" : "Ricardo",
    "Apellidos" : "C A",
    "Email": "chacon@mail.com"
    }
]

print(contactos)
contactos[0]["Nombre"] = "Nombre modificado"
print(contactos[0]) #Accediento al diccionario de la lista con el indice
print(contactos[0]["Nombre"]) #Accediento al elemento 'Nombre' del diccionario de la lista con el indice

#Recorriendo la lista de diccionario con for
for contacto in contactos:
    print(f"Nombre del contacto:    {contacto['Nombre']}")
    print(f"Nombre del contacto:    {contacto['Email']}")
    print("-----------------------------------------------")