'''
repetitivas_desde_7.py
script en Python que al usuario una cantidad de numeros a registrar, le solicite dichos valores y finalmente imprima el promedio de los mismos.
'''
acumulador = 0
print('Calculador de promedio')
total_datos = int(input('¿Cuantos datos deseas registrar? '))

for valor in range(total_datos):
    numero = int(input(f'Ingresa el valor {valor+1}: '))
    acumulador += numero

promedio = acumulador/total_datos
print(f'promedio es {promedio}')

print('Nos vemos...')  
