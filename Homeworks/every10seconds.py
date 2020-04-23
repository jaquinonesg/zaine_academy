import datetime
source = open("output.txt", "a")
time = datetime.datetime.now()
source.write(str(time) + "\n")
source.close()