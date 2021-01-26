def holamundo(nombre):
    return f"Hola que tal estas {nombre}"

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