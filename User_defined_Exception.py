
class AgeInvalid(Exception):
    def __init__(self, name_exception):
        self.value = name_exception



def main():
    num = int(input("enter your Age "))
    try:
        if num<18:
            raise(AgeInvalid("Invalid Age : under age"))
    except AgeInvalid as ex:
        print(ex.value)

if __name__ == "__main__":
    main()