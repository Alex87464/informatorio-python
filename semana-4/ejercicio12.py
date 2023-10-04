"""
12-Crea una función llamada convertir_temperatura que tome una temperatura
en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
es: Fahrenheit = (Celsius * 9/5) + 32. 
"""

def convertir_temperatura(temperatura_en_celcius):
    
    temperatura_en_farenheit = (temperatura_en_celcius * 9/5) + 32
    
    print(f"La temperatura {temperatura_en_celcius}°C en Farenheit es {temperatura_en_farenheit}°F")
    
convertir_temperatura(20) # 20°C a Farenheit son 68°F