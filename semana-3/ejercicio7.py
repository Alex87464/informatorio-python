# 7-Escribe un programa que pida al usuario una palabra y determine si es un 
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
# Ejemplos de palabras palíndromo -> ana, reconocer, neuquen, radar, somos, etc.

palabra = str(input("Ingrese una palabra: "))

palabra_invertida = ""

# Creamos un ciclo for que itere desde la última letra de la palabra hasta la primera
for i in range(len(palabra)-1, -1, -1):
    # En cada iteración del ciclo for, vamos a guardar la letra en la variable palabra_invertida
    palabra_invertida = palabra_invertida + palabra[i]

# Ahora comparamos si la palabra ingresada es igual a la palabra invertida
if palabra == palabra_invertida: # <- Si son iguales quiere decir que la palabra es palíndromo
    print("La palabra `" + palabra +  "` si es un palíndromo")
else: # <- Caso contrario no es palíndromo
    print("La palabra `" + palabra + "` no es un palíndromo")