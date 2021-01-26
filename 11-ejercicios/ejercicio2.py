"""
Añadir valores a una lista mientras la longitud sea menor a 120
"""

coleccion = [ ]
"""
for contador in range(0,120):
    coleccion.append(f"Elemento:  {contador}")
    print("Mostrando el:  "+coleccion[contador])

print(coleccion)
"""
x = 0
while x < 120:
    coleccion.append(f"Elemento : {x}\n")
    print("Mostrando el:  "+coleccion[x])
    x+=1
print(coleccion)