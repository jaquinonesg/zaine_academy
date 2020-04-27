import random

def janken():
    number = random.randint(0,2)
    print (number)
    name = str(input("ingresa tu nombre de jugador: "))
    inputnumber = int(input("por favor ingresa 0 para piedra, 1 para papel, 2 para tijera: "))
    vyctory_bot = "Victoria de la maquina"
    vyctory_player = "Victoria del jugador "+name
    paper_win = " papel le gana a piedra"
    scissor_win = " tijera le gana a papel "
    rock_win = " piedra le gana a tijera"
    
    while number == inputnumber:        
        print("empate, vuelve a intentar")         
        number = random.randint(0,2)
        inputnumber = int(input("por favor ingresa 0 para piedra, 1 para papel, 2 para tijera: "))
    if number == 0 and inputnumber ==1:
        print(vyctory_player+paper_win)        
    elif number == 0 and inputnumber ==2:
        print(vyctory_bot+rock_win)       
    elif number == 1 and inputnumber ==0:
        print(vyctory_bot+paper_win)        
    elif number == 1 and inputnumber ==2:
        print(vyctory_player+scissor_win)        
    elif number == 2 and inputnumber ==0:
        print(vyctory_player+rock_win)        
    elif number ==2 and inputnumber ==1:
        print(vyctory_bot+scissor_win)
    else:
         print("de que me hablas viejo ?, vuelve a leer las instrucciones")        
            
if __name__ == '__main__':
    janken()