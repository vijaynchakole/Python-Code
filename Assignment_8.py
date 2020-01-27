
import threading

def even(num):
   while num > 0:
       if num%2 == 0 :
           print(f"even number : {num}")
       num -= 1

#####################################################################
def odd(num):
    while num > 0:
        if not num%2 == 0 :
            print(f"odd number : {num}")
        num -= 1

#####################################################################

def EvenFactor(integer):
    even = 2
    sum = 0
    while even < (int(integer/2)+1) :
        if integer % even == 0 :
            print(even)
            sum = sum + even
        even += 2
    print(f"Addition of EvenFactor is  : {sum}")


def OddFactor(integer):
    odd = 1
    sum = 0
    while odd < (int(integer/2)+1) :
        if  integer % odd == 0 :
            print(odd)
            sum = sum + odd
        odd += 2
    print(f"Addition of OddFactor is : {sum}")

#####################################################################

def EvenList(lst):
    sum = 0
    for i in lst :
        if i % 2 == 0 :
            #print(f"even number : {i}")
            sum = sum + i
    print(f"Even Elements Addition is : {sum}")

def OddList(lst):
    sum = 0
    for i in lst :
        if not i % 2 == 0 :
            sum = sum + i
    print(f"Odd elements Addition is : {sum}")

#####################################################################


def SmallLetter(str):
    #pass ;
    lower = 0
    for i in str:
        if i.islower():
            #print(i)
            lower += 1
            print(f"Total number of lower letters are  {lower}")


def CapitalLetter(str):
    #pass ;
    upper = 0
    for i in str:
        if i.isupper() :
            #print(i)
            upper += 1
            print(f"Total number of upper letters are  {upper}")



def Digit(str):
    #pass ;
    digit = 0
    for i in str :
        if i.isdigit():
            #print(i)
            digit += 1
            print(f"Total number of digits are  {digit}")
#####################################################################

def straigth(num):
    while num <=50 :
        print(num)
        num += 1

def reverse(num):
    temp = 50
    while not temp == (num -1 )  :
        print(temp)
        #num += 1 ;
        temp -= 1 ;



#####################################################################
if __name__ == "__main__":

    #question 5
    num = 1
    thread_1 = threading.Thread(target=straigth,args=(num,))
    thread_2 = threading.Thread(target=reverse,args=(num,))

    thread_1.start()
    thread_1.join()
    print("thread1 completed")

    thread_2.start()
    thread_2.join()
    print("thread2 completed")





    #question 4
    # str = "My Na3me Is Vi2jay5 Narsi15ng Ch7aKole"
    # #SmallLetter(str)
    # #CapitalLetter(str)
    # #Digit(str)
    #
    # T1 = threading.Thread(target=SmallLetter, args=(str,))
    # T2 = threading.Thread(target=CapitalLetter, args=(str,))
    # T3 = threading.Thread(target=Digit, args=(str,))
    #
    # T1.start()
    # T2.start()
    # T3.start()
    #
    # T1.join()
    # T2.join()
    # T3.join()
# question 3
#    list = [10,56,8,7,9,14,5,6,3,87,17]

    #EvenList(list)
    #OddList(list)

#    T1 = threading.Thread(target=EvenList, args=(list,))
#    T2 = threading.Thread(target=OddList, args=(list,))

#    T1.start()
#    T2.start()

#    T1.join()
#    T2.join()

#Question 2
#    integer = 500
#   T1 = threading.Thread(target=EvenFactor, args=(integer,))
#    T2 = threading.Thread(target=OddFactor, args=(integer,))
#
#    T1.start()
#    T2.start()

#    T1.join()
#    T2.join()

#    print("Exit from Main")

#####################################################################
#Question 1
#    num = 10
#    T1 = threading.Thread(target=even, args=(num,))
#    T2 = threading.Thread(target=odd, args=(num,))
#    starting the thread 1
#    T1.start()
#    starting the thread 2
#    T2.start()
#    wait until the first thread is completely executed
#    T1.join()
#    wait until the second thread is completely executed
#    T2.join()
#   both threads completely executed
#   print("Done")
#####################################################################

