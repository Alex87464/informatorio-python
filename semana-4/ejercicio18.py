"""
18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
números como parámetro y devuelva la mayor diferencia entre el numero mas
alto y el numero mas bajo en la lista.
"""

def calcular_mayor_diferencia(numeros):
    
    # Retorno la diferencia entre el valor máximo y mínimo de la lista números
    return print(f"La máxima diferencia en esta lista es de {max(numeros) - min(numeros)}, por los números '{max(numeros)}' y '{min(numeros)}' ") 
    
    
calcular_mayor_diferencia([10, 27, 44, 31, 19, 24, 9]) 
# Debería retornar 35 dado que el numero menor es 9 y el mayor es 44. 44-9 = 35