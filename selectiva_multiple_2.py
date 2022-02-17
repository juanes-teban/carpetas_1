'''
selectiva_multiple_2.py
script en Python que muestre un menu en los nombres de distintos paises de america y si el usuario selecciona algunas de las opciones se le mostrara el nombre de la capital de ese pais
'''

COLOMBIA=1
URUGUAY=2
MEXICO=3
ARGENTINA=4
ECUADOR=5
PERU=6
print('''           Capitales de America
1)Colombia
2)Uruguay
3)Mexico
4)Argentina
5)Ecuador
6)Peru

''')
opc = int(input('Seleciona una opcion: '))

if opc == COLOMBIA:
    print('Bogota')
elif opc == URUGUAY:
    print('Montevideo')
elif opc == MEXICO:
    print('Ciudad de Mexico')
elif opc == ARGENTINA:
    print('Buenos Aires')
elif opc == ECUADOR:
    print('Quito')
elif opc == Peru:
    print('Lima')
else: print('Opcion no valida')


print('Que tengas un buen dia')
