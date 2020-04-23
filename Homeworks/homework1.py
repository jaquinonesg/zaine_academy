with open("lista1.txt", "a+") as data1:
    lines = data1.readlines()
    for line in lines:
      print(line, 'It is of type:  =>', type(eval(line)))
   
 



