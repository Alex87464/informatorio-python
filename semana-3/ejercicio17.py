# 17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con las palabras en orden inverso.

# Guardamos el texto que escriba el usuario
cadena = input("Escribe una cadena de texto: ")

# Imprimimos un mensaje con la cadena de texto en orden inverso
print("La cadena de texto en orden inverso es: ", end="") # end="" -> No imprime un salto de línea al final asi que podemos seguir imprimiendo en la misma línea

# cadena.split() -> Separa la cadena de texto en palabras
# cadena.split()[::-1] -> Separa la cadena de texto en palabras y las invierte <- (ver 'slicing' al final de este archivo)
for palabra in cadena.split()[::-1]: # Separamos la cadena de texto en palabras y las imprimimos en orden inverso
    print(palabra, end=" ") # Imprimimos la palabra y un espacio
print() # Imprimimos un salto de línea

# Recurso sobre slicing:
# Leer '4.1.3. Slicing avanzado: cambiando el paso' en el siguiente link:
# https://cupi2-ip.github.io/IPBook/nivel3/seccion3-4.html

# Para que sirve "end" en print:
# https://es.quora.com/Para-qu%C3%A9-sirve-end-en-Python#:~:text=%22end%22%20es%20un%20par%C3%A1metro%20opcional,de%20imprimir%20el%20contenido%20especificado.