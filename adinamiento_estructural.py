'''
adinamiento_estructural.py
script en Python que simula un juego de preguntas y respuestas si el usuario contesta correctamente una pregunta puede continuar con la siguiente, en caso de fallar se le indica que ha perdido.
Si contesta acertadamente todas las preguntas se le felicita por su conocimiento.
'''
print('Bienvenid@ pongamos a prueba tu conocimiento :v')
respuesta =int(input('¿cual es la velocidad de la luz en m/s'))
if respuesta == 299792458:
    print('¡Correcto!')
    respuesta = int(input('¿Cuanto es 8+8/8*8? '))
    if respuesta == 8+8/8*8:
        print('¡Correcto!')
        respuesta =input('De que color eran las mangas de napoleon')
        if respuesta == 'los chalecos no tienen mangas':
            print('Felicidades eres un crack')
        else:
            print('Lo siento, respuesta incorrecta')
    else:
        print('Lo siento, la respuesta es incorrecta')
else:
    print('Lo siento, la respuesta es incorrecta')


print('nos vemos')    
