#Ejercicio 9
numeros=None
signos=None
while True:
    try:
        numero1=float(input('Ingresa un numero:\n'))
        numero2=float(input('Ingresa otro numero:\n'))
        break
    except:
        print('Deben ser un números.')
        

while True:
    try:
        signos=input('signo: ')
        break
    except:
        print('Deben ser un signo.')

if signos=='-':
    resultado=numero1-numero2
    print(resultado)
if signos=='+':
    resultado=numero1+numero2
    print(resultado)
if signos=='*':
    resultado=numero1*numero2
    print(resultado)
if signos=='/':
    resultado=numero1/numero2
    print(resultado)
