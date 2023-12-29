#when a function call itself it is called recursion.
def fun():
    print("hello")
    fun()                                #1000  times chalega and don't run
fun()                    


# def factorial(num):
#     if num==1:
#         return num
#     return num*factorial(num-1)

# number = int(input("enter a number: "))
# result = factorial(number)
# print("factorial of",result)







# def fib(n):
#     if n<=1:
#         return 1
#     return fib(n-1)+fib(n-2)
# pos = int(input("enter the position of fib number - "))
# print(fib(pos))









# def fib(i):
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     else:
#         return fib(i-2) + fib(i-1)
    
# for x in range(13):
#     print(fib(x))



# def suml(list):
#     x=list[0]+list[1]+list[2]+list[3]
#     return x
                                                                     
# a =int(input("how many numbers are there in a list - "))
# b =int(input("enter a number - "))
# c =int(input("enter a number - "))
# d =int(input("enter a number - "))
# e =int(input("enter a number - "))
# y=list((b,c,d,e))
# z=suml(y)
# print(z)







# def suml(list):
#     if len(list)==0:
#         return 0
#     x=list[0]+list[1]+list[2]+list[3]
#     return x


# a =int(input("how many numbers are there in a list - "))
# b =int(input("enter a number - "))
# c =int(input("enter a number - "))
# d =int(input("enter a number - "))
# e =int(input("enter a number - "))
# y=list((b,c,d,e))
# z=suml(y)
# print(z)




# def sumlist(nums):
#     if len(nums)==0:
#         return 0
#     return nums[0] + sumlist(nums[1:])

# numbers = []
# n = int(input("how many numbers are  there in your list "))
# for a in range(n):
#     num = int(input("enter a number:  "))
#     numbers.append(num)


# print("list is ",numbers)
# print("sum of list is ",sumlist(numbers))
# #print("sum of list is ",sum(numbers))






# def great(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# n1=int(input("enter first number"))
# n2=int(input("enter second number"))
# n3=int(input("enter third number"))
# y=great(n1,n2,n3)
# print("number is - ",y)




















