'''
repetitivas_desde_e.py
scipt en Python que muestre un cronometro en formato de 24 horas.
El despliegue seguira el formato h:m:s. El cronometro debera iniciar en 0:0:0 y podra llegar hasta 23:59:59. Implementar retardos de 1 segundo y limpieza y limpieza de pantalla de forma tal que solo se vea un tiempo en pantalla.
'''
import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system('cls')
            print(f'{hora}:{minuto}:{segundo}')
            time.sleep(1)
