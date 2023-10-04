"""
9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números.
"""

numeros = [1, 2, 3, 4, 5]

def promedio(numeros):
    print(f"El promedio de la lista ingresada es {sum(numeros)/len(numeros)}")
    # Imprimo la division entre la suma total de todos los numeros en la lista
    # divido la cantidad de numeros en la lista (en este caso 5)
    # 1+2+3+4+5=15
    # 15 / 5 = 3

promedio(numeros)
    

# Recursos
# sum():    https://thedataschools.com/python/funciones/sum-funcion/
#           https://www.w3schools.com/python/ref_func_sum.asp

 