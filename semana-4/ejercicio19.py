"""
19-Crea una función llamada es_bisiesto que tome un año como parámetro y
devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
divisible por 400.
"""

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
    
es_bisiesto(1992) # Debería retornar True dado que es bisiesto
es_bisiesto(2100) # Debería retonar False dado que no es un año bisiesto