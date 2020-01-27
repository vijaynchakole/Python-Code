
import multiprocessing
import os

print("Demonstration of Multiprocessing")


def fun(number):
    print("parent process id of fun: ", os.getppid())
    print("process id of fun ", os.getpid())

    for i in range(number):
        print(i)



def gun(number):
    print("parent process id of gun: ", os.getppid())
    print("process id of gun ", os.getpid())

    for i in range(number):
        print(i)







if __name__ == "__main__":

    print("Total cores available : ", multiprocessing.cpu_count())

    print("Parent process id of main : ", os.getppid())
    print("process id of main : ", os.getpid())

    number = 3
    result = None

    p1 = multiprocessing.Process(target = fun, args=(number,))

    p2 = multiprocessing.Process(target=gun, args=(5,))

    p1.start()
    p2.start()


    p1.join()
    p2.join()


