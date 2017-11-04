#Este juego es para Python 2.X
#Para Python 3.X hay que cambiar el "raw_input" por "input"
import random

intentos=0
maximos_intentos=7
numero_maximo=str(maximos_intentos)
final_intentos=str(intentos)

print("Cual es tu nombre?")
nombre=raw_input()

numero=random.randint(1, 50)
numero_final=str(numero)

print('Empecemos '+nombre+', estoy pensando un numero del 1 al 50, tienes '+numero_maximo+' intentos para adivinarlo')

while intentos<maximos_intentos:
    print('Adivina')
    estimacion=int(raw_input())
    intentos=intentos+1

    if estimacion<numero:
    	print('Mi numero es mas grande')
    if estimacion>numero:
    	print('Mi numero es mas pequeno')
    if estimacion==numero:
    	break

if estimacion==numero:
    print('Bien hecho '+nombre+' lo adivinaste en '+final_intentos+' intentos!')
if estimacion!=numero:
    print('No lo adivinaste, mi numero era '+numero_final)