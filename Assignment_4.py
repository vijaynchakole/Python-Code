
# Normal Function
def Add(no1,no2):
    return (no1 + no2)


#iret = Add(10,30)

#print(iret)
#
#
# # lambda Function
#
#
# fptr = lambda no1,no2:no1+no2
#
# iret = fptr(23,20)
#
# print(iret)
# print(fptr(45,20))


# Write a program which contains one lambda function which accepts one parameter and return  power of two.
#
#
# powerOfTwo = lambda num : num * num
#
# ans = powerOfTwo(int(input("enter number ")))
#
# # print(ans)
#
#
#
#
# multiplication = lambda no1,no2 : no1 * no2
#
# ans = multiplication(int(input("enter first number  ")), int(input("enter second number  ")))
#
# print(ans)




# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10.
# Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80] Output of reduce = 6538752000

from functools import reduce
arr = list()

num = int(input("enter number "))

for i in range(num):
    arr.append(int(input("num  ")))



#def Range(tempArr):

    # brr = list()
    #
    # if  tempArr >= 70 and tempArr<= 90 :

       # brr.append(tempArr)

    # for i in range(len(tempArr)):
    #
    #     if tempArr[i] >= 70 and tempArr[i] <= 90:
    #        # print(tempArr[i])
    #         brr.append(int(tempArr[i]))

   # return brr


# Range = list(filter(lambda no : no>=70 and no<=90,arr))
#
# print(Range)
#
# ModArray = list(map(lambda no: no + 10,Range))
#
# print(ModArray)
#
# from functools import reduce
# Final = reduce(lambda no1,no2: no1 * no2,ModArray)
#
# print(Final)

#
# even = list(filter(lambda no : no%2 == 0,arr))
#
# print(even)
#
# square = list(map(lambda no : no * no,even))
#
# print(square)
#
# addition = reduce(lambda no1,no2: no1 + no2,square)
#
# # print(addition)
#
#
# def ChkPrime(arr):
#
#     brrPrime = list()
#
#     bit = 0
#
#     for i in range(len(arr)):
#         bit = 0
#
#         for j in range(2,int((arr[i]/2)+1),1):
#
#             if (arr[i]%j) == 0:
#                 bit = 1
#                 break
#
#         if bit == 0 :
#            brrPrime.append(int(arr[i]))
#
#     #print(brrPrime)
#     return brrPrime




#Prime = ChkPrime(arr)

#print(Prime)


def PrimeNum(no):
    bit = 0
    for i in range(2,int(no/2),1):
        if (no%i) == 0 :
            bit = 1
            break



    if bit == 0 :
        return no



def multiply(no):
    return (no * 2)



def Maximum(no1,no2):
    max = 0

    if no1>no2 :
        max = no1
    else:
        max = no2

    return max


number = list(filter(PrimeNum,arr))

print(number)

multi = list(map(multiply,number))

print(multi)

maxvalue = reduce( Maximum,multi)

print(maxvalue)
