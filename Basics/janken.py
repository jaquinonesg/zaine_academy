import random
def janken():
    number = random.randint(0,3)
    number = 2
    inputnumber = int(input("por favor ingresa 0 para piedra, 1 para papel, 2 para tijera :"))
    while number == inputnumber:
        print("empate, vuelve a intentar") 
        number = random.randint(0,3)
        inputnumber = int(input("por favor ingresa 0 para piedra, 1 para papel, 2 para tijera :"))
    if number == 0 and inputnumber ==1:
        print("Victoria del jugador")
        
    elif number == 0 and inputnumber ==2:
        print("Victoria de la maquina")
       
    elif number == 1 and inputnumber == 0:
        print("victoria de la Maquina")
        
    elif number == 1 and inputnumber == 2:
        print("Victoria del jugador")
        
    elif number == 2 and inputnumber == 0:
        print("Victoria del jugador")
        
    elif number ==2 and inputnumber == 1:
        print("victoria de la Maquina")

    else:
         print("de que me hablas viejo ?, vuelve a leer las instrucciones")        
            

if __name__ == '__main__':
    janken()