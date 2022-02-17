'''
repetitiva_while_2.py
script en python que sume sus valores pares y multiplique valores impares el usuario no puede ingresar un 0. Se debera utilizar la estructura repetitiva"while" para solicitar al usuario un numero y dependiendo del numero lo suma o lo multiplica.
'''

print('Programa que suma los numeros pares y multiplica los impares')

suma = 0
multiplicacion = 1

numero = -1

while numero != 0:
    numero = int(input('Ingrese un numero(0 para salir)'))
    if numero % 2 == 0:
        suma = suma + numero
    else:
        multiplicacion = multiplicacion * numero


        print(f'suma:{suma}')
        print(f'multplicacion:{multiplicacion}')

print ('nos vemos')
