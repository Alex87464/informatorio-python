"""
8-Crea una función llamada es_palindromo que tome una cadena de texto como
parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
contrario.
"""


def es_palindromo(texto):
    if(texto == texto[::-1]): # Comparo el texto ingresado con el mismo texto pero invertido
        return print(f"{texto} es un palíndromo") # Si se cumple la condición de igualdad es palíndromo
    else:
        return print(f"{texto} no es un palíndromo") # Si no se cumple, no es un palíndromo

es_palindromo("neuquen") # Debería retornar True / es un palíndromo