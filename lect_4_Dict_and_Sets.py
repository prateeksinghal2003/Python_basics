#-----------------Dictionary and Sets
#-Dictionary---store comma separated key value pairs
#keys cannot be list and dict
#keys can be int,float
#they are mutable
#they are unordered,order in which keys are inserted , on printing can come in different order

dict={
    "name" : "karan",
    "age" : 25,
    "height" : 65,
    "weight" : 70,
    12:12
}

print(dict)
print(dict["name"])
print(type(dict))

dict["name"]="Alice"
dict["gender"]="male"
print(dict)


#-----------------Nested Dictionary
student={
    "name":"Alice",
     "marks":{
         "maths":23,
         "chem":34
     }
}

print(student)
print(student["marks"]["maths"])
print(student["marks"])

#--------------------Methods in Dictionary

#return all keys
print(student.keys())

print(list(student.keys()))

#--number of keys
print(len(student))
print(len(list(student.keys())))

#-------.values()---to get values from key value pair
print(student.values())
print(list(student.values()))


#-----.items()---return all pairs in the form of tuple

print(student.items())
print(list(student.items()))

#--------.get(key)----return value of key
print(student.get("name"))
print(student["name"])

#----if key does not exist .get(key) would return None, while dict_name[key] will give an error
print(student.get("name2"))
# print(student["name2"])


#-------------update()---add more key value pair that is adding new dictionary
#----if in update existing keys are used , value would get overwrite
student.update({"city":"delhi"})
print(student)

student.update({"name":"Alex"})
print(student)

#------------------------------------Sets

#they are unordered and all items are immutable
#since elements are immutable , so cannot store list and dictionary, tuple can be added
#but set is immutable , can add or remove elements

collections={1,2,34,4,4,4,4,4,4,"world"}
print(collections)
print(len(collections))

#--creating empty dictionary
collect={}

collection=set()
print(collection)
print(len(collection))

#---------------------Set Methods
#------set.add(el)

collection.add(1)
collection.add(2)
print(collection)

collection.remove(2)
print(collection)

# collection.clear()
# print(collection)

collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.add(6)
print(collection)


#---pop() can  be random
print(collection.pop())
print(collection.pop())
print(collection.pop())
print(collection.pop())

#---------set.union(set2)---returns new set
#----------set.intersection(set2)  ---returns new set

set1={1,2,3}
set2={1,4,5,6}


print(set1.union(set2))
print(set1.intersection(set2))


#-------------------------Program

set3={9,9.0}
print(set3)

set4={9,"9.0"}
print(set4)