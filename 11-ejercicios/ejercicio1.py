"""
Un programa que tenga una lista de 8 numeros enteros.
#Recorrerla y mostrarla
#Ordenarla y mostrarla
#Mostrar la logitud
#Buscar elemento (Que el usuario pida)
"""

numeros = [13,64,52,73,21,7,91,63]

def recorrer (list):
    num = " "
    for list_n in list:
        num = num +" "+ str(list_n)
    return num 

def buscausuario (num):
    if (num in numeros) == True:
        print("Elemento encontrado")
        print(f"Elemento {num} esta en la posición {numeros.index(num)}")
    else:
        print("Elemento No encontrado")

print("\n######### Recorrer la lista #########\n")
print(recorrer(numeros))
print("\n######### Recorrer la lista Ordenada #########\n")
numeros.sort()
print(recorrer(numeros))
print("\n######### Logitud de la lista #########\n")
print(len(numeros))
print("\n######### Buscar elemento en la lista #########\n")
busca = int(input("Dame un elemento a buscar en la lista:   "))
comprobar  = isinstance(busca,int)
while not comprobar or busca <= 0:
    busca = int(input("Dame un elemento a buscar en la lista:   "))
else:
    print(f"Has introducido el {busca}")

buscausuario(busca)