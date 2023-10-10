# Grupo 4: Ivana Josefina Verbek / Alex Fabricio Oliva Schumann

import os
import random

palabras = ["python", "programacion", "computadora", "inteligencia", "informatica"]

palabra_secreta = random.choice(palabras)


intentos = 6
letras_adivinadas = []
letras_incorrectas = []

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


def mostrar_palabra_oculta(palabra, letras_adivinadas): 
    resultado = "" 
    for letra in palabra: 
        if letra in letras_adivinadas: 
            resultado += letra 
        else:
            resultado += "_" 
    return resultado 


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    limpiar_consola() 
    
    print("\nPalabra:", mostrar_palabra_oculta(palabra_secreta, letras_adivinadas)) 
    print("Intentos restantes:", intentos) 
    print("Letras incorrectas:", ", ".join(letras_incorrectas)) 
    print(mostrar_ahorcado(intentos))

    
    if mostrar_palabra_oculta(palabra_secreta, letras_adivinadas) == palabra_secreta: 
        print("\n¡Felicidades! Has adivinado la palabra: " + palabra_secreta)
        break

    
    if intentos == 0: 
        print("\n¡Lo siento, has perdido! La palabra era: " + palabra_secreta) 
        break

    
    letra = input("Ingresa una letra: ").lower()

    
    if len(letra) != 1 or not letra.isalpha(): 
        print("Por favor, ingresa una sola letra válida.")
        continue

    
    if letra in letras_adivinadas or letra in letras_incorrectas: 
        print("Ya has adivinado esa letra antes.")
        continue

    
    if letra in palabra_secreta: 
        letras_adivinadas.append(letra) 
    else:
        letras_incorrectas.append(letra) 
        intentos -= 1 