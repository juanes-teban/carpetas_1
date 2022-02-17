'''
repetitiva_while_e.py
script en Python que implemente el juego de adivinar un numero, pero esta vez en modo competitivo. La computadora debera generar un numero aleatorio entre 1 y 100 y tanto el usuario como la computadora deberan intentar adivinar dicho numero. Para que el juego sea retador el jugador maquina debera ser "inteligente" y competir para ganar. El juego se realizara por turnos, primero la maquina y despues el usuario y por cada intento la computadora respondera si el numero es mayor o menor que el secreto.
'''
# Usuario #
import os
import random

inferior = 1
superior = 100
secreto = random.randint(1, 100)
usuario = -1
maquina = -1
while usuario != secreto and maquina != secreto:
     os.system('cls')
     print('Maquina, cual crees que sea el numero secreto? ')
     maquina = random.randint(inferior, superior)
     print(f'Maquina:{maquina}')
     if   maquina < secreto:
          print('Tu numero no alcanza el digito')
          inferior = inferior + 1
     elif maquina > secreto:
         print ('Tu numero es mayor')
         superior = maquina - 1
     else:
         print('Ha ganado la maquina')
     if maquina != secreto:
         usuario = int(input('Usuario, ¿Cual crees que sea el numero?'))
         if usuario < secreto:
              print('Tu numero no alcanza el digito')
              if usuario > inferior:
                  inferior = usuario + 1

         elif usuario > secreto:
               print('Tu numero sobrepasa el digito')
               if usuario < superior:
                   superior = usuario - 1
         else:
               print('El usuario ha ganado')
         input('Presiona enter para continuar...')

input('nos vemos...')
