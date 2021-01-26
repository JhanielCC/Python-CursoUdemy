"""
FUNCION
Es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarce  invocando a
la funcion  tantas veces como sea necesario

def nombre_funcion(parametros):
    # Bloque / conjunto_de_instrucciones

nombre_funcion(parametro)
"""
########## Ejemplo 1 ######### Invocar una función
def muestra_nombre():
    print("Usuario 1")
    print("Usuario 2")
    print("Usuario 3")

#muestra_nombre()

########## Ejemplo 2 ######### Paso de parametros
def mostrartunombre(name,age):
    print(f"Tu nombre es:   {name}")
    if age >=18:
        print("Eres mayor de edad")
    else:
        print("Aun no eres mayor de edad")

nm = "Juan" #str(input("Como te llamas?:    "))
edad= 18 #int(input("Dame tu edad:  "))
#mostrartunombre(nm,edad)

########## Ejemplo 3 #########

def tabla(numero):
    print(f"Tabal del {numero}")
    for c in range(1,11):
        print(f"{numero} X {c} = {numero*c}")
    print("\n")
tbnum = 5# int(input("Dame un numero:  "))
#tabla(tbnum)

########## Ejemplo 3 ######### Tablas de multiplicar
"""
for c in range(1,11):
    tabla(c)
"""

########## Ejemplo 4 ######### Parametros opcionales

def getEmpleado(nombre,dni = None):
    print("EMPLEAADO")
    print(f"Nombre:  {nombre}")
    if dni != None:
        print(f"DNI:    {dni}")

#getEmpleado("Jhaniel","77788999")
#getEmpleado("User")

########## Ejemplo 5 ######### Parametros opcionales return 
"""
def saludame(nombre):
    saludo = f"Hola nuevo usuario {nombre}"
    return saludo
print(saludame("Jhaniel"))
"""
########## Ejemplo 6 ######### Parametros opcionales return 
def calculadora(num1,num2,basicas=False):
    
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 // num2
    
    cadena = " "
    #cadena +="Suma: " + str(suma) +"\nResta:  "+str(resta)+"\nMultiplicación:   "+str(multi)+"\nDivisión:   "+str(divi)
    if basicas != False:
        cadena +="Suma: " + str(suma) +"\nResta:  "+str(resta)
    else:
        cadena +="\nMultiplicación:   "+str(multi)+"\nDivisión:   "+str(divi)
    return cadena

#print(calculadora(98,12,True))

########## Ejemplo 7 ######### Funcion que llama funcion

def getNombre(nombre):
    texto=f"El nombre del usuario es {nombre}"
    return texto

def getApellidos(apellidos):
    texto=f"Los apellidos del usuario son {apellidos}"
    return texto

def regresaTodo(nombre,apellidos):
    texto = getNombre(nombre) + "\n"+ getApellidos(apellidos)
    return texto
#print(getNombre("Usuario"))
#print(getApellidos("Apellidos Usuario"))
#print(regresaTodo("Jhaniel","Coronel C"))


########## Ejemplo 8 ######### Funciones anonimas lambda
"""
Una función lambda es una función anonima, una funcion que no tiene nombre
Funciones que sirven para tareas simples y pequeñas pero que pueden llegar a ser
repetitivas y que todo su contenido se traduce en una linea de codigo
"""
dime_el_year = lambda year:f"El año es {year}"

#print(dime_el_year(2021))