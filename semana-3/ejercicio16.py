# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con cada palabra al revés.

# Por ejemplo, si el usuario ingresa la cadena "Hola, mundo", el programa
# debería imprimir "aloH, odnum".

# Nota: No es necesario invertir el orden de las palabras, solo invertir el
# orden de las letras de cada palabra.

# Guardamos la cadena de texto ingresada por el usuario
cadena = input('Ingrese una cadena de texto: ')

# Crear una lista con las palabras de la cadena
lista = cadena.split()

# Acá vamos a recorrer la lista y cada palabra invertirla
for i in range(len(lista)):
    lista[i] = lista[i][::-1] # Acá invertimos la palabra usando slicing (ver recurso al final)
    
# Unir la lista en una cadena
cadena = ' '.join(lista)
# Imprimir la cadena
print(cadena)

# Recurso sobre slice: 
# Leer '4.1.3. Slicing avanzado: cambiando el paso' en el siguiente link:
# https://cupi2-ip.github.io/IPBook/nivel3/seccion3-4.html