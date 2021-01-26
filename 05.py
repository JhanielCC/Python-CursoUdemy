"""
Condicionales
"""

print("-------------Ejemplo1-------------")

#Ejemplo1
#color = input("Adivina mi color favorito:   ")
color = "Rojo"
if color == "Rojo":
    print("SI !!!, El color es Rojo")
else:
    print("No es ese color!!!")

"""
Operadores de Comparación

==  igual a
!=  diferente a
<   menor que
>   mayor que
<=  menor igual a
>=  mayor igual a
"""
print("\n-------------Ejemplo2-------------")
#Ejemplo2
#year = int(input("En que año estamos?:  "))
year=2020
if year >= 2021:
    print("Estamos en 2021 en adelante.")
else:
    print("Estamos en un año anterior a 2021.")

"""
If anidados
"""
print("\n-------------Ejemplo3-------------")
#Ejemplo3
nombre = "Jhaniel" #input("Cual es tu nombre?:    ")
ciudad = "Mexico"   #input("Cual es tu ciudad?:    ")
continente = "LATAM"    #input("Cual es tu continente?:    ")
edad = 26   # int(input("Cual es tu edad?:    "))
m_edad = 18 # int(input("Cual es la mayoria de edad en ti pais?:    "))

if edad >= m_edad:
    print(f"{nombre} Es mayor de edad")
    if continente != "LATAM":
        print(f"{nombre} No es latinoamericano")
    else:
        print(f"{nombre} Es Latino y de {ciudad}") 
else:
    print(f"{nombre} No es mayor de edad")


"""
Elif
"""
print("\n-------------Ejemplo4-------------")
#Ejemplo4
dia = 1
#dia = int(input("Introduce el número del día de la semana:  "))

"""
if dia == 1:
    print("Es Lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miercoles") 
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    if dia == 6:
                        print("Es Sabado")
                    else:
                        if dia == 7:
                            print("Es Domingo")   
"""

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles") 
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado")
elif dia == 7:
    print("Es Domingo")   

"""
Operadores Lógicos y múltiples condiciones

and     Y 
or      O
!       Negación
not     No
"""
print("\n-------------Ejemplo5-------------")
#Ejemplo5

ed_min = 18
ed_max = 65
edad_uss = 26 #int(input("Cual es tu edad?:   "))

if edad_uss >= ed_min and edad_uss <= ed_max:
    print("Estas en edad de trabajar")
else:
    print("No tienes edad para trabajar")


"""

"""
print("\n-------------Ejemplo6-------------")
#Ejemplo6

pais = "Mexico" #input("Introduce un pais:   ")

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} SI es un pais de habla hispana !!!")
else:
    print(f"{pais} No es un pais de habla hispana :(")

print("\n-------------Ejemplo7-------------")
#Ejemplo7

pais = "España" #input("Introduce un pais:   ")

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana  :(")
else:
    print(f"{pais} SI es un pais de habla hispana !!!")


print("\n-------------Ejemplo8-------------")
#Ejemplo8

pais = "USA" #input("Introduce un pais:   ")

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana  :(")
else:
    print(f"{pais} SI es un pais de habla hispana !!!")
