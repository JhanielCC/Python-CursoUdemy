"""
SETS
Es una colección de datos que no tienen indice ni orden 
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}
personas.add("Paco") #Agregar elementos a un set
personas.remove("Francisco") #Eliminar elementos de un set
print(personas)
print(type(personas))