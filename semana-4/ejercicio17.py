"""
17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
letras pero en distinto orden), o False en caso contrario.
"""

def es_anagrama(palabra1, palabra2):
    # print(palabra1, palabra2)
    # if palabra1 == palabra2:
    #     return print("Ambas palabras son iguales")
    
    # Convierto a minúsculas ambas palabras
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    print(sorted(palabra1), sorted(palabra2))
    # Sorted ordena las letras de las palabras formando una lista alfabeticamente 
    # por ende deberíamos tener una lista igual en ambas si es que son anagramas
    if sorted(palabra1) == sorted(palabra2): 
        print(f"Las palabras '{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"Las palabras '{palabra1}' y '{palabra2}' no son anagramas.")
    
es_anagrama("amor", "roma") # Debería retornar True porque tienen las mismas letras pero distinto orden

# Recurso sobre sorted():
# https://docs.python.org/es/3/howto/sorting.html