"""
18-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 3
4 5 6
7 8 9 10
"""

# Variable que almacena el número ingresado por el usuario
n = int(input("Ingrese un número: "))

numero = 1 # Variable que almacena el número a imprimir

for i in range(1, n + 1): # Imprimimos n filas
    for j in range(i): # Imprimimos i números
        print(numero, end=" ")
        numero += 1 # Incrementamos el número
    print()  # Salto de línea después de cada fila
    
# Fin del programa