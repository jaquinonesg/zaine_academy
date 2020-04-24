import random

def aleatory(): 
    number = random.randint(0,10)
    inputnumber = int(input("por favor ingresa el numero aleatorio que crees que salio :"))
    print(number)            
    count=0
    while number != inputnumber:
        count = count+ 1
        print("nop, ese no es el numero sigue intentando") 
        inputnumber = int(input("por favor ingresa el numero aleatorio que crees que salio :"))
        
        if number == inputnumber:
            print("muy bien ese era el numero : " +str(number) )
        
        elif count ==2:
            print("game over")
            break
              
        
      

if __name__ == '__main__':
    aleatory()