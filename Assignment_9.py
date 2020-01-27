
#from os import *
from sys import *

#from os import open
import os

# question 1
def fileSearchInCurrentDirectory(FName):

    workingDirectory = getcwd()
    # print(work)

    for folder, subFolder, file in walk(workingDirectory):
        #print("name of folder is ", folder)

        #for sf in subFolder:
           # print("name of Subfolder is ", sf)
        for fileName in file:

            if fileName == FName:
                #print("subfolder name is ", sf)
                print(argv[1], "is exist in current working directory")



# question 2

def FileReading(Fname):

  fd = os.open(Fname,"w")
  read(fd)





def main():
    print("inside main")

    #print("file name is ", argv[0])
    #print()
   # fileSearchInCurrentDirectory(argv[1])
    #FileReading(argv[1])

    mode = 0o666
    flags = os.O_RDWR | os.O_CREAT

    fd = os.open("world.txt", flags,  mode)
    content = os.read(fd,10)
    print(content)

    # Write a string to the file
    # using file descriptor
    str = "GeeksforGeeks: A computer science portal for geeks."
    os.write(fd, str.encode())
    print("String written to the file descriptor.")

    # Now read the file
    # from beginning
    os.lseek(fd, 0, 0)
    str = os.read(fd, os.path.getsize(fd))
    print("\nString read from the file descriptor:")
    print(str.decode())

    # Close the file descriptor
    os.close(fd)
    print("\nFile descriptor closed successfully.")



if __name__ == "__main__" :
    main();
