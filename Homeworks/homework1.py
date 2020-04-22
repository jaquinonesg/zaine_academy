
""" data1 = open('lista1.txt')
content = data1.read()
data1.close() """

var = []
with open("lista1.txt", "a+") as data1:
    lines = data1.readlines()
    lines.pop(0)
    for line in lines:
      line_type = line.split(',')
      var.append(
        str(line_type(0)), 
        #float(line_type[1]), 
        #complex(line_type[2]), 
        #list(line_type[4]), 
        #tuple(line_type[4]), 
        #dict(line_type[5])
      )
print(var)













    #content = data1.write("DataTypes\n")
    #data1.seek(0)
    #data1.write("This is a string: ")
    #content = data1.read()

    #print(lines)    


#for line in data_types.readlines():
 #   for a in line:
  #      print(a)
    #print(line, type(line))   



