from threading import *
from multiprocessing import *
from time import *
from os import *

def square(no):
    print(getpid())
    return (no*no)

def main():
    print("inside main")
    arr = [1,31,41,3,5,4,2]
    brr = []

    starttime1 = time()
    for i in range(len(arr)):
        brr.append(square(arr[i]))
    endtime1 = time()
    print(brr)
    print("serial time : ",endtime1 - starttime1)

    pobj = Pool()

    starttime2 = time()
    crr =pobj.map(square,arr)
    endtime2 = time()
    print(crr)
    print("Parallel time : ", endtime2 - starttime2)
    print(getpid())







if __name__ == "__main__":
    main()