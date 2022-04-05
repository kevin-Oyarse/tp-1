#Ejercicio 10
import random
vidas=0
minmun=1
maxnum=10
numero=random.randint(minmun,maxnum)
id=input('Hola jugador podrias decirme tu nombre:')
print(id,'Vamos a jugar un juego, tenes que adivinar el numero que pienso que es entre '+str(minmun),'y' ,str(maxnum))

while vidas!=5:
    print('Dime tu numero')
    intentos=input()
    intentos=int(intentos)
    vidas=vidas+1
    if intentos<numero:
        print('casi,tu numero es bajo')
    if intentos>numero:
        print('uff,tu numero es alto')
    if intentos==numero:
        break

if intentos==numero:
    vidas=str(vidas)
    print (id,'adivinaste el numero en el intento '+ vidas)
if intentos !=numero:
    print('bueno,'+id+' perdiste,el numero que estaba pensando era '+str(numero))