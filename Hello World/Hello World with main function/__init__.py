# Python program to demonstrate 
# main() function
import random

print("Hello")


def printAnyRandomNumber():
    print(random.randint(1,10000))


# Defining main function
def printMyName():
    print("I'm Mithun")


def main():
    print("hey there... I'm inside the main function")
    printMyName()
    printAnyRandomNumber()


# Using the special variable  
# __name__ 
if __name__ == "__main__":
    main()
