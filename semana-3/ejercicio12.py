# 12-Escribe un programa que pida al usuario una lista de números separados por comas y calcule su promedio.
"""
NOTA: Para calcular el promedio sumamos todos los números y luego los dividimos por la cantidad de números que hay.
Ejemplos:
Si tenemos los números: 1, 2, 3, 4, 5
Sumamos todos los números: 1 + 2 + 3 + 4 + 5 = 15
Dividimos la suma por la cantidad de números que hay: 15 / 5 = 3 <- Este es el promedio

Otro ejemplo con los números: 2, 4, 6, 8 
2 + 4 + 6 + 8 = 20
20 / 4 = 5 <- Este es el promedio
"""

# Tomamos los números ingresados por el usuario
numeros = input("Ingrese una lista de números separados por comas: ")

# Creamos la lista con los números ingresados por el usuario
lista_numeros = numeros.split(",") # IMPORTANTE: En este punto tenemos la lista de números como cadenas de texto
# y no cómo números. Si ingresamos 1,2,3,4,5 la lista queda así: ['1', '2', '3', '4', '5']

# Creamos la variable donde guardamos la suma total de los números
suma = 0

# Creamos la variable donde guardamos la cantidad de números ingresados para luego calcular el promedio
total_numeros_ingresados = len(lista_numeros)

if "," in numeros:
    
    # Acá hacemos una `compresión de listas`(info al final del archivo) para convertir los números de la lista a enteros
    suma = sum([int(i) for i in lista_numeros])
    
    # En este punto tenemos la suma de todos los números solo queda dividirlos 
    # por la cantidad de números en la lista

    print("El promedio es: ", suma / total_numeros_ingresados)
    
else: # En caso de no ingresar numeros separados por comas imprimimos un mensaje y salimos del programa
    print('Error no se ingresaron números separados por `,`')
    exit()


# Comprención de listas
# Una comprensión de lista es una forma concisa de crear una lista.
# Ejemplo:
# lista = [i for i in range(1, 11)] # Creamos una lista con los números del 1 al 10
# print(lista) # Imprimimos la lista

# Ejemplo de lista con cadenas de texto a enteros:
# lista = ['1', '2', '3', '4', '5']
# lista_enteros = [int(i) for i in lista] # Creamos una lista con los números de la lista anterior pero como enteros
# print(lista_enteros) # Imprimimos la lista de enteros -> [1, 2, 3, 4, 5]

# Recursos sobre compresión de listas: 
# https://blog.finxter.com/como-convertir-una-lista-de-cadenas-en-una-lista-de-enteros-en-python/