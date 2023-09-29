# 3- Escribe un programa que pida al usuario un número y luego imprima la tabla de 
# multiplicar correspondiente a ese número del 1 al 10.

"""
Ejemplo: si el usuario ingresa 5, el programa debe imprimir:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""

# En esta variable guardamos el número de la tabla de multiplicar
numero = int(input("Ingrese un número: ")) 

    # NOTA: range es una función que nos permite crear una lista de números
    # en este caso creamos una lista de números desde 1 hasta 10 (el 11 no se incluye)
for i in range(1, 11): # Iteramos desde 1 hasta 10
    print(f"{numero} x {i} = {numero * i}") 
    # Imprimimos en pantalla la multiplicacion entre el `numero` ingresado por el usuario
    # y el valor de i en cada iteración del ciclo for
    
    