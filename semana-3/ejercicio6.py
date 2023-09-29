# 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma palabra pero con las letras en orden inverso.

# En esta variable guardamos la palabra que ingresa el usuario
palabra = str(input("Ingrese una palabra: "))

# En esta variable vamos a guardar las letras pero en orden inverso
palabra_invertida = ""

# Creamos un ciclo for que itere desde la última letra de la palabra hasta la primera
for i in range(len(palabra)-1, -1, -1): # <- El tercer parámetro es el paso, en este caso -1
    # En cada iteración del ciclo for, vamos a guardar la letra en la variable palabra_invertida
    palabra_invertida = palabra_invertida + palabra[i]

print(palabra_invertida) # Imprimimos la palabra invertida

# Explicación del range usado en el ciclo for

# len(palabra) <- Calcula la longitud de la palabra ingresada por el usuario

# range(len(palabra)-1, -1, -1) <- crea un rango que comienza desde el índice de la última letra 
# de la palabra (len(palabra)-1), va hacia atrás hasta el índice 0 (-1), 
# y el tercer parámetro -1 especifica que el rango se decrementará en -1 en cada iteración. 
# Esto garantiza que el ciclo itere desde la última letra hasta la primera, en orden inverso.

# Ejemplo con una palabra de longitud 6
# range(5, -1, -1) -> [5, 4, 3, 2, 1, 0]
