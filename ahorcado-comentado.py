import os
import random


# Lista de palabras
palabras = ["python", "programacion", "computadora", "inteligencia", "informatica"]

# Selecciona una palabra aleatoria con el método random
palabra_secreta = random.choice(palabras)

# Inicialización de variables
intentos = 6
letras_adivinadas = [] # Lista donde se guardan las letras correctas ingresadas
letras_incorrectas = [] # Lista donde se agregan las letras incorrectas ingresadas
# Estas listas se verifican después en caso de ingresar 2 veces la misma letra


# * Función que retorna el estado del personaje
# ? Recibe por parámetro el número de intentos dependiendo del valor 
# ? que reciba, se muestra un elemento con posición del intento
def mostrar_ahorcado(intentos):
    estados_ahorcado = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        '''
    ]
    return estados_ahorcado[intentos]


# Función para presentar la palabra oculta en consola. Ejemplo: python -> _ _ _ _ _ _ 
def mostrar_palabra_oculta(palabra, letras_adivinadas): # Recibe la palabra secreta y las letras adivinadas
    resultado = "" # Variable que almacena el resultado
    for letra in palabra: # Ciclo que recorre la palabra secreta
        if letra in letras_adivinadas: # Verifica si la letra está en la lista de letras adivinadas
            resultado += letra # Si está, la agrega a la variable resultado
        else:
            resultado += "_" # Si no está, agrega un guión bajo
    return resultado # Retorna el resultado

# Función para limpiar la pantalla de la consola y que no quedé todo el historial de letras ingresadas
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ciclo principal del juego
while True:
    limpiar_consola() # Limpia la consola con la función limpiar_consola()
    # Muestra el estado del juego
    print("\nPalabra:", mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)) # Muestra la palabra oculta
    print("Intentos restantes:", intentos) # Muestra los intentos restantes
    print("Letras incorrectas:", ", ".join(letras_incorrectas)) # Muestra las letras incorrectas separadas por coma
    print(mostrar_ahorcado(intentos))

    # Verificar si el jugador ha ganado
    if mostrar_palabra_oculta(palabra_secreta, letras_adivinadas) == palabra_secreta: # Comprueba si la palabra oculta es igual a la palabra secreta
        print("\n¡Felicidades! Has adivinado la palabra: " + palabra_secreta)
        break

    # Verificar si el jugador ha perdido
    if intentos == 0: # Si los intentos llegan a 0, el jugador pierde
        print("\n¡Lo siento, has perdido! La palabra era: " + palabra_secreta) # Muestra la palabra secreta
        break

    # Solicitar una letra al jugador
    letra = input("Ingresa una letra: ").lower()

    # Verificar si la letra ingresada es válida
    if len(letra) != 1 or not letra.isalpha(): # Comprueba si la letra ingresada es una sola letra y si es alfabética
        print("Por favor, ingresa una sola letra válida.")
        continue

    # Verificar si la letra ya se ha adivinado antes
    if letra in letras_adivinadas or letra in letras_incorrectas: # Comprueba si la letra ingresada está en las listas de letras adivinadas o incorrectas
        print("Ya has adivinado esa letra antes.")
        continue

    # Verificar si la letra está en la palabra secreta
    if letra in palabra_secreta: # Comprueba si la letra ingresada está en la palabra secreta
        letras_adivinadas.append(letra) # Si está, la agrega a la lista de letras adivinadas
    else:
        letras_incorrectas.append(letra) # Si no está, la agrega a la lista de letras incorrectas
        intentos -= 1 # Resta un intento