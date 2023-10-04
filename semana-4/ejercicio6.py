"""
6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par.
"""

def es_par(numero):
    if(numero % 2 == 0):
        return print("El número es par")
    else:
        return print("El número es impar")
    
es_par(10) # Debería devolver True dado que 10 % 2 = 0