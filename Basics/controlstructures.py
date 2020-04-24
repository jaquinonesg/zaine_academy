from io import open 

route = "lista1.txt"
file_ = open(route,'r')
lines = file_.readlines()
for line in lines:
    line = eval(line)
    print(type(line))

#list_ = [line.strip() for line in lines]
#print(type(str(list_[0])))
#print(type(int(list_[1])))
#print(type(float(list_[2])))
#print(type(complex(list_[3])))
#print(type(list(list_[4])))
#print(type(tuple(list_[5])))
#print(type(list_[6]))
#print(type(dict(list_[6])))




#list_ = [line.strip().split(' ') for line in data]
##comi = list_.replace('"', '')
#i=0
#for lista in list_:
#    lis=(lista[i].replace('"', '""'))
#    print(type(lis))
#i=i+1
#

#
#
#
##for info in data1:
# #   print(info, type(info)) 