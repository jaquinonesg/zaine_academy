from random import randrange


random = randrange(0, 10)
print('¡Adivina el número!')
num = int(input('Ingresa un número entre 0 y 10: '))
count = 3

while num != random:
    count -= 1
    if count == 0:
        print('Perdiste, el número era:', random)
        break
    else:
        if num > random:
            num = int(input('El número es menor, intentalo de nuevo: '))
        elif num < random:
            num = int(input('El número es mayor, intentalo de nuevo: '))
else:
    print('Felicitaciones, acertaste el número', random)

