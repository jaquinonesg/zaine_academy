

def prime (number):
    if number <1:
        return False
    elif number ==2:
        return True
    else:
        for i in range(2,number):
            if number %i == 0:
                return False
            return True

def numberIntput():
    number = int(input('escribe  un numero por favor  prro:  '))
    result = prime(number)
    if result is True: 
        print('este numero es primo perro')
    else:
        print('de que me hablas viejo, esto no es primo: ')

if __name__ == '__main__':
    numberIntput()
 




