'''
procedimientos_3.py
acript en Python que dentro de un procedimiento solicite el nombre y la edad del usuario y en caso de ser mayor o igual que 18 le indique que es mayor de edad, en caso contrario indicarle que aun es menor.
'''
def mayoria_edad():
    nombre=input('Hola ¿Cómo te llamas?')
    edad = int(input('¿Cual es tu edad?'))
    if edad >=18:
        print('Ya eres mayor de edad')
    else:
        print(f'Aun eres menor, {nombre}')
mayoria_edad()
print('Nos vemos...')
