
import os
from random import choice
import time

listaAnimales = ['tortuga','perro','gato','loro','jirafa','elefante','aguila','pinguino','ballena']
pistaAnimales = ['Marino y terreste','Mascota','Mascota','Volador','Africa','Africa','Volador','Antartida','Gran animal Marino']

listaCuerpoHumano = ['nariz','boca','brazo','pierna','cabeza','ojo','lengua','hombro']
pistaCuerpoHumano = ['Rostro','Rostro','Cuerpo','Cuerpo','Cuerpo','Rostro','Rostro','Cuerpo']

listaUniverso = ['saturno','venus','marte','jupiter','nebulosa','estrella','planeta','constelacion']
pistaUniverso = ['Nuestro Sistema Solar','Nuestro Sistema Solar','Nuestro Sistema Solar','Nuestro Sistema Solar','Gran objeto gaseoso','Parte de nuestro sistema solar','Nuestro Sistema Solar','Se ve desde la tierra']

listaVarios = ['bicicleta','arbol','pizarra','lluvia','escritorio','lampara','casa']
pistaVarios = ['Objeto del hogar','Naturaleza','Objeto para enseñar','Naturaleza','Objeto para estudiar','Brinda luz','Hogar']

#MENUS
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

#AHORCADO
def mostrarAho5():
    print('--------------0--------------')
    print('___________')
    print('|_/      |')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|__________')
    print('|____________|')

def mostrarAho4():
    print('--------------0--------------')
    print('___________')
    print('|_/      |')
    print('|_|      O')
    print('|_|      |')
    print('|_|      |')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|__________')
    print('|____________|')

def mostrarAho3():
    print('--------------0--------------')
    print('___________')
    print('|_/      |' )
    print('|_|      O' )
    print('|_|     \| ' )
    print('|_|      |')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|__________')
    print('|____________|')

def mostrarAho2():
    print('--------------0--------------')
    print('___________')
    print('|_/      |' )
    print('|_|      O' )
    print('|_|     \|/' )
    print('|_|      |')
    print('|_|')
    print('|_|')
    print('|_|')
    print('|_|__________')
    print('|____________|')

def mostrarAho1():
    print('--------------0--------------')
    print('___________')
    print('|_/      |' )
    print('|_|      O' )
    print('|_|     \|/' )
    print('|_|      |')
    print('|_|     /  ')
    print('|_|')
    print('|_|')
    print('|_|__________')
    print('|____________|')

def mostrarAho0():
    print('--------------0--------------')
    print('___________')
    print('|_/      |')
    print('|_|      O')
    print('|_|     \|/' )
    print('|_|      |')
    print('|_|     / \ ')
    print('|_|')
    print('|_|')
    print('|_|__________')
    print('|____________|')

#UN JUGADOR
def unJugador(num):
    if num == '1':
        aleatorio = choice(listaAnimales)
        a = listaAnimales.index(aleatorio)
        b =  pistaAnimales [a]
    elif num == '2':
        aleatorio = choice(listaCuerpoHumano)
        a = listaCuerpoHumano.index(aleatorio)
        b =  pistaCuerpoHumano [a]
    elif num == '3':
        aleatorio = choice(listaUniverso)
        a = listaUniverso.index(aleatorio)
        b =  pistaUniverso [a]
    elif num == '4':
        aleatorio = choice(listaVarios)
        a = listaVarios.index(aleatorio)
        b =  pistaVarios [a]
    else:
        mostrarMenu1()
    palabra = ""
    vidas=5
    while vidas > 0:
        os.system('cls')
        if vidas == 5:
            mostrarAho5()
        elif vidas == 4:
            mostrarAho4()
        elif vidas == 3:
            mostrarAho3()
        elif vidas == 2:
            mostrarAho2()
        elif vidas == 1:
            mostrarAho1()
        print('')
        print('Pista |||', b,'   |||')
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
            os.system('cls')
            mostrarAho0()
            print(" ")
            print("Fin del juego, Perdiste")
            print("")
            time.sleep(3)
    else:
        print("Bien jugado!!")

#MULTIJUGADOR
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
        if vidas == 5:
            mostrarAho5()
        elif vidas == 4:
            mostrarAho4()
        elif vidas == 3:
            mostrarAho3()
        elif vidas == 2:
            mostrarAho2()
        elif vidas == 1:
            mostrarAho1()
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
            os.system('cls')
            mostrarAho0()
            print(" ")
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
            unJugador('1')
        elif opcion1 == '2':
            os.system('cls')
            print('Seccion Cuerpo Humano')
            unJugador('2')
        elif opcion1 == '3':
            os.system('cls')
            print('Seccion UNIVERSO')
            unJugador('3')
        elif opcion1 == '4':
            os.system('cls')
            print('Seccion VARIOS')
            unJugador('4')
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