"""
13-Crea una función llamada calcular_descuento que tome dos parámetros:
precio y porcentaje_descuento. La función debe calcular y devolver el precio
después de aplicar el descuento. 
"""

def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * ((porcentaje_descuento/100))
    return print(f"El precio ${precio} con un descuento del {porcentaje_descuento}% es ${precio - descuento}")

# calcular_descuento(100, 20) # Tendría que retornar $80 dado que el 20% de 100 es 80
calcular_descuento(130, 10) # Tendría que retornar $117 dado que el 10% de 130 es 13 