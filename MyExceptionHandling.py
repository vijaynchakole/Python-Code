

class AgeInvalid(Exception):
    def __init__(self,value):
        self.value = value

def main():
    print("inside main")
    # print("Demonstration of Exception Handling")
    #
    # no1 = int(input("enter first number "))
    # no2 = int(input("enter second number "))
    #
    # try:
    #     ans = no1 / no2
    #     print("Division is ",ans)
    # except ZeroDivisionError:
    #     print("Unable to divide by zero")
    # finally:
    #     print("Inside finally block to release all resources")
    #
    # print("end of exception Handling Application")
    #
    print("User defined exception")

    try:
        age = int(input("enter your Age "))
        if age<18 :
            raise (AgeInvalid("Age is invalid"))
        else:
            print("your Age is valid")
    except AgeInvalid as error:
        print("A New exception occured : ",error.value)




if __name__ == "__main__":
    main() ;