from sys import *
import os

# set current working to "C:/Users/hp/PycharmProjects" and then it will find given folder name in this directory
#if given folder is exists then it will show all file names otherwise throws exception
#very important line
# you must given folder name which are already exists in below mentioned directory path

# set current working directory
os.chdir("C:/Users/hp/PycharmProjects")



def DirectoryWatcher(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filename in os.walk(path):
            print("Current folder is ", foldername )
            for subfold in subfolder :
                print("sub Folder of " + foldername +" is "+ subfold)
            for file_name in filename:
                print("File inside "+foldername+" is "+file_name)
            print('')
    else:
        print("Not Found ")



def main():
    print("inside main")
    #path = "college"
    path = argv[1]

    DirectoryWatcher(path)


if __name__ == "__main__":
    main()