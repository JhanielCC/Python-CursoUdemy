"""
Bucle For
for variable in elemento_iterable (Lista,Rango, etc)
    Bloque de instrucciones
"""
print("_________BUCLE FOR_________")
contador = 0
r = 0

for contador in range(0,5):
    print(f"Voy por el: {str(contador)}")
    r += contador
print(f"El resultado es:    {r}")

#Ejemplo tablas de multiplicar
print("\n##### EJEMPLO FOR #####")
n_user = 5 #int(input("De que número quieres la tabla?:    "))
if n_user < 1:
    n_user = 1
print(f"Tabla del {n_user}")
for n_tabla in range(1,11):
    if n_user == 30:
        print(f"No se puede utilizar {n_user}.")
        break
    print(f"{n_user} X {n_tabla} = {n_user*n_tabla}")
else: #Este else se ejecuta al finalizar el for
    print("Tabla finalizada")


"""
Bucle While
Estructura de control que itera o repite la ejecución  de una serie de instrucciones 
tantas veces como sea necesario hasta que deje de cumplirse la condición.

WHILE condicion:
    Bloque de instrucciones
    actualización de contador
"""
print("_________BUCLE WHILE_________")
contador = 1
while contador<=5:
    print(f"Estoy en el número:{contador}")
    contador+=1

print("\n##### EJEMPLO WHILE 1 #####")
contador = 1
muestrame =str(0)

while contador<=100:
    muestrame = muestrame +", "+ str(contador)
    contador+=1
print(muestrame)

print("\n##### EJEMPLO WHILE 2 #####")

n_ss = int(input("Des que número quieres la tabla?: "))

if n_ss == 1:
    n_ss = 1
print(f"Tabal del {n_ss}")
cc=1
while cc<=10:
    print(f"{n_ss} X {cc} = {n_ss*cc}") 
    cc+=1
else:
    print("Tabla terminada.")

