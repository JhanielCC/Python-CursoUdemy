mi_texto = "'Curso'" # '"Curso"'
mi_texto2 = "de \"Python\" "

union = mi_texto +" "+ mi_texto2
print(union)

union = mi_texto +" \n "+ mi_texto2 #Salto de linea
print(union)

union = mi_texto +" \t "+ mi_texto2 #Tabulación
print(union)

union = mi_texto +" \r "+ mi_texto2 #Borra lo que hay detras de \r
print(union)