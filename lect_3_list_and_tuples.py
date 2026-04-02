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
#if no index is passed , remove last item
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


#----tuple slicing

print(tup[0:2])

#---gives first index of element
print(tup.index(12))

#---count occurrences of element
print(tup.count(12))


#--------------------Palindrome
list1=[1,2,1]


cp_list1=list1.copy()
cp_list1.reverse()


if cp_list1==list1:
    print("palindrome")
else:
    print("Not Palindrome")



""" What is a shallow copy?

 It copies:

 the outer list
 NOT the inner objects (nested elements)
 Example (important)
list1 = [1, 2, [3, 4]]
cp = list1.copy()

cp[2][0] = 99

print(list1)   # [1, 2, [99, 4]]
print(cp)      # [1, 2, [99, 4]]

 Why both changed?
Because inner list [3,4] is shared

 Simple understanding
Shallow copy → references copied
Deep copy → everything copied
 Deep copy (for comparison)
import copy

cp = copy.deepcopy(list1)

Now changes WON’T affect original

 One-line answer (exam)

list.copy() creates a shallow copy where only 
the outer list is copied, but nested objects are shared.


list1 = [1, 2, 3]
cp_list1 = list1.copy()
🔹 Why is it shallow?
A new list object is created ✔
But elements inside are just references copied 

👉 In this case:

Elements = 1, 2, 3 (integers)
Integers are immutable → so no issue appears
🔹 Important point

👉 Since there are no nested (inner) objects,
it looks like a deep copy — but actually it's still shallow

list.copy() creates a shallow copy; in non-nested lists 
it appears independent because elements are immutable."""