# # Arithmetic Operations in PY
#
# print(8/3)
# print(8%3)
# print(8//3)
# print(8*3)
# print(8**3)
# print(8+3)
# print(8-3)
#
# # Comparison Operators in PY < , >, >=,<=,!,==
# print(4>3)
# print(4<3)
# print(4>=3)
# print(4<=3)
# print(4==3)
# print(4!=3)
#
# # Logical Operators in PY --> | , & , ^ , !
# print((1>3)|(1<3))
# print((1>3)&(1<3))
# print((2>3)^(2<3))
# print(not((3>3) & (3<3)))
#
# # Assignment Operators in PY
# a=3
# a+=1
# print(a)
# a-=1
# print(a)
# a*=2
# print(a)
# a//=2
# print(a)
# a%=2
# print(a)
# a**=2
# print(a)
#
# # Indentity Operators in PY ---> is or is not
# a=1234
# b="1234"
# print(type(a) is type(b))
# print(a is b)
# print( a is not b)
# b=1234
# print(type(a) is type(b))
#
# print(a is b)
# print(a is not b)
#
# #  Bitwise Operators --->  | , & , ^ , << , >>
# print(bin(10))
# print(hex(10))
# print(oct(10))
# print(bin(18))
# print(hex(18))
# print(oct(18))
#
# x=4
# y=5
#
# print(x&y)
# print(x^y)
# print(x|y)
#
# print(x>>2)
# print(x<<3)
#
#
# #  Membership Operator  ----> In , In not
#
#
# s="Mukul Kumar Sharma"
# print("s" in s)
# print("S" in s)
# print("Muk" in s)
#
# print('X' not in s)
#
# #  Conditional Operators  --> If, elif,else
#
# heightt=float(input("Enter your height: "))
#
# if heightt>1.8:     # Nested Loop
#     if heightt>2.0:
#         print("You are Selected")
#     else:
#         print("You are Eligible")
# elif heightt>1.7: # ELIF
#     print("Do hard work")
# else : # ELSE
#     print("You are Not Eligible")
#
#
# marks=float(input("Enter your marks: "))
#
# print("You passed the EXAM") if marks>=36 else print("You failed in the EXAM")
#
#
# # Loops For, While , do- while,
# count=0
# for i in range(1,11): count+=1
# print(count)
# while count<=100 :
#     count+=1
#     print(count)
#
# print(count)
while True :
    cnt=int(input("Enter number: "))

    for i in range(1,11):
        print(cnt,"X",i,"=",i*cnt)
    stop=int(input("Enter 1 to continue or 0 to stop: \n"))
    if stop==0 : break
    else : continue
