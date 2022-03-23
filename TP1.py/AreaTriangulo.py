base=None
altura=None
while True:
    try:
        base=float(input('Escriba el tamaño de la base:'))
        break
    except:
        print('Deben ser números')

while True:
    try:
        altura=float(input('Escriba la altura:'))
        break
    except:
        print('Deben ser números')

area=base*altura/2

print('El area del triangulo es de',area)