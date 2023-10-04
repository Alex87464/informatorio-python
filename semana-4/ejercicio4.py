"""
4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.
Ejemplo:
es_capicua(12321) # Debería devolver True
"""


def es_capicua(numero):
    # Convertimos el número a una cadena de texto
    numero = str(numero)
    # Invertimos la cadena de texto
    numero_invertido = numero[::-1]
    # Comparamos si el número y su inverso son iguales
    if numero == numero_invertido:
        # print(True)
        return print(f"{numero} es capicua")
    else:
        return print(f"{numero} no es capicua")
    
    
es_capicua(12321) # Debería devolver True