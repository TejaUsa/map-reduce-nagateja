#Nagateja
fileIp = open("a.txt","r")  # open file, read-only
fileOp = open("sortedOp.txt", "w") # open file, write
lines = fileIp.readlines()
lines.sort()

for line in lines:
 fileOp.write(line)

fileIp.close()
fileOp.close()