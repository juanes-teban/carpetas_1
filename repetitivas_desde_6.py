'''
repetitivas_desde_6.py
script en Python que muestre uno a uno los simbolos de una palabra o frase. Por ejemplo si la frase fuera "Hola" se deberia imprimir:
H
o
l
a
'''
frase = input('Ingrese una frase o palabra: ')
print('Los simbolos de tu frase/palabra son: ')

for simbolo in frase:
    print(f'{simbolo}')

print('Nos vemos..')    
