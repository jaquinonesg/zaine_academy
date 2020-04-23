import datetime
source = open("/Users/jaquinonesg/Projects/zaineacademy/output.txt", "a")
time = datetime.datetime.now()
source.write(str(time) + "\n")
source.close()