'''
repetitivas_desde_4.py
script en Python que muestre la tabla de multiplicar de un numero ingresado por el usuario. El usuario tambien podra ingresar hasta que valor llegara la tabal de multiplicar.
'''
numero = int(input('¿De que numero desea ver la tabla de multiplicar?'))
limite = int(input('¿Hasta que punto deseas ver?'))

print(f'       Tabla del {numero} ')
for multiplo in range(1, limite+1):
    print(f'{numero} x {multiplo} = {numero * multiplo}')

print('Nos vemos...')
