'''
procedimientos_5.py
script en Python que implemente un procedimiento que reciba el nombre del usuario como argumento e imprima un saludo personalizado.
'''
def saludo(nombre):
    print(f'Hola {nombre},gusto en conocerte')

n = input('¿Como te llamas?')

saludo(n)

print('Nos vemos...')
