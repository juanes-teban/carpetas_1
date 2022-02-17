'''
repetitiva_while_4.py
script en Python que muestre un menu con distintos personajes de un  videojuego. Si el usuario selecciona alguno de los personajes, se le mostraran sus caracteristicas. El menu sera ciclico y se mostrara mientras el usuario no indique que desa salir.
'''
import os

MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 4
#bandera
continuar = True
while continuar:
    os.system('cls')
    print(f'''             Personajes
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir
    ''')
opc = int(input('Selecciona tu personaje: '))

if opc == MAGO:
        print('''

         Fuerza: 22
         Energia: 25
         Especial: 98

    ''' )
elif opc == GUERRERO:
          print('''

          Fuerza:98
          Energia:50
          Especial:7

    ''')

elif opc == SACERDOTISA:

           print(''''

           Fuerza: 36
           Energia: 7
           Especial: 20

    ''')
elif opc == SALIR:
        continuar = False

else:
    print('Opcion no valida')

input('Presiona enter para continuar')

input('Que tengas un buen dia')
