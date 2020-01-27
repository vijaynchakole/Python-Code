class BookStore:

    NoBooks = 0

    def __init__(self, bookName, authorName):

        self.Book = bookName
        self.Author = authorName

        BookStore.NoBooks += 1

    def Display(self):

        print("Book Name :: ", self.Book)

        print("Author Name :: ", self.Author)

        print("Number of Books :: ", BookStore.NoBooks)





class BankAccount:

    ROI = 10.5

    def __init__(self, custName, Amt):

        self.Name = custName
        self.Amount = Amt
        self.period = 1



    def Display(self):
        print("Customer Name :: ", self.Name)
        print("Total Amount :: ", self.Amount)



    def Deposit(self,Amt):
        self.Amount = self.Amount + Amt


    def Withdraw(self,Amt):
        self.Amount = self.Amount - Amt


    def CalculateInterest(self):

        return (( self.Amount * self.period * BankAccount.ROI) / 100)





class Number:

    def __init__(self,no):
        self.Num = no
        self.bit = 0
        self.sum = 0

    def ChkPrime(self):

        for i in range(2,int((self.Num/2)+1)):
            if self.Num % i == 0:
                #print(i)
                self.bit = 1
                break

        if self.bit == 0:

            return True
        else:
            return False


    def ChkPerfect(self):

        for i in range(1,int((self.Num/2)+1)):

            if self.Num % i == 0 :
                self.sum = self.sum + i


        if self.sum == self.Num :
            return True
        else:
            return False


    def SumFactors(self):
        self.sum = self.Num
       #  for i in range(1,int((self.Num/2)+1)):
       #
       #      if self.Num % i == 0 :
       #          print(i, end=" ")
       #          self.sum = self.sum + i

        self.ChkPerfect()
        return self.sum




def main():

    print("inside main ")

   # Obj1 = BookStore("Linux System Programming","Robert Love")
   # Obj1.Display()

   # Obj2 = BookStore("C Programming","Dennis Ritchie")
   # Obj2.Display()


    # Obj3 = BankAccount("Vijay Narsing Chakole", 1000)
    #
    # Obj3.Display()
    # Obj3.Deposit(44000)
    # Obj3.Display()
    # Obj3.Withdraw(20000)
    # Obj3.Display()
    # print("simple interest :: ", Obj3.CalculateInterest())


    # check prime number
#     num = 280
#     bit = 0
#     for i in range(2,int((num/2)+1)):
#         #print(i,end=" ")
#         if num % i == 0:
#             bit = 1
#             break
#
#     if bit == 0 :
#         print("number is Prime")
#     else:
#         print("NOT Prime")
#
# #################################################
#
#     # check perfect number
#     sum = 0
#     for i in range(1,int(((num/2)+1))):
#
#         if num % i == 0 :
#             sum = sum + i
#
#
#     if sum == num :
#         print("number is Perfect")
#     else:
#         print("NOT Perfect")


    no = 133
    Obj4 = Number(no)

    if Obj4.ChkPrime() == True :
        print("Number is Prime :: ", no)
    else:
        print("Number is NOT Prime :: ", no)


    if Obj4.ChkPerfect() == True :
        print("Number is Perfect :: ", no)
    else:
        print("NOT Perfect Number ", no)


    print("Summation of all Factors is :: ", Obj4.SumFactors())


if __name__ == "__main__":
    main()