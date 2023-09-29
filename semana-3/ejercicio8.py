# 8-Escribe un programa que pida al usuario una cadena de texto  y luego imprima el número de palabras que contiene.
# Ejemplos: 'Hola como estas' -> 3 palabras | 'Hola' -> 1 palabra | '' -> 0 palabras


# Tomamos la cadena de texto
cadena = input("Escribe una cadena de texto: ")

# Usamos el método split() para separar la cadena de texto en palabras
palabras = cadena.split()
# palabras guardaría ahora una lista de palabras ingresadas por el usuario
# por ejemplo: ['Hola', 'como', 'estas']

# Por ultimo, imprimimos la longitud de la lista de palabras
print("La cantidad de palabras ingresadas es:", len(palabras))

# Recurso sobre la función split():
# https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/

# Recurso sobre la función len():
# https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/python-len/