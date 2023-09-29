# 4-Escribe un programa que imprima los números pares del 1 al 100.
# Como saber si es par un numero?
# Los números pares son aquellos que tienen como múltiplo al número dos, es decir, 
# que se pueden dividir en una mitad exacta.
# Por ejemplo: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, etc.

# Creamos un ciclo for que itere desde 1 hasta 100
for i in range(1, 101):
    # Si el residuo de la división entre el número actual del ciclo for y 2 es igual a 0
    # entonces el número es par
    if i % 2 == 0: # <- Si se cumple que el número es par
        print(i) # Imprimimos el número en pantalla
        
        
# Link útil para comprender el operador '%' (módulo o residuo)
# https://www.freecodecamp.org/espanol/news/el-operador-del-modulo-python-que-significa-el-simbolo-de-porcentaje-en-python-resuelto/#:~:text=El%20s%C3%ADmbolo%20%25%20en%20Python%20se,de%20un%20problema%20de%20divisi%C3%B3n.