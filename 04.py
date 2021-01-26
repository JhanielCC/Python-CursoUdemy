"""
Operadores Aritmeticos 

"""
n1 = 77
n2 = 44

rest = n1 - n2
mult = n1 * n2
div = n1 / n2
resto = n1 % n2
print("-----------------Operadores Aritmeticos -------------------------")
print(f"Suma:  {n1 + n2}")
print(f"Resta:  {rest}")
print(f"Multiplicación:  {mult}")
print(f"División:  {div}")
print(f"El Resto de la división es:  {resto}")


"""
Operadores de Asignación

"""
edad = 55 # = Es un operador de asignación
print("-----------------Operadores de Asignación -------------------------")
print(edad)
# += Operador de asignación sumar 5 al valor que ya tiene este 
edad += 5 # edad = edad + 5
print(edad)
# -= Operador de asignación restar 5 al valor que ya tiene este 
edad -= 5 # edad = edad - 5
print(edad)


"""
Operadores de Incremento y Decremento

"""
print("-----------------Operadores de Incremento y Decremento -------------------------")

year = 2020

year = year + 1 # +=1 Incremento
year = year - 1 # -=1 Decremento

year = 1 + year # +=1 PreIncremento
year = 1 - year # -=1 PreDecremento



"""
Entrada y Salida de datos
"""
print("-----------------Entrada y Salida de datos-------------------------")
#Entrada
nombre = input("¿Cual es tu nombre?:    ")
edad = input("¿Cual es tu edad?:    ")

#Salida
print(f"El usuario es:   {nombre}, tiene {edad} años")

print(f"El usuario es:   {nombre}, tiene {int(edad)+2} años chinos")
