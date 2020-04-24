from random import randrange


random = randrange(1, 5)

if random == 1:
    random = 'tijera'
elif random == 2:
    random = 'papel'
elif random == 3:
    random = 'piedra'
elif random == 4:
    random = 'lagarto'
elif random == 5:
    random = 'spock'

print('REGLAS')
print('Tijera corta papel, papel cubre piedra, piedra aplasta lagarto, lagarto envenena Spock, Spock destruye tijera, tijera decapita lagarto, lagarto come papel, papel desautoriza Spock, spock vaporiza piedra, piedra aplasta tijera')
print('!Vamos a jugar¡')
options = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']
print(options)
game = ''

while game not in options:
    game = input('Elige una opción válida: ')
else:
    if game == random:
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡EMPATE!!!, intentalo de nuevo...')

    elif game == 'tijera' and random == 'papel':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, tijera corta papel.')
    elif game == 'tijera' and random == 'piedra':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, piedra aplsta tijera.')
    elif game == 'tijera' and random == 'lagarto':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, tijera decapita lagarto.')
    elif game == 'tijera' and random == 'spock':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, Spock rompe tijera.')

    elif game == 'papel' and random == 'piedra':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, papel envuelve piedra.')
    elif game == 'papel' and random == 'lagarto':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, lagarto devora papel.')
    elif game == 'papel' and random == 'spock':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, papel desautoriza Spock.')
    elif game == 'papel' and random == 'tijera':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, tijera corta papel.')

    elif game == 'piedra' and random == 'lagarto':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, piedra aplasta lagarto.')
    elif game == 'piedra' and random == 'spock':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, Spock vaporiza piedra.')
    elif game == 'piedra' and random == 'tijera':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, piedra aplasta tijera.')
    elif game == 'piedra' and random == 'papel':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, papel envuelve piedra.')

    elif game == 'lagarto' and random == 'spock':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, lagarto envenena Spock.')
    elif game == 'lagarto' and random == 'tijera':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, tijera decapita lagarto.')
    elif game == 'lagarto' and random == 'papel':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, lagarto devora papel.')
    elif game == 'lagarto' and random == 'piedra':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, piedra aplasta lagarto.')

    elif game == 'spock' and random == 'tijera':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, Spock rompe tijera.')
    elif game == 'spock' and random == 'papel':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, papel desautoriza Spock.')
    elif game == 'spock' and random == 'piedra':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Felicitaciones!!!, Spock vaporiza piedra.')
    elif game == 'spock' and random == 'lagarto':
        print('Tú:', game, 'VS', 'PC:', random)
        print('¡¡¡Buuuuu!!!, perdiste, lagarto envenena Spock.')
