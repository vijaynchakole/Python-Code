

# Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that List.

# arr = list()
# num = int(input("enter number"))
#
# for i in range(num):
#     no = int(input("num : "))
#     arr.append(int(no))
#
# print(arr)
#
# def Add(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#
#     return sum
#
# iret = Add(arr)
#
# print(iret)


# Write a program which accept N numbers from user and store it into List.
# Return Maximum number from that List.
#
#
# arr = list()
#
# num = int(input("enter number"))
#
# for i in range(num):
#     arr.append(int(input("num :  ")))
#
#
# print(arr)
#
# def Maximum(arr):
#     max = 0
#
#     for i in range(len(arr)):
#         if max < arr[i]:
#             max = arr[i]
#
#
#     return max
#
#
#
#
# maxvalue = Maximum(arr)
#
# print(maxvalue)


# Write a program which accept N numbers from user and store it into List.
# Return Minimum number from that List.
#
# arr = list()
#
# num = int(input("enter number"))
#
# for i in range(num):
#     arr.append(int(input("num")))
#
#
# print(arr)
#
#
#
# def Minimum(arr):
#     min = arr[0]
#     for i in range(len(arr)):
#         if arr[i]<min :
#             min = arr[i]
#
#     return min
#
#
#
# minvalue = Minimum(arr)
#
# print(minvalue)


# Write a program which accept N numbers from user and store it into List.
# Accept one another number from user and return frequency of that number from List.

#
# arr = list()
#
# num = int(input("enter number"))
#
# for i in range(num):
#     arr.append(int(input("num")))
#
#
# search = int(input("search number is "))
#
# cnt = 0
# for i in range(len(arr)):
#     if search == arr[i] :
#         cnt = cnt + 1
#
#
#
# print(search, " occurred at ", cnt , " times ")



arr = list()

num = int(input("enter number"))


for i in range(num):
    arr.append(int(input("num : ")))


print(arr)



def ChkPrime(arr):

    brrPrime = list()

    bit = 0

    for i in range(len(arr)):
        bit = 0

        for j in range(2,int((arr[i]/2)+1),1):

            if (arr[i]%j) == 0:
                bit = 1
                break

        if bit == 0 :
           brrPrime.append(int(arr[i]))


    print(brrPrime)

    return brrPrime


def Addition(Primelist):
    sum = 0
    for i in range(len(Primelist)):

        sum = sum + int(Primelist[i])

    return sum



summation = Addition(ChkPrime(arr))

print(" Addition of Prime number is ",summation)