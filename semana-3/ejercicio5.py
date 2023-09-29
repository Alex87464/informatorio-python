# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.
# Acá podemos aplicar los conceptos de los ejercicios 2 y 4

# Creamos la variable donde guardamos la suma de los números
suma = 0
# Creamos un ciclo for que itere desde 1 hasta 100 usando la función range
for i in range(1, 101):
    # Si el resto de la división entre el número actual del ciclo for y 2 es igual a 0
    # entonces el número es par
    if i % 2 == 0: # <- Si se cumple que el número es par
        suma = suma + i # Sumamos el valor de i a la variable suma
        
print(suma) # Imprimimos el resultado de la suma