#--------------------------List and Tuples
#List built in data structure , to store multiple values
#can access a particular element from a list , and can modify it

marks=[12,13,14,15,18.2,"karan"]
print(marks)
print(marks[2])
print(len(marks))

marks[2]=20
print(marks)


#-------------------Slicing
print(marks[0:2])

#--------List methods
marks.append("sanjay")
print(marks)

fruits=["mango","banana","pear","12"]
fruits.sort()
#sorted using unicode values
print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

fruits.reverse()
print(fruits)

fruits.insert(2,"kiwi")
print(fruits)

fruits.append("kiwi")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.pop(2)
print(fruits)

#----------------------------Tuples
# built in data type  creates immutable values

tup=(12,13,14,12,12)
print(tup)
print(type(tup))
print(tup[0])

#----tup[0]=3 not allowed

#can create an empty tuple
#--tup=()

#--for single element
tup2=(1,)
print(tup2)
print(type(tup2))

#--if comma not used tup2 type would be assumed same as type of first value

tup3=(12.44)
print(type(tup3))


#----tuple slicing

print(tup[0:2])

#---gives first index of element
print(tup.index(12))

#---count occurrences of element
print(tup.count(12))

#--------------------Palindrome
list1=[1,2,1]
list2=[2,3,4]

cp_list1=list1.copy()
cp_list1.reverse()
cp_list2=list2.copy()
cp_list2.reverse()

if cp_list1==list1:
    print("palindrome")
else:
    print("Not Palindrome")

    
