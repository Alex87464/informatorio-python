"""
11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.
"""

def contar_vocales(texto):
    # Creamos una variable para guardar la palabra resultante
    resultado = 0

    # Recorremos cada letra del texto
    for caracter in texto:
        # Si el caracter/letra es una vocal
        if caracter in "aeiouAEIOU":
            resultado = resultado+1 # Aumentamos el valor de las vocales encontradas 
            
    # Por último imprimimos el resultado
    print(resultado)
    
    
contar_vocales( input("Ingrese una cadena de texto: ") )
# contar_vocales("hola como estas") # Deberia retornar 6 