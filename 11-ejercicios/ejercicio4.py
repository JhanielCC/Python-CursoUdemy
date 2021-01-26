"""
Tener 4 variables:  lista, string, entero, boolean
y que imprima un mensaje segun el tipo de dato de cada variable
"""
def tipo_trad(tipo):
    resp = " "
    if tipo == list:
        resp = "LISTA"
    elif tipo == int:
        resp = "INT"
    elif tipo == str:
        resp = "STRING"
    elif tipo == bool:
        resp = "BOOLEANO"
    return resp

def tipo_var (variable, tipo):
    ret = " "
    comprobar = isinstance(variable,tipo)
    if comprobar:
        ret = f"La variable Si es del tipo:  {tipo_trad(tipo)}"      #{type(variable)}
    else:
        ret = f"La variable no es del tipo ingresado, es del tipo  {tipo_trad(type(variable))}"
    return ret

lista =['Esta es una lista',44]
cadena = "Esta es una cadena"
num = 12
var_bool = True

print(tipo_var(lista,list))
print(tipo_var(lista,str))
print(tipo_var(cadena,str))
print(tipo_var(num,int))
print(tipo_var(var_bool,bool))