#no argument no return
# def oe():
#     a =int(input("enter number - "))
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# oe()



#with argument no return
# def add(a,b):
#     c =a+b
#     print("addition - ",c)
# a = int(input("enter -"))
# b = int(input("enter - "))

# add(a,b)




#no argument with return
# def add():
#     a = int(input("enter - "))
#     b = int(input("enter 2nd no. "))
#     c = a+b
#     return c
# s = add()
# print("addition",s)



#with argument with return
# def add(a,b):
#     c = a+b
#     return c

# a = int(input("enter 1st no.- "))
# b =int(input("enter 2nd no.- "))
# x = add(a,b)
# print("addition",x)






def verify(num1,num2):
    if num1 > num2:
        return num1
    elif num1==num2:
        return 1
    else:
        return num2


def display(arg1,arg2):
    if(verify(arg1,arg2)==arg1):
        print("A")
    elif(verify(arg1,arg2)==1):
        print("c")
    else:
        print("b")
display(1000,3500)


