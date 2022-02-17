'''
procedimientos_4.py
script en Python que muestre un menú cíclico;dicho menú será implementado en un procedimiento.
'''
import os
ESP = 1
ING = 2
NO_SUBS = 3
SALIR = 4

def mostrar_menu():
    print(f'''       Subtitulos
    {ESP}) Español
    {ING}) Ingles
    {NO_SUBS}) No subtitulos
    {SALIR}) Salir
    ''')

continuar = True
while continuar:
    os.system('cls')
    mostrar_menu()
    opc = int(input('Selecciona una opción: '))
    os.system('cls')
    if opc == ESP:
        os.system('cls')
        print('Subtitulos en Español')
    elif opc == ING:
        print('Subtitulos en Ingles')
    elif opc == NO_SUBS:
        print('Sin subtitulos')
    elif opc == SALIR:
        continuar = False
    else:print('Opcion no válida')
    input('Presiona enter para continuar')

print('Nos vemos')
