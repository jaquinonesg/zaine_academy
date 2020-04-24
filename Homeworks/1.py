link = 'lista1.txt'
data = open(link, 'r')

for line in data.readlines():
    line = eval(line)
    print(line)
    print(type(line))

data.close()

#datastr = data.readline()
#datastr = str(datastr)
#print(datastr)
#print(type(datastr))
#
#dataint = data.readline()
#dataint = eval(dataint)
#print(dataint)
#print(type(dataint))
#
#datafloat = data.readline()
#datafloat = eval(datafloat)
#print(datafloat)
#print(type(datafloat))
#
#datacomplex = data.readline()
#datacomplex = eval(datacomplex)
#print(datacomplex)
#print(type(datacomplex))
#
#datalist = data.readline()
#datalist = eval(datalist)
#print(datalist)
#print(type(datalist))
#
#datatuple = data.readline()
#datatuple = eval(datatuple)
#print(datatuple)
#print(type(datatuple))
#
#datadict = data.readline()
#datadict = eval(datadict) 
#print(datadict)
#print(type(datadict))


