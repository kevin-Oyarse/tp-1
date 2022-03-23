#Que se le pida al usuario el nombre, la edad, el dinero que hay en su billetera y el hambre que
#tiene (medido de 0 a 10). Luego que muestre el mensaje:
#Si es menor de 35: Hola - nombre -. Eres una persona joven ya que tu edad es-edad.
#Si es mayor a 34 y tiene más de $500 y su hambre es mayor a 5: Hola - nombre -apellido- ¿Hoy hay asado?
#Si su hambre es de al menos 7 o tiene menos de $100 y su edad es menor a 18: Hola -nombre – apellido - ¿Vas a comer a lo de tus padres?

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