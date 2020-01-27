
from array import *
print("outside main")
def main():
    #print("inside main")

    arr = array('i',[10,20,30,40,50])

  #  print(arr[4])


if __name__ == "__main__" :
    main();


# for i in range(0,5,1):
#
#     print(" * ",end=" ")

i = int(input("enter number "))

def recursion_1():
    global i

    if i == 0 :
       return 1

    print(" * ", end=" ")
    i -= 1

    recursion_1()



#recursion_1()


def recursion_2():
    global i
   # print(i, end=" ")
    if i == 0 :

        return 1

    #print(i, end=" ")
    print(i , end=" ")
    i -= 1
    recursion_2()



recursion_2()

#num = 879
#sum = 0
# while(num!=0) :
#
#     bit = int((num%10))
#     sum = sum + bit
#
#     num = int(num / 10)


def recursion_3():
    global num
    global sum
    if num != 0 :
        bit = int((num % 10))
        sum = sum + bit
        num = int(num / 10)
        recursion_3()


#recursion_3()

num = 5
fact = 1
# while(num > 0):
#     fact = int(num * fact)
#     num -= 1



def recursion_4():
    global num
    global fact
    if num!=0 :


        fact = int(num * fact)
        num -= 1

#print(fact)
#recursion_4()
#print(fact)







print()
print(sum)









