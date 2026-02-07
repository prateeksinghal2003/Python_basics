

#--------------del keyword
#it delete properties or entire object

#
# class Student:
#
#
#     def __init__(self,name,age):
#        print("Printing name")
#        self.name=name
#        self.age=age
#
# s1=Student("Karan",17)
# print(s1.name)
# print(s1.age)
#
# del s1.age
# print(s1.name)
# #will get error
# #print(s1.age)


#--------------Private members
#
# class Student:
#
#
#     def __init__(self,name,age):
#        print("Printing name")
#        self.name=name
#
#        #made age variable private using __variable_name/method_name, cannot access outside the class
#        self.__age=age
#
# s1=Student("Karan",17)
# print(s1.name)

#will give error
#print(s1.__age)


#----------Inheritance
#
# class Car:
#
#      @staticmethod
#      def start():
#          print("Car is starting")
#
#      @staticmethod
#      def stop():
#          print("Car is stopped")
#
#
# class SuzukiCar(Car):
#       def __init__(self,name):
#           self.name=name
#
# car1=SuzukiCar("car1")
# car2=SuzukiCar("car2")
#
# print(car1.name)
# car1.start()
#
#


#----Multiple Inheritance

# class A:
#     varA="This is class A"
#
# class B:
#     varB="This is class B"
#
# class C(A,B):
#     varC="This is C"
#
# c=C()
# print(c.varA)
# print(c.varB)
# print(c.varC)


#-----------Super method
#use to access methods of parent class

# class Car:
#
#
#      def start(self):
#          print("Car is starting")
#
#
#      def stop(self):
#          print("Car is stopped")
#
#
# class SuzukiCar(Car):
#       def __init__(self,name):
#           self.name=name
#
#       def start(self):
#
#           #--super() is called to invoke parent method
#           super().start()
#           print("Suzuki car is starting")
#
# car1=SuzukiCar("car1")
# car2=SuzukiCar("car2")
#
# print(car1.name)
#
# car1.start()


#--------Class methods

# class Person:
#     name="Random"
#
#     # def __init__(self):
#     # accessing class attributes
#     # self.__class__.name="Rahul"
#
#another way is creating  a class method by decorator
#
#     @classmethod
#     def change_name(cls,name):
#         cls.name=name
#
#
# p1=Person()
# # print(p1.name)
# # print(Person.name)
#
# p1.change_name("John")
# print(p1.name)


#-------property decorator

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#
#         self.per=(self.phy+self.chem+self.math)/3
#
# s1=Student(60,70,80)
# print(s1.per)
#
# #--If i change physics marks
# s1.phy=50
# print(s1.phy)
#
# #--now cal percentage, it would be same , as self.per is already set
# print(s1.per)

#---to do this create  a function

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#
#     def cal_per(self):
#         self.per=(self.phy+self.chem+self.math)/3
#
#
# s1=Student(60,70,80)
# s1.cal_per()
# print(s1.per)

#--If i change physics marks
# s1.phy=50
# print(s1.phy)

#--now cal percentage, it would change accordingly
# s1.cal_per()
# print(s1.per)

#-----------------Polymorphism
#operator overloading --->like + would have different meaning


class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def show(self):
        print(self.real,"i +",self.imag,"j")

    # def add(self,num2):
    #    return Complex(self.real+num2.real,self.imag+num2.imag)

    def __add__(self,num2):
        return Complex(self.real+num2.real,self.imag+num2.imag)

num1=Complex(10,20)
num1.show()


num2=Complex(1,2)
num2.show()

# num3=num1.add(num2)
# num3.show()

#----but I want num3=num1+num2
#--- + is not defined for adding complex numbers
#---create  a dunder function for + it is __add__
#---implement add in your ways  and + would act in that way

#Dunder Functions :
# +>---__add__
# ->---__sub__
# *>---__mul__
# />---__truediv__
# %>---__mod__



num3=num1+num2
num3.show()



