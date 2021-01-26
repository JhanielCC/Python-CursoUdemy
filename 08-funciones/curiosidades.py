"""
Es recomendable tener las funciones en la parte superior
"""
def mi_funcion(name):
    #print("Hola que tal")   #Lo mas recomendable es que la funcion no haga el print si no que retorne un dato
    return "Hola que tal " + name

def mi_funcion2(lastname):
    #print("Hola que tal 2")
    return "Hola que tal 2 " + lastname

nombre ="Usuario Nombre"
apellidos = "Apellido Usuario"
print("Hola mundo")
print(f"Bienvenido {nombre} {apellidos}")

print(mi_funcion(nombre))
print(mi_funcion2(apellidos))
#Otra recomendacion es pasar los valores como parametros para las funciones, tratar de evitar usar las variable globales a menos que sea necesario
