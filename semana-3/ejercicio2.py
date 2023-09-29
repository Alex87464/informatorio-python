# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

# Ejemplo si el usuario ingresa 5, el programa debe imprimir el resultado 
# de 1 + 2 + 3 + 4 + 5 = 15

# Creamos la variable donde guardamos el número ingresado por el usuario
numero = int(input("Ingrese un número: "))

suma = 0 # Creamos la variable donde guardamos la suma de los números
for i in range(1, numero + 1): # Iteramos desde 1 hasta el número ingresado
    suma = suma + i # Sumamos el valor de i a la variable suma
print(suma) # Imprimimos el resultado de la suma