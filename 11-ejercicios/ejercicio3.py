"""
Comprobar si una variable esta vacia y si esta vacia que sea llenada con un texto en minuscula y al mostrarlo que sea en mayuscula
"""
texto = " "
texto2 = "Este texto tiene contenido"

def check_variable(varia):
    if len(varia.strip())<=0:
        varia = "texto agregado"
        print(varia.upper())
    else:
        print(f"La variable tiene texto:    {varia}")

check_variable(texto)
check_variable(texto2)