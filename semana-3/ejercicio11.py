"""
11-Escribe un programa que pida al usuario un número y calcule su factorial.
Un factorial es el producto que resulta de multiplicar un número entero positivo
dado por todos los enteros inferiores a él hasta el uno.
Por ejemplo, el factorial de 4 es 4! = 4 * 3 * 2 * 1 = 24.
o el factorial de (5!) es 120, es decir:
5! = 5 * 4 * 3 * 2 * 1 = 120
"""

# Acá guardamos el número ingresado por el usuario
numero = int(input("Ingrese un número entero positivo para calcular su factorial: "))
factorial = 1 # Iniciamos el factorial en 1

# Calculamos el factorial del número ingresado
for i in range(1, numero + 1): # el range va desde 1 hasta el número ingresado + 1 por ejemplo si el usuario ingresa 5, el range va desde 1 hasta 6
    factorial *= i # Multiplicamos el factorial por el número actual (i) del range

# Por último imprimimos el resultado
print("El factorial de", numero, "es:" ,factorial)