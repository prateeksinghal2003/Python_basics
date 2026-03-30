#----------------Python Basics
#interpreted language
#Case sensitive

print("Hello world")
print("all good")

#to print on same line
print("Hello world","all good")


#another way to print on same line , using end parameter of print function
print("Hello world",end=" ")
print("all good")



print(23)
print(23+56)

# converts the number 23 (integer) into a string "23"
print(str(23))

#creating variables
name='Alice'
name2="Alex"

#can also use tripe double quotes
name3='''Bob'''
print(name,name2,name3)

age =23

print("My name is "+name+" or "+name2+" and age is "+str(age))
print("My name is "+name+" or "+name2+" and age is ",age)

print(type(age))

b=False
#cannot write F small

a=None
print(type(a))


#---------------Print sum of two numbers
op1=12
op2=13
sum=op1+op2
print(sum)

#-----------------------Comments

#---Single line comment
# for multi line comments use triple double quotes  or use contrl + forward slash
""""multi
line 
comment"""


#------Arithmetic Operators
# +,-,*,/,%
# / always gives floating point value
# a**b = a^b

#------------------Relational Operators
# !=,==,>=,<=,>,<

#-----------------Assignment Opeartors
# =,+=,-=,*=,/=,%=,**=

#---------------Logical Opeartors
#not, and ,or

print(not True)

print(op2>op1 and op2>=op1)

print(op2>op1 or op1>=op2)


#----------------Type conversion(Implicit Conversion)
op3=13.3
print(op1+op3)
#int is converted to float , more accurate

#-------------Type casting (Explicit Conversion )
op4="25"

print(op1+int(op4))
print(op1+int(op3))

print("Street "+str(17))

#-----------------Taking input from user
#input("enter your name")
#input() return user input in string

#int(input()) ---return int

# op5=input("enter key")
# print(type(op5))
#
# op6=int(input("enter key"))
# print(type(op6))


#-----------------------Programs
# s1=int(input())
# s2=int(input())
# print(s1+s2)


#-------Formatted String
# The f stands for “formatted string” (called an f-string).
#
# It tells Python:
#
# “This string contains variables inside it — replace them with their values.”
#
# 🧩 Without f (Normal String)
#
# If you wrote:
#
# print("{user_id} joined group {group_id}")
#
#
# Python would print exactly this:
#
# {user_id} joined group {group_id}
#
#
# It would NOT replace anything.
#
# ✅ With f
# user_id = "Alice"
# group_id = "Group1"
#
# print(f"{user_id} joined group {group_id}")
#
#
# Output:
#
# Alice joined group Group1


#--+--> would merge them
print([1,2,3]+[4,5,6])