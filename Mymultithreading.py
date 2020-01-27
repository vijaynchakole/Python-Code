import threading

print("Demonstration of Multithreading")

def fun(number):
    for i in range(number):
        print(i)


def gun(number):
    for i in range(number):
        print(i)

if __name__ == "__main__":

    number = 5
    number2 = 10
    thread1 = threading.Thread(target=fun,args=(number,))
    thread2 = threading.Thread(target=gun,args=(number2,))

    #will both execute in parallel
    thread1.start()
    thread2.start()

    # joins threads back to the parent process,which is this program
    # otherwise parent process gone and its threads are running

    thread1.join()
    thread2.join()