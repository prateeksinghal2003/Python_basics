#----------------------Files handling
#------------Open ,read a file


# f=open('files_notes.txt',"r")

#---read is the default
#---rt--is the read mode and opening text file
#-----t is by default
#----for binary files , must write rb


# data=f.read()
# print(data)
# print(type(data))
# f.close()


#--see different modes in notes

#---to read some characters
#data=f.read(5)

#---to read line by line
# line1=f.readline()
# line2=f.readline()
#
#
# print(line1)
# print(line2)


#---once read is called once, then if we do read(5) , it causes error , there are no 5 characters
#----because entire file is read


#-------------Writing to a file
# w--write mode--overwrite the existing content , replace with new,pointer is at starting
# a---append mode--pointer is at end , adds new content at the end of the file
#

# f=open('files_notes.txt',"a")
# f.write("I am new here")
# #--to insert at new line
# f.write("\nI am learning soon")
# f.close()


# f=open('files_notes.txt',"w")
# f.write("I am new here")
# f.close()

#----if no file exist , and we opened it , python will automatically create a new one

#f=open('demo.txt',"r+")

#--by r+ we can read and write , pointer is placed at starting , so if we write first
#---content already existing in file would be overwritten
#---after writing abc , pointer is placed after c of "abc" , so we get content after c
#f.write("abc")

# data=f.read()
# print(data)
# f.close()


#--w+ --> can read and write.file content is removed first , pointer is at starting

#f=open('demo.txt',"w+")

#---file content would be erased (truncated)
# data=f.read()
# print(data)
# f.close()


# f=open('demo.txt',"a+")
#--a+ --> can read and write.file content remains , pointer is at end
#---file content would remain but pointer is at last, so cannot read anything
# data=f.read()
# print(data)
# f.close()


#--------with syntax
#----will handle close by default
#---file would be presented as f
# with open("demo.txt",'r') as f:
#     print(f.read())


#----Deleting a file
#--import os module

# import os
# os.remove("demo.txt")

#----------------Programs


#1)remove all occurrences of python with java

with open("files_notes.txt","r") as f:
    data=f.read()
    new_data=data.replace("python","java")

with open("files_notes.txt","w") as f1:
     f1.write(new_data)

with open("files_notes.txt","r") as f:
    data=f.read()
    print(data)

#2)Search if learning exist or not

with open("files_notes.txt","r") as f:
    data=f.read()
    if data.find("java")!=-1:
        print("Found")
    else:
        print("Not Found")

#3)----tell in which line a word occurs

# word="fastest"
#
# lineno=0
# flag=False
#
# with open("files_notes.txt","r") as f:
#
#     data=True
#
#     while data:
#         data=f.readline()
#         lineno+=1
#
#         if word in data:
#             flag=True
#             print("Line number is ",lineno)
#
#
# if flag==False:
#     print("Not Found")

#4)numbers separated by comma,find even numbers

with open("files_notes.txt","r") as f:
    data=f.read()
    nums=data.split(",")

print(nums)

for val in nums:
    if int(val)%2==0:
        print(val)
