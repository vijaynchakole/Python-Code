#
# class Demo :
#     def __init__(self,value1,value2):
#         print("inside init ",end=" ")
#         self.i = value1
#         self.j = value2
#
#     def fun(self):
#         print("inside fun ",end=" ")
#         print(self.i,self.j)
#
#     def Add(self):
#         print(self.i + self.j)



# class Demo:
#
# # class characteristics
#     x = 10
#     def __init__(self, no1, no2):
#         self.i = no1
#         self.j = no2


class Demo:
    def __init__(self):
        self.i = 0
        self.j = 0

    def fun(self):
        print("inside instance method ")

    @classmethod
    def gun(cls):
        print("inside class method ")

    @staticmethod
    def sun():
        print("inside static method ")




def main():
    print("inside main ")

    #
    # #creating object of Demo class
    #
    # obj1 = Demo(10, 20)
    #
    # print("object 1", obj1.i)
    # print("object 1", obj1.j)
    # print("object 1", obj1.x)
    #
    #
    # #creating another object of Demo class
    #
    # obj2 = Demo(50,60)
    #
    # print("object 2", obj2.i)
    # print("object 2", obj2.j)
    # print("object 2", obj2.x)
    #
    # print("class variable ", Demo.x)
    #calling method fun

   # obj2.fun()

    #call method Add to perform addition of characterstics

   # obj1.Add()
   # obj2.Add()

    #
    # obj1 = Demo()   # creating object of demo class
    # obj1.fun()      # calling instance method by using object of that class
    # Demo.fun(obj1)  # if we want to access instance method by using class name then
    #                 # we have to pass object name as first parameter wich is cllected in self in that method
    # Demo.gun()      # we have to access  class method by using class name
    # obj1.gun()      # we can also access class method by using object of that class
    #
    # Demo.sun()      # we have to access static method by using class name
    # obj1.sun()      # we can also access static method by using object of that class




    # either you can provide parameterise init method or default init method
    # but you can't give both method , there is only one init method for every single class
    obj2 = Demo(10, 20)

    print(obj2.i)
    print(obj2.j)

    obj1 = Demo()  # TypeError: __init__() missing 2 required positional arguments: 'no1' and 'no2'

    obj1.fun()    # TypeError: __init__() missing 2 required positional arguments: 'no1' and 'no2'




if __name__ == '__main__':

    main()


