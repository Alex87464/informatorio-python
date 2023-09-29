# 9-Escribe un programa que pida al usuario un número y luego imprima la secuencia de Fibonacci correspondiente a ese número.

# Tomamos el número ingresado por el usuario
numero_ingresado = int(input("Ingrese un número entero para generar la secuencia de Fibonacci: "))

# Inicializar los primeros dos números de la secuencia de Fibonacci
fibonacci = [0, 1]

# Generar la secuencia de Fibonacci hasta el número ingresado
while fibonacci[-1] + fibonacci[-2] <= numero_ingresado:
    siguiente_numero = fibonacci[-1] + fibonacci[-2] # El siguiente número es la suma de los dos últimos números de la secuencia
    fibonacci.append(siguiente_numero) # Agregamos el siguiente número a la secuencia

# Imprimir la secuencia de Fibonacci
print("Secuencia de Fibonacci hasta", numero_ingresado, ":")
print(fibonacci) # Imprimimos la secuencia de Fibonacci generada en el bucle while

# Recurso para comprender que es la secuencia de Fibonacci:
# https://www.educ.ar/recursos/132013/la-matematica-incrustada-en-la-inmensa-variedad-de-formas-de-vida#:~:text=En%20matem%C3%A1tica%2C%20la%20sucesi%C3%B3n%20de,%2C%20610%2C%20987%2C%201597%E2%80%A6

