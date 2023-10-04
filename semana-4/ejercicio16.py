"""
16-Crea una función llamada eliminar_duplicados que tome una lista como
parámetro y devuelva una nueva lista sin duplicados, conservando el orden
original.
"""


def eliminar_duplicados(lista):
    resultado = [] # Arreglo auxiliar donde voy a guardar las palabras no repetidas
    
    for item in lista: # Recorro el arreglo recibido por parametro en la funcion
        if item not in resultado: # Si el elemento actual no está en mi array resultado
            resultado.append(item) # Agrego el elemento al arreglo auxiliar
    
    return print(resultado) # Imprimo el resultado
    
eliminar_duplicados([1, 1, 1, 2, 3, 3, 4, 'x', 'x']) # Debería retornar 1,2,3,4,'x'