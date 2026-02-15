# def greet(name):
#     print("Good Morning",name)
# name=input("Enter your name: ")
# greet(name)

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def square(a):
    return a**2
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

while(True):
    Op = int(input("Enter 1->+,2->-,3->*,4->/,5-> square , 6 -> Factorial of No.s or 0 to stop: \n"))
    if Op==0: break
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))

    if Op==1: print(add(a,b))
    elif Op==2: print(subtract(a,b))
    elif Op==3: print(multiply(a,b))
    elif Op==4: print(divide(a,b))
    elif Op==5:
        print(square(a))
        print(square(b))
    elif Op==6:
        print("a! =",fact(a))
        print("b! =",fact(b))

    else: print("Invalid Input");
# **   👉 *args collects values into a tuple.
# ** 👉 **kwargs collects into dictionary.