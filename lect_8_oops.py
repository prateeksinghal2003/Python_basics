#------------------oops

# class Student:
#     name="karan"
#
# s1=Student()
# print(s1.name)


#---Creating Constructors

# class Student:




#---self represents the object itself,always the first argument,compulsory to pass, self is just a name,
#---can be anything
# __init__ → runs automatically on object creation
# A constructor that initializes object properties when an object is created.

# self : refers to the current object
# Used to store and access object data

#     def __init__(self,name):
#        print("Printing name")
#        self.name=name
#
# s1=Student("Karan")
# print(s1.name)
#
# s2=Student("Narine")
# print(s2.name)


#--------------Attributes
#-----Class attributes

# class Student:
#
#   #---class attributes, shared among every object
#     college_name="XYZ"
#
#     def __init__(self,name):
#        print("Printing name")
#        self.name=name
#
# s1=Student("Karan")
# print(s1.name)
# print(s1.college_name)
#
# s2=Student("Narine")
# print(s2.name)
# print(s2.college_name)
#
# #---can also write
# print(Student.college_name)


#----Functions inside class are called methods
# class Student:
#     def __init__(self,name,age):
#        print("Printing name")
#        self.name=name
#        self.age=age
#
#      #--self must be passed in instance methods to refer to the current object.
#     def hello(self):
#         print("Hello",self.name)
#
# s1=Student("Karan",23)
# print(s1.name,s1.age)
# s1.hello()


#---Static Methods--work at class level
#
# class Student:
#     def __init__(self,name):
#        print("Printing name")
#        self.name=name
#
#      # @staticmethod makes the method static , which is a decorator
#      # ---decorator is  a function that takes function as input and return function as output
#      # ---@staticmethod takes any function as input and makes it static
#     @staticmethod
#     def hello():
#         print("Hello")
#
# s1=Student("Karan")
# print(s1.name)
# s1.hello()
# Student.hello()


#------------------OOPS CONCEPTS-------
#-----------Abstraction


class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self ):
        self.acc=True
        self.clutch=True
        print("Car Started")

c1= Car()
#---simply called start method, hiding implementation details
c1.start()

#--------Encapsulation



