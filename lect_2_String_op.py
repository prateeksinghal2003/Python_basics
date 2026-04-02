#------------------------Strings

#--Strings are immutable in python
#--can access a character at an index but cannot change it

#escape sequence characters
# \n for next line
# \t for tab space

print("This is my code \nThis is my code")

#---------------concat
print("Hello"+"World")

#finding length of string
print(len("Hello"))

#--------------indexing
word="World"
print(word[3])

# cannot do like this
# word[3]='L'
# print(word)

#---------------Slicing
#string or string_variable_name[start_index:end_index] , end index not included

print("Prateek"[0:2])

name ="karan"
print("Slicing using variable name :",name[0:2])

#go till last
print("Prateek"[2:])

#start from 0
print("Prateek"[:2])

#-----Negative index
print("Prateek"[-4:-1])


#-----------------String functions
#See PDF

print("Prateek".replace("e","i"))
print("Prateek".find("e"))
print("Prateek".count("e"))
print("prateek".capitalize())


#----------Conditional Statements
age=18

if age>=18:
    print("Adult")
elif age>12 and age<18 :
    print("Teen")

else:
    print("Child")