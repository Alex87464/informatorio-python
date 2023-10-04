"""
5-Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario.
"""

def es_divisible(numero1, numero2):
    if(numero1 / numero2 == 0):
        return print(f"{numero1} es divisible por {numero2}")
    else:
        return print(f"{numero1} no es divisible por {numero2}")
    
es_divisible(10, 2) # Debería devolver True