

def FahToCel(F):

    C = (F - 32 ) * (5/9)

    return C




import numpy as np
print(np.__version__)


def main():
    print("inside main")


    num = int(input("enter Temperature in Fah  "))

    print( FahToCel(num))



if __name__ == "__main__":
    main()
