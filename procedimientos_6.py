'''
procedmientos_6.py
script en Python que implemente un procedimiento que reciba el nombre y la edad del usuario y en caso que la edad sea mayor o igual que 18 le indique que ya es mayor edad; en caso contrario le indique que es menor de edad
'''

def mayoria_edad(nombre, edad):
    print(f'Que tengas buen dia {nombre}')
    if edad >= 18:
        print('Ya eres mayor de edad')
    else:
        print('todavia no eres mayor de edad')



mayoria_edad('Juan', 18)
print('Nos vemos...')
