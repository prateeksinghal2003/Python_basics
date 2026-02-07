#------------------Functions
def  cal_sum(a,b):
    return a+b

print(cal_sum(1,2))

#----Default parameters , when no value passed  to parameters, take default values


def prod(a=1,b=2):
    return a*b

print(prod())


#--------Recursions

def show(n):
    if n==0:
        return
    print(n)
    show(n-1)


show(5)

def cal_sum_nat(n):
    if n==1:
        return n
    return cal_sum_nat(n-1)+n

print("Sum of numbers till n")

print(cal_sum_nat(5))

list=[1,2,3,4,5,6]
a=len(list)


def print_list_ele(list,idx):
    if idx==a:
        return
    print(list[idx])
    print_list_ele(list,idx+1)


print_list_ele(list,0)