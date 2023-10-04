"""
10-Crea una función llamada calcular_factorial que tome un número entero como
parámetro y devuelva el factorial de ese número. El factorial de un número
entero positivo n se define como el producto de todos los números enteros
positivos desde 1 hasta n.
"""

def calcular_factorial(numero):
    factorial = 1 # Iniciamos el factorial en 1

    # Calculamos el factorial del número ingresado
    for i in range(1, numero + 1): # El range va desde 1 hasta el número ingresado
        factorial *= i # Multiplicamos el factorial por el número actual (i) del range
        
    print(factorial)
    
calcular_factorial(5) # Deberia retornar 120 dado que 5! -> 5*4*3*2*1 = 120 
     