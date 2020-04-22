x = int(input("Enter a number: "))
z = range(2, x)

for y in z:
    if (x % y) != 0 :
        continue     
    else:
        print("it's not a prime number")
    break
else:
    print("it's a prime number")    