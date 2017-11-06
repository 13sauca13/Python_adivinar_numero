#Este juego es para Python 2.X
#Para Python 3.X hay que cambiar el "raw_input" por "input"

#Importa el modulo random para generar el numero aleatorio
import random

#Establece 0 intentos de inicio y el maximo de intentos posible
intentos=0
maximos_intentos=7

#Pregunta y establece el nombre de jugador
print("Cual es tu nombre?")
nombre=raw_input()

#Genera el numero aleatorio
numero=random.randint(1, 50)

#Para imprimir las variables numericas se convierten antes en string (aqui y al final del juego
print('Empecemos '+nombre+', estoy pensando un numero del 1 al 50, tienes '+str(maximos_intentos)+' intentos para adivinarlo')

#Juego en si
#Dura hasta que se alcancen los maximos intentos
while intentos<maximos_intentos:
    print('Adivina')
    estimacion=int(raw_input())  #Convierte el input en numero entero
    intentos=intentos+1          #Suma un intento tras cada estimacion

    if estimacion<numero:
    	print('Mi numero es mas grande')
    if estimacion>numero:
    	print('Mi numero es mas pequeno')
    if estimacion==numero:
        #Al acertar termina el "while"
    	break

#Final del juego
if estimacion==numero:
    print('Bien hecho '+nombre+' lo adivinaste en '+str(intentos)+' intentos!')
if estimacion!=numero:
    print('No lo adivinaste, mi numero era '+str(numero))
