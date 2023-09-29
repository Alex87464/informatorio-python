# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

# Ejemplo si el usuario ingresa 5, el programa debe imprimir el resultado 
# de 1 + 2 + 3 + 4 + 5 = 15

numero = int(input("Ingrese un número: "))
suma = 0
for i in range(1, numero + 1):
    suma = suma + i
print(suma)