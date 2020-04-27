import random

random1 = random.randrange(0, 3)
pcchoose = ""
print("Let's play rock paper scissors.")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
option = int(input("What do you choose?: "))

if option == 1:
    userchoose = "rock"
elif option == 2:
    userchoose = "paper"
elif option == 3:
    userchoose = "scissors"
print("You choose: ", userchoose)

if random1 == 0:
    pcchoose = "piedra"
elif random1 == 1:
    pcchoose = "paper"
elif random1 == 2:
    pcchoose = "scissors"
print("PC chose: ", pcchoose)
print("...")
if pcchoose == "rock" and userchoose == "paper":
    print("You win, paper defeat rock")
elif pcchoose == "papel" and userchoose == "scissors":
    print("You win, scissors defeat paper")
elif pcchoose == "scissors" and userchoose == "rock":
    print("You win, rock defeat scissors")
if pcchoose == "papel" and userchoose == "rock":
    print("You lose, paper defeat rock")
elif pcchoose == "scissors" and userchoose == "paper":
    print("You lose, scissors defeat paper")
elif pcchoose == "piedra" and userchoose == "scissors":
    print("You lose, rock defeat scissors")
elif pcchoose == userchoose:
    print("tie")