
def sub(no1,no2):

     return(no1-no2)


def Decorators(OriginalFunction):
    def Updator(a,b):
        if(a<b):
            a,b = b,a
        return OriginalFunction(a,b)

    return Updator


newsub = Decorators(sub)

print("Substraction of 10 and 7 is ", newsub(10,7))

print("Substraction of 7 and 7 is ", newsub(7,10))


