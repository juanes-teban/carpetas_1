'''
selectiva_multiple_1.py
script en Python en donde el ususario ingrese su calificacion y numero de asistencias luego que se le indique si aprobo o no y se le indique la razon del porque paso o no.La calificacion minima aprobatoria sera 60 y la cantidad minima de asistencias sera 24.
'''

MIN_CAL = 60
MIN_ASI = 24

print('Por favor ingresa los siguientes datos: ')
cal = int(input('Calificacion: '))
asi = int(input('Asistencia: '))

if cal >=MIN_CAL and asi >= MIN_ASI:
    print('¡Felicidades aprobaste este curso!')
elif cal < MIN_CAL and asi >= MIN_ASI:
    print(f'Calificacion insuficiente.El minimo es {MIN_CAL}')
elif cal >= MIN_CAL and asi < MIN_ASI:
    print(f'Asistencia insuficiente.El minimo es {MIN_ASI}')
else:
    print('Calificacion y asistencias insuficientes.')

print('Que tengas un buen dia')
