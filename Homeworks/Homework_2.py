def primNum(num):
 if num > 0 and num <= 100:
    if num == 1:
          return ("It's not a prime number")
    elif num == 2:
          return ("It's a prime number")
    else: 
        for i in range(2, num):
          if num%i == 0:
            return ("It's not a prime number")
        return ("It's a prime number")
 else:
    return ("This number is out of bounds")
          

print(primNum(3))