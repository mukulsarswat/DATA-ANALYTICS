print("Hi")
print("This is the first program")
print("This is in course of Data Analytics")

print("""This how we can use to print multiple lines using triple "
This will print as it as we write """)

print("Here we'll learn to program using \nThis is the way to print multiple lines ")
print('We can use single quotation to print but its avoid while using the same in the lines that can lead to error')
 # This is the way to write comments using '#'.

# For the multi line Comment we can use triple quotation
# This is way of writing comments this isn't working..


#********* In this we'll learn the variables********************

a="Hello World"
print("\n"+a+"\n")


# *********** USER INPUTS************
name=input("What's your name by the way:")
age =int(input("What's your age :"))
print(name+" and Age:"+str(age))
height=float(input("What's your height ( in m) :"))
print("Height:"+str(height))
# print(age)
weight=float(input("What's your weight (in kg) :"))
print("Weight:"+str(weight))

BMI=weight/(height*height)
print(name+",Your BMI is :"+str(BMI))
if(BMI<18.0): print("You are underweight")
elif(BMI<24.0): print("Great ,You are normal")
elif(BMI<32.0): print("Shittt,You are overweight")
else: print("You are obese")

rate=eval(input("How much protein to take: "))
print(rate)