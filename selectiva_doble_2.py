'''
selectiva_doble_2.py
script en Python que simule sistema de validacion de una plataforma digital. el usuario debera proporcionar tanto su nombre como la contarseña. Si los valores coinciden con los previamente almacenados entonces se le dara la bienvenida, sino se le indicar que hubo un error.
 '''

USER = 'Pep3'
PASSWORD = 'Nava132'

print('Proporciona los siguientes datos: ')
user = input('Usuario: ')
password = input('Contraseña: ')


if user == USER and password == PASSWORD:
    print('    insta[ª]')
    print('Bienvenid@ a tu cuenta')
else:
    print('Datos incorrectos, intenta de nuevo')

print('Que tengas un buen dia')        
