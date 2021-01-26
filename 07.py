"""
Ejercicio 1
Mostrar "pais" y "continente" en pantalla y que tipo son
"""
print("############# Ejercicio 1 #############")
pais = "México" #String
continente = "LATAM" #String

print(f"El pais es {pais} y el continente es {continente}")
print(f"El 'pais' es de tipo: {type(pais)} y el 'continente' es de tipo: {type(continente)}")

"""
Ejercicio 2
Mostrar los numeros pares de 1 - 120
"""
print("############# Ejercicio 2 #############")
print("Usando While")
np=1
while np<=120:
    if np%2 == 0:
        print(f"{np} es par")
    np+=1
print("\nUsando For")
np=1
for np in range(1,121):
    if np%2 == 0:
        print(f"{np} es par")
"""
Ejercicio 3
El cuadrado de los primero 60 números naturales
"""
print("############# Ejercicio 3 #############")
print("Usando While")
contador = 0
while contador<=60:
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es: {cuadrado}")
    contador+=1
print("\nUsando For")
contador=0
for contador in range(61):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es: {cuadrado}")


"""
Ejercicio 4
Pedir dos números al usuario y realizar los operaciones basicas
"""
print("############# Ejercicio 4 #############")

n_us1 =120 #int(input("Dame el primer número:   "))
n_us2 =66 #int(input("Dame el segundo número:   "))

print(f"\nLa suma de {n_us1} + {n_us2} es:    {n_us1 + n_us2}")
print(f"La resta de {n_us1} - {n_us2} es:    {n_us1 - n_us2}")
print(f"La multiplicación de {n_us1} * {n_us2} es:    {n_us1 * n_us2}")
print(f"La división de {n_us1} / {n_us2} es:    {n_us1 // n_us2}")
print(f"El resto de {n_us1} % {n_us2} es:    {n_us1 % n_us2}\n")

"""
Ejercicio 5
Mostrar todos los números que hay dentro de dos números que de el usuario
"""
print("############# Ejercicio 5 #############")

n_us1 =12 #int(input("Dame el primer número:   "))
n_us2 =22 #int(input("Dame el segundo número:   "))

print(f"Los números entre {n_us1} y {n_us2} son:")

if n_us1 < n_us2:
    for n in range(n_us1,(n_us2+1)):
        print(f"N: {n}")
else:
    for n in range((n_us2+1),n_us1):
        print(f"N: {n}")

"""
Ejercicio 6
Mostrar las tablas de multiplicar
"""
print("############# Ejercicio 6 #############")

nm=1
while nm <=10:
    print(f"Tabla del {nm}")
    for n in range(1,11):
        print(f"{nm} X {n} = {nm*n}")
    print("\n")
    nm+=1

"""
Ejercicio 7
Todos los numeros impares que hay dentro de dos numeros
"""
print("############# Ejercicio 7 #############")

n_us1 = 12 #int(input("Dame el primer número:   "))
n_us2 = 41 #int(input("Dame el segundo número:   "))

print(f"Los números impares entre {n_us1} y {n_us2} son:")

if n_us1 < n_us2:
    for n in range(n_us1,(n_us2+1)):
        if n%2 != 0:
            print(f"N impar: {n}")
else:
    for n in range((n_us2+1),n_us1):
        if n%2 != 0:
            print(f"N impar: {n}")


"""
Ejercicio 8
Obtener el porcentaje de:
"""
print("############# Ejercicio 8 #############")

n_us1 = 120 #int(input("Dame un número:   "))
n_us2 = 20  #int(input("Qué porcentaje quieres saber?:   "))

print(f"El {n_us2} % de {n_us1} es: {(n_us1*n_us2)//100}")  # n_us1*(n_us2//100)

"""
Ejercicio 9
Pedir números indefinidamente hasta que el usuario introduzca: 111
"""
print("############# Ejercicio 9 #############")

while True:
    numero = 111#int(input("Dame un número: "))
    if numero == 111:
        break
    else:
        print(f"Número introducido: {numero}")
        


"""
Ejercicio 10
Pedir datos de alumnos y decir cuantos han pasado y cuantos no
"""
print("############# Ejercicio 10 #############")

print("Dame 10 usuarios y sus notas")
t_apro=0
t_susp=0

for n in range(1,4):
    alumno = str(input("Dame el nombre del alumno:  "))
    nota = int(input("Dame su calificación: "))
    if nota >=5:
        print(f"El alumno {alumno} Si a pasado la materia con {nota}")
        t_apro+=1
    else:
        print(f"El alumno {alumno} No a pasado la materia")
        t_susp+=1

print(f"Total de aprobados:  {t_apro}, total de suspendidos:  {t_susp}")