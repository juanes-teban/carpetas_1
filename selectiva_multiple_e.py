'''
selectiva_multiple_e.py
script en Python que le pida al usuario dos numeros y una operacion que quiera realizar con estos numeros
'''
RESTA='R'
SUMA='S'
DIVIDIR='D'
MULTIPLICACION='M'

print('''         CALCULADORA
Realiza una de las cuatro operaciones de tu calculadora
R)Resta

S)Suma

D)Division

M)Multiplicacion




''')

ope =input('Que operacion quieres realizar')

num_1 =int(input('Escribe un numero: '))
num_2 =int(input('Escribe otro numero: '))


 #posible error aqui#
if ope == 'R':
    residuo=int(num_1-num_2)
    print(f'La resta es {residuo}')
elif ope == 'S':
    sumatoria=int(num_1+num_2)
    print(f'La suma de los numeros es {sumatoria}')
    #Posible errror aqui#
elif ope=='M':
    producto=int(num_1*num_2)
    print(f'la multiplicacion de estos numeros es {producto}')


if ope =='D'and num_2!=0:
  division=int(num_1/num_2)
  print(f'La division es {division}')

else:print('operacion no encontrada')

print('Que tengas buen dia')
