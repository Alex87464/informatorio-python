# 15-Escribe un programa que pida al usuario una cadena de texto y determine
# cuántas veces aparece cada letra en la cadena.

# Por ejemplo, si el usuario ingresa la cadena "Hola, mundo", el programa
# debería imprimir algo como lo siguiente:
# H: 1
# o: 2
# l: 1
# a: 1
# ,: 1
#  : 1
# m: 1
# u: 1
# n: 1
# d: 1


# Tomamos la cadena de texto ingresada por el usuario
cadena = input("Ingrese una cadena de texto: ")

# Creamos un diccionario vacío
diccionario = {}

# Recorremos la cadena de texto ingresada por el usuario
for letra in cadena:
    # Si la letra ya existe en el diccionario, incrementamos su valor en 1
    if letra in diccionario:
        diccionario[letra] += 1
    # Si la letra no existe en el diccionario, la agregamos con valor 1
    else:
        diccionario[letra] = 1

# Recorremos el diccionario
for letra, cantidad in diccionario.items():
    # Imprimimos la letra y su cantidad
    print(letra + ": " + str(cantidad))
    
# 'letra' es la clave del diccionario y 'cantidad' es el valor de la clave
# Para verlo mas claro descomentá la última línea y te recomiendo probar con la palabra 'hola'
# vas a ver algo como esto en tu consola -> {'h': 1, 'o': 1, 'l': 1, 'a': 1}
# donde lo primero que aparece es la clave y lo segundo el valor o en este caso 
# la cantidad de veces que aparece en el texto ingresado
# print(diccionario) # Descomentá esta línea para ver el diccionario completo
    