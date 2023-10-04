"""
19-Escribe un programa que pida al usuario un número y luego imprima si ese
número es un número perfecto o no. Un número perfecto es aquel que es igual a
la suma de sus divisores propios (excluyendo el propio número).
Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

Ejemplos de numeros perfectos:
6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14
496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
"""

numero = int(input("Ingrese un número positivo: "))
suma_divisores = 0

if numero <= 0:
    print("Ingrese un número positivo.")
else:
    for i in range(1, numero // 2 + 1):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        print(f"{numero} es un número perfecto.")
    else:
        print(f"{numero} no es un número perfecto.")