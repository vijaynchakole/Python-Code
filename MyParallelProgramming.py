

#below program which uses serial processing approach

def square(n):
    return(n*n)

if __name__ == "__main__":
    #input list
    arr = [1,2,3,4,5]

    #empty list to store result
    result = []

    for num in arr :
        result.append(square(num))

    print(result)


###########################################################################################################################
#program  which uses Pooling for Parallel Programming

import multiprocessing
import os

def square(n):
    print("Worker process id for {0}:{1}".format(n,os.getpid()))
    return(n*n)


if __name__ == "__main__":
    #input list

    arr = [1,2,3,4,5]
    # creating pooling object
    p = multiprocessing.Pool()

    #map this list to target function
    result = p.map(square,arr)

    print("Square of each elements:")
    print(result)