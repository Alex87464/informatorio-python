"""
15-Crea una función llamada contar_palabras que tome una cadena de texto
como parámetro y devuelva el número de palabras que contiene. Se considera
que las palabras están separadas por espacios.
"""

def contar_palabras(texto):
    print (f"El texto ingresado tiene {len( texto.split(' ') )} palabras")
    # Con split(' ') creo una lista con las palabras ingresadas
    # y con len() tomo el total de elementos que contiene la lista (en este caso palabras)
    
    
contar_palabras("Este es un texto de prueba") # Debería retornar 6