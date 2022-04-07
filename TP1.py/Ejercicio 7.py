#Ejercicio 7

from errno import EADDRNOTAVAIL
nombre=(input('Hola, podrias decirme tu nombre:\n'))
apellido=(input('Hola,'+' '+nombre+' '+ 'podrias decirme tu apellido:\n'))
edad=float(input('podrias decirme tu edad:\n'))
dinero=float(input('Cuanto dinero tenes en la billetera?\n'))
hambre=float(input("del 0 al 10 cuanta hambre tenes?\n"))
if edad<35:
    print('hola '+ nombre+','+'eres una peronsa muy joven tu edad es de '+str(edad))
elif edad>34 and dinero>500 and hambre>5:
    print('hola '+nombre+' '+apellido+' ¿hoy hay asado?')
elif hambre>=7 or dinero<100 and edad<18:
    print ('Hola '+nombre+' '+apellido+' ¿Vas a comer con tus padres?.')
else:
    print("Quedate en tu casa mejor")