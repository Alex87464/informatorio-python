# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima 
# la misma cadena pero con todas las vocales en mayúscula.

cadena = input("Escribe una cadena de texto: ")

# Creamos una variable para guardar la palabra resultante
resultado = ""

# Recorremos cada letra de la cadena de texto
for caracter in cadena:
    # Si el caracter/letra es una vocal en minúscula
    if caracter in "aeiou":
        resultado += caracter.upper() # Agregamos la vocal pero ahora en mayúscula a la lista resultado
    else: # En caso de no ser una vocal lo agregamos sin modificar al resultado
        resultado += caracter
        
# Por último imprimimos el resultado
print(resultado)

# Recurso sobre el método upper():
# https://programacionfacil.org/cursos/python_basico/capitulo_5_strings_python_3.html