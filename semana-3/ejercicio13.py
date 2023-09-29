# 13-Escribe un programa que pida al usuario un número y luego imprima un triángulo de asteriscos con esa cantidad de filas.

# Tomamos el número ingresado por el usuario
numero = int(input("Ingrese un número: "))

for i in range(numero): # Recorremos el rango del número ingresado por el usuario
    print("*" * (i + 1)) # Imprimimos el asterisco multiplicado por el número de la iteración + 1
    