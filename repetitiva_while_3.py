'''
repetitiva_while_3.py
script en Python que simule el sistema de validacion de plataforma digital. Se le solicitara al usuario su nombre y contraseña mientras la informacion proporcionada no coincida previamente registrada.
'''
import os

USER = 'juan'
PASSWORD = 'v1dr1o'

user = ''
password = ''
while USER != user or PASSWORD != password:
    os.system('cls')
    print('                    kit_kot')
    user = input('Usuario: ')
    password = input('Contraseña: ')

    if USER != user or PASSWORD != password:
         print('credenciales incorrectas')
         print('Intenta de nuevo')
         input('Presiona enter para continuar...')
    else:
         print('Bienvenid@')

    input ('nos vemos...')
