#--------------------------Loops

num=[10,20,30]
tup=(11,12,13)
a=1
wrd="hello"

while a<=5:
    print(a)
    a+=1

#-----break and continue
a=1
while a<=5:
    print(a)
    if a==3:
        break
    a+=1

a=1
while a<=5:

     if a==3:
        a+=1
        continue
     print(a)
     a+=1

#-----------------For loops
for el in num:
    print(el)

for n in tup:
    print(n)

for v in wrd:
    print(v)

#----optional else with for loop,for doing task after loop
#-----if break , comes else will not run , so else is used
# when we want to run something after complete loop runs
# else runs only if loop completes normally
# else does NOT run if break happens

for el in num:
    print(el)
else:
    print("after loop")



for n in num:
    if n % 2 != 0:
        print("Odd found")
        break
else:
    print("All numbers are even")

#--------range()---return sequence of numbers
#range(start,end,step_size)
# end value is not included
#default start value=0, step_size=1

seq=range(5)

for el in seq:
    print(el)

for el in range(2,10):
    print(el)

for el in range(2,10,2):
    print(el)

#-----pass Statement
#---does nothing, cannot leave empty body under loops

for el in range(2,10,2):
    pass

#---------Programs
sum=0

for el in range(1,6):
    sum=sum+el
    print(sum)
