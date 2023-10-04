"""
7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número.
"""

def imprimir_pares(numero):
    
    for item in range(2, numero+1): # Creo una lista desde el 2 hasta el numero ingresado + 1
        if(item % 2 == 0): # Si el número actual es par
            print(item) # Lo imprimo
     

imprimir_pares(20)