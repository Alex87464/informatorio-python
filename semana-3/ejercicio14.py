# 14-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Tomamos el número ingresado por el usuario
numero = int(input("Ingrese un número: "))

for i in range(numero): # Recorremos el rango del número ingresado por el usuario
    print( str(i + 1) * (i + 1) ) # Imprimimos el número de la iteración multiplicado por el número de la iteración + 1
    # Es importante tener en cuenta el str() para convertir el número a string
    # De lo contrario, el programa hará la multiplicación de números y no de strings
    
    # Descomentá la siguiente línea si ver el error que se genera
    # print( (i + 1) * (i + 1) )