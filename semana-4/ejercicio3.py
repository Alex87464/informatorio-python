"""
3-Crea una función llamada invertir_cadena que tome una cadena de texto como
parámetro y devuelva la cadena invertida. 
"""

def invertir_cadena(cadena):

    # Variable donde se va a almacenar la cadena invertida
    cadena_invertida = ""
    
    # Recorremos la cadena de texto de derecha a izquierda
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i] # Concatenamos cada caracter a la cadena_invertida
    
    # Retornamos la cadena invertida
    print(cadena_invertida)
    return cadena_invertida

invertir_cadena("Hola mundo")