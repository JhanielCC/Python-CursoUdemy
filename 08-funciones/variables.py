"""
Variable local:
Es aquella que se define dentro de una función y no puede ser usada fuera de ella
Variable global:
Son declaradas fuera de la función y estan disponibles dentro y fuera de las funciones 
"""
#Variable global 
frase="Hola esta es una frase en una variable global"

print(frase)

def holamundo():
    frase = "Esta es una frase en una variable local dentro de una función"
    print(frase)
    year = 2021
    print(year)
    global git #Me permite hacer una variable global dentro de una funcion
    git = "https://github.com/JhanielCC"
    return "Dato devuelto" + str(year)

#print(year) No se podra ya que la variable year pertenece solo en la funcion holamundo, tendria que retornar la variable para poder acceder a ella
print(holamundo())
print(git) #Variable global dentro de una funcion 