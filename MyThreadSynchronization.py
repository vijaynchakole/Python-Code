import threading
amount = 0

def Counter(fun,lock):
    fun(lock)

def Credit(lock):
    value = int(input("enter amount to credit "))
    lock.acquire()
    global amount
    amount += value
    print("Balance is ",amount)
    lock.release()

def Debit(lock):
    value = int(input("enter amount to withdraw "))
    lock.acquire()

    global amount
    if value>amount :
        print("unable to withdraw")
    else:
        amount -= value
        print("amount withdraw is ",value)
        print("Balance is ",amount)

    lock.release()

def main():
    print("inside main")

    lock = threading.Lock()

    T1 = threading.Thread(target=Counter, args=(Credit,lock))
    T2 = threading.Thread(target=Counter,args=(Debit,lock))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("work done ")

if __name__ =="__main__":
    main();