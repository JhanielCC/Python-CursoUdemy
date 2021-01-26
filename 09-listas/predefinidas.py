cantantes = ['2pack','Drake','Bad Bunny','Julio Iglesias']
numeros = [1,2,5,8,3,4]


#Ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos 
cantantes.append("The Pillows")#Agrega el dato al final de la lista
cantantes.insert(1,"David Bisbal")#Indicamos en que indice queremos agregar el elemnto
print(cantantes)

#Eliminar elementos
cantantes.pop(0) #Eliminamos indicando el indice
cantantes.remove("Bad Bunny")    #Eliminamos por el dato del elemento, este tiene que ser escrito como aparece en la lista
print(cantantes)

#Dar vuelta a una lista
numeros.reverse() #El orden va a ser inverso
print(numeros)

#Buscar dentro de una lista
print('The Pillows' in cantantes) #Este nos dara un true o false si encuentra o no el elemento

#Contar elementos
print(len(cantantes))

#Cuantas veces aparece un elemento en la lista
numeros.append(8)
print(numeros.count(8))

#Conseguir indice 
print(cantantes.index("The Pillows"))

#Unir  listas
cantantes.extend(numeros)
print(cantantes)