

#fd1 = open("world.txt") # equivalent to'r' and 'rt'

#print(fd1)
#fd2 =open("world.txt",'w') #write in a text mode
#print(fd2)

#fd3 = open("world.txt",'r+b')  # read  and write in binary mode
#print(fd3)

# Read  data from file

fd = open("world.txt", mode='r',encoding='cp1252')

output = fd.read(10) # read first 10 bytes
print(output)

output1 = fd.read() # read in the rest till end of file
print(output1)

# change current file cursor location using seek()

print("Current file  position is ",fd.tell())

so = fd.seek(0)
print(so)

# print content of whole file

print(fd.read())

# writing data into file

fd1 = open("world.txt",'a',encoding='cp1252')

wo = fd1.write("Python Programming\n")

