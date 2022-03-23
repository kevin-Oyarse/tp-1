n1=float(input ('ingrese su numero: '))
n2=float(input ('ingrese su numero: '))
n3=float(input ('ingrese su numero: '))

if n2<n1>n3:
    print('El numero mayor es :',n1)
elif n1<n2>n3:
    print ('el numero mayor es:',n2)
elif n1<n3>n2:
    print ('el numero mayor es:',n3)
else:
    print('los numeros que se ingreso son iguales')