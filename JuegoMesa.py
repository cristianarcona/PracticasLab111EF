
import os
from random import choice
import time

listaAnimales = ['tortuga','perro','gato','loro','jirafa','elefante','aguila','pinguino','ballena']
listaCuerpoHumano = ['nariz','boca','brazo','pierna','cabeza','ojo','lengua','hombro']
listaUniverso = ['saturno','venus','marte','jupiter','nebulosa','estrella','planeta','constelacion']
listaVarios = ['bicicleta','arbol','pizarra','lluvia','escritorio','lampara','casa']


def mostrarMenu():
    print('')
    print('-------------------------------------- 0 --------------------------------------')
    print('                       BIENVENIDO AL JUEGO DEL AHORCADO')
    print('')
    print('Seleccione el modo de Juego:')
    print('')
    print('     1. Palabra al azar (UN JUGADOR)')
    print('     2. Introduce una palabra (MULTIJUGADOR)')
    print('     0. Salir')
    print('')

def mostrarMenu1():
    print('Seleccione un grupo:')
    print('')
    print('     1. Animales')
    print('     2. Cuerpo Humano')
    print('     3. Universo')
    print('     4. Varios')
    print('     0. Volver al Menu Principal')
    print('')

def animales():
    aleatorio = choice(listaAnimales)
    palabra = ""
    vidas=5
    while vidas > 0:
        os.system('cls')
        print('')
        print('Pista |||   ANIMALES   |||')
        print('')
        print("--------------0--------------")
        print("")
        print("Letras utilizadas: "+ palabra )
        print("")
        print("Vidas Restantes: ",+vidas)
        print("")
        print("")
        fallas = 0
        for letra in aleatorio:
            if letra in palabra:
                print(letra, end="")
            else:
                print("_ ", end="")
                fallas = fallas + 1
        if fallas == 0:
            print("  GANASTE!!!!")
            print("")
            time.sleep(3)
            break
        print("")
        print("")
        letra=input("Introduce una letra: ")
        print("")
        palabra = palabra + letra + " "
        print("")
        if letra not in aleatorio:
            vidas = vidas - 1
        if vidas == 0:
            print("Fin del juego, Perdiste")
            print("")
            time.sleep(3)
    else:
        print("Bien jugado!!")

def cuerpoHumano():
    aleatorio = choice(listaCuerpoHumano)
    palabra = ""
    vidas=5
    while vidas > 0:
        os.system('cls')
        print('')
        print('Pista |||  CUERPO HUMANO   |||')
        print('')
        print("--------------0--------------")
        print("")
        print("Letras utilizadas: "+ palabra )
        print("")
        print("Vidas Restantes: ",+vidas)
        print("")
        print("")
        fallas = 0
        for letra in aleatorio:
            if letra in palabra:
                print(letra, end="")
            else:
                print("_ ", end="")
                fallas = fallas + 1
        if fallas == 0:
            print("  GANASTE!!!!")
            print("")
            time.sleep(3)
            break
        print("")
        print("")
        letra=input("Introduce una letra: ")
        print("")
        palabra = palabra + letra + " "
        print("")
        if letra not in aleatorio:
            vidas = vidas - 1
        if vidas == 0:
            print("Fin del juego, Perdiste")
            print("")
            time.sleep(3)
    else:
        print("Bien jugado!!")

def universo():
    aleatorio = choice(listaUniverso)
    palabra = ""
    vidas=5
    while vidas > 0:
        os.system('cls')
        print('')
        print('Pista |||  UNIVERSO   |||')
        print('')
        print("--------------0--------------")
        print("")
        print("Letras utilizadas: "+ palabra )
        print("")
        print("Vidas Restantes: ",+vidas)
        print("")
        print("")
        fallas = 0
        for letra in aleatorio:
            if letra in palabra:
                print(letra, end="")
            else:
                print("_ ", end="")
                fallas = fallas + 1
        if fallas == 0:
            print("  GANASTE!!!!")
            print("")
            time.sleep(3)
            break
        print("")
        print("")
        letra=input("Introduce una letra: ")
        print("")
        palabra = palabra + letra + " "
        print("")
        if letra not in aleatorio:
            vidas = vidas - 1
        if vidas == 0:
            print("Fin del juego, Perdiste")
            print("")
            time.sleep(3)
    else:
        print("Bien jugado!!")

def varios():
    aleatorio = choice(listaVarios)
    palabra = ""
    vidas=5
    while vidas > 0:
        os.system('cls')
        print('')
        print('Pista |||  VARIOS (MODO DIFICIL)   |||')
        print('')
        print("--------------0--------------")
        print("")
        print("Letras utilizadas: "+ palabra )
        print("")
        print("Vidas Restantes: ",+vidas)
        print("")
        print("")
        fallas = 0
        for letra in aleatorio:
            if letra in palabra:
                print(letra, end="")
            else:
                print("_ ", end="")
                fallas = fallas + 1
        if fallas == 0:
            print("  GANASTE!!!!")
            print("")
            time.sleep(3)
            break
        print("")
        print("")
        letra=input("Introduce una letra: ")
        print("")
        palabra = palabra + letra + " "
        print("")
        if letra not in aleatorio:
            vidas = vidas - 1
        if vidas == 0:
            print("Fin del juego, Perdiste")
            print("")
            time.sleep(3)
    else:
        print("Bien jugado!!")

def nuevaPalabra():
    aleatorio=input("JUGADOR 1 Ingrese una palabra: ")
    print("Palabra Elegida: ", aleatorio)
    print("")
    print("El juego empezará en 5 segundos")
    print("")
    print("JUGADOR 2, PREPARESE!!!!!!!")
    time.sleep(5)
    palabra = ""
    vidas=5
    while vidas > 0:
        os.system('cls')
        print("--------------0--------------")
        print("")
        print("Letras utilizadas: "+ palabra )
        print("")
        print("Vidas Restantes: ",+vidas)
        print("")
        print("")
        fallas = 0
        for letra in aleatorio:
            if letra in palabra:
                print(letra, end="")
            else:
                print("_ ", end="")
                fallas = fallas + 1
        if fallas == 0:
            print("  GANASTE JUGADOR 2!!!!")
            print("")
            time.sleep(3)
            break
        print("")
        print("")
        letra=input("Introduce una letra: ")
        print("")
        palabra = palabra + letra + " "
        print("")
        if letra not in aleatorio:
            vidas = vidas - 1
        if vidas == 0:
            print("Fin del juego, GANO JUGADOR 1")
            print("")
            time.sleep(3)
    else:
        print("Bien jugado!!")

while True:
    os.system('cls')
    mostrarMenu()
    opcion = input()
    if opcion == '1':
        os.system('cls')
        mostrarMenu1()
        opcion1 = input()
        if opcion1 == '1':
            os.system('cls')
            animales()
        elif opcion1 == '2':
            os.system('cls')
            print('Seccion Cuerpo Humano')
            cuerpoHumano()
        elif opcion1 == '3':
            os.system('cls')
            print('Seccion UNIVERSO')
            universo()
        elif opcion1 == '4':
            os.system('cls')
            print('Seccion VARIOS')
            varios()
        elif opcion1 == '0':
            os.system('cls')
            mostrarMenu()
        else:
            print('Dato Erroneo, Vuelva a seleccionar una opcion')
            mostrarMenu1
    elif opcion == '2':
        os.system('cls')
        nuevaPalabra()
    elif opcion == '0':
        os.system('cls')
        print('Hasta pronto!!!')
        break
    else:
        print('Dato erroneo, Fin del Programa')
        break