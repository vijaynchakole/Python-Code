class Demo:

    Value = 10

    def __init__(self, value1, value2):
        self.no1 = value1
        self.no2 = value2

    def Fun(self):


        print("inside fun  ", self.no1, "  ", self.no2 )

    def Gun(self):

        print("inside gun  ", self.no1, "  ", self.no2)


class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, radi):
        self.Radius = radi

    def CalculateArea(self):
        self.Area = (Circle.PI) * (self.Radius * self.Radius)

    def CalculateCircumference(self):
        self.Circumference = 2 * (Circle.PI) * (self.Radius)

    def Display(self):
        print("Area of Circle is  ", self.Area)

        print("Circumference of Circle is ", self.Circumference)






class Arithmetic :

    def __init__(self):
        self.value1 = 0
        self.value2 = 0


    def Addition(self,num1,num2):

        self.value1 = num1
        self.value2 = num2
        return (self.value1 + self.value2)


    def Substrction(self,num1,num2):

        self.value1 = num1
        self.value2 = num2

        if self.value1 < self.value2:

            return (self.value2 - self.value1)
        else:
            return (self.value1 - self.value2)


    def Multiplication(self,num1,num2):

        self.value1 = num1
        self.value2 = num2

        return(self.value1 * self.value2)


    def Division(self,num1,num2):

        self.value1 = num1
        self.value2 = num2

        return(self.value1 / self.value2)







def main():
    print("inside main ")

    # Obj1 = Demo(11, 21)
    # Obj2 = Demo(51, 101)
    #
    # #calling instance method
    #
    # Obj1.Fun()
    # Obj2.Fun()
    #
    # print("function Gun ")
    #
    # Obj1.Gun()
    # Obj2.Gun()
    #
    # print("Class variable is ", Demo.Value)
    #



    # radius = float(input("enter radius "))
    #
    # Obj3 = Circle()
    #
    # Obj3.Accept(radius)
    #
    # Obj3.CalculateArea()
    #
    # Obj3.CalculateCircumference()
    #
    # Obj3.Display()



    Obj4 = Arithmetic()

    number1 = int(input("enter first number "))

    number2 = int(input("enter second number "))


    print("Addition of  is ", Obj4.Addition(number1, number2))

    print("Substraction is ", Obj4.Substrction(number1, number2))

    print("Multiplication is ", Obj4.Multiplication(number1, number2))

    print("Division is ", Obj4.Division(number1, number2))


if __name__ == "__main__" :
    main()





