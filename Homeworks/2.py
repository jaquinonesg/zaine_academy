num = int(input('Inserta un numero: '))
value = range(2, num)
count = 0

for n in value:

    if (num % n) == 0:
        count += 1
        print('Divisor: ', n)

if num < 2:
    print('El numero no es primo')
elif count > 0:
    print('El numero no es primo')
else:
    print('El numero es primo')

