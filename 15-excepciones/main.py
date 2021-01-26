"""
Capturar Excepciones y manejar errores en código 
susceptible a fallos/errores
"""
#Excepciones
"""
try:
    nombre ="Janiel"# input("Cual es tu nombre?")
    if len(nombre)>1:
        nombre_usuario = "El nombre es: " + nombre
    print(nombre_usuario)
except:
    print("Ha ocurrrido un error con el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("fin de la iteración !!!")

try:
    numeros = [13,64,52,73,21,7,91,63]
    busqueda = int(input("Dame un numero:   "))
    search  = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el indice: {search}")
except:
    print("El número no esta en la lista")
"""
#Multiples excepciones
"""
try:
    numero = int(input("Dame un numero para elevarlo al cuadro: "))
    print("El cuadrado es:  "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo") 
except ValueError:
    print("Introduce un número correcto")
except Exception as e:
    print("Ha ocurrido un error:    ", type(e).__name__) 
"""

#Excepciones Personalizadas o Lanzar excepcion
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Dame la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError ("La edad introducida no es real") #raise generar una excepcion 
    elif len(nombre) <= 1:
        raise ValueError ("El nombre no esta completo") 
    else:
        print(f"Bienvenido {nombre}")
except ValueError:
    print("Introduce los datos correctamente !!!")
except Exception as e:
    print("Existe un error: ", e)

