# def conv(y):
#     x=(y * 9/5) + 32
#     return x
# y =int(input("enter temperature in degree celsius - \n"))
# z=conv(y)
# print("temperature in fahrenheit is - ",z)






# print("hello",end=" ")
# print("are",end=" ")
# print("you",end=" ")




# def sumn(n):
#     if x==0:
#         return 0
#     else:
#         x=n(n+1)/2
#         return x
# n=int(input("enter a number - \n"))
# z=sumn(n)
# print("the sum is - ",z)





# def pyr(a):
#     for i in range(a,0,-1):
#         for j in range(i,0,-1):
#             print("*",end="")
#         print()
    
# a=int(input("enter number -"))
# pyr(a)





# def rep_strip(word):
#     x=a.replace(word,"")
#     return x.strip()

# a="      pratham      is       good    "
# z=rep_strip("pratham")
# print(z)




# def remove(b):
#     a.remove(b)
#     return a

# a=[1,2,3,4,5]
# print(a)
# b=int(input("enter a number to remove - \n"))
# z=remove(b)
# print(z)




# def sum(python,apti,reas):
#     a=python+apti+reas
#     return a

# def average(all):
#     y=(all/300)*100
#     print("your average in exam is - ",y)

# all=sum(80,84,76)
# average(all)






# n = int(input("Enter number of Stairs:"))
# def cal(x):
#     if x <= 1:
#         return x
#     return cal(x - 1) + cal(x - 2)


# def total(n):
#     return cal(n + 1)


# print("Number of ways:", total(n))





# a = int(input("enter the money first house has- "))
# b = int(input("enter the money second house has- "))
# c = int(input("enter the money third house has- "))
# d = int(input("enter the money 4th house has- "))
# e = int(input("enter the money 5th house has- "))      #house theif problem,but it is wrong  
# f = int(input("enter the money 6th house has- "))
# g = int(input("enter the money 7th house has- "))
# n = list((a,b,c,d,e,f,g))
# print(n)
# sum = a+c+e+g
# print("the maximum you could stole is - ",sum)








# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")




# b = ["yes","no"]
# n =input("enter the parent member name :\n")
# a = input("do you have any child member :\n")
# if a in ["yes"]:
#     print("enter name of child members:\n")
#     n1 = input("")
#     n2 = input("")
#     print("the child members are - ",n1,",",n2 )        #can't do

    
# elif a in ["no"]:
#     print("ok")



# submenu = {
#     1 : "espresso",
#     2 : "cappacino",
#     3 : "latte"
# }
# list = ["c","t","s","b"]
# menu = print("coffee\ntea\nsoup\nbeverages")
# a = input()
# if a in ["c"]:
#     print(submenu)
#     b = int(input())
#     print("welcome to CCD,\n enjoy your")
#     print(submenu.get(b))
# else:
#     print("invalid")





# def fun(x,ans):
#     if x==0:
#         return 0
#     else:
#         return fun(x,x+ans)
# print(fun(2,0))




# def func(x, ans):
#     if(x==0):
#         return 0
#     else:
#         return(func(x-1, x+ans))
# print(func(2,0))






# def func(n):
#     if (n>100):
#         return n-5 
#     return func(func(n+11))
# print(func(45))






# x = "abcdef"
# i = "a"
# while i in x:
#     print(i,end="")



# total = 1000
# mydict = {
#     1 : 500,
#     2 : 700,
#     3 : 200
# }
# print("1.apple\n2.samsung\n3.mi\n4.oppo")
# n = int(input(""))
# if n==1:
#     left = total - mydict.get(n)
#     print("remaining is - ",left)





# total = 1000
# mydict = {
#     1 : 100,
#     2 : 80,
#     3 : 60,
#     4 : 40
# }


# def repeat():

#     print("1.apple,Rs.100\n2.samsungRs.80\n3.mi,Rs.60\n4.oppo,rs.40")
#     n = int(input(""))
#     sum = 0 
#     sum = sum + mydict.get(n)
#     a = input("wanna go back? :- ")
#     if a in "yes":
#         repeat()
#     else:
#         left = total - sum 
#         print("total bill",sum)
#         print("left in your account",left)
#         exit()
# repeat()
    



# mydict = {
#     1 : 100,
#     2 : 80,
#     3 : 60,
#     4 : 40
# }
# lis = []
# def repeat():

    
#     n = int(input("1.apple,Rs.100\n2.samsungRs.80\n3.mi,Rs.60\n4.oppo,rs.40\n"))
#     lis.append(mydict.get(n))
#     total = sum(lis)
#     x = input("wanna back:-- ")
#     if x in ["yes"]:
#         repeat()
#     else:
#         print("total bill is",total)
# repeat()










# def TicketingSystem(a):
#     x = (50)*a/100
#     z = 50 - x
#     return z 


# p1 = int(input("enter your age -  "))
# p2 = int(input("enter your age -  "))
# p3 = int(input("enter your age -  "))
# p4 = int(input("enter your age -  "))
# p5 = int(input("enter your age -  "))

# lst = list((p1,p2,p3,p4,p5))
# lst.sort()
# a = lst[0]

# y = TicketingSystem(a)
# print("the total price of your tickets after discount is -  $",y)





# n = int(input("enter a number - "))
# for i in range(n,0,-1):
#     if i%5==0:
#         print("beep")
#     print(i)



# n = int(input("enter no. of cakes - "))
# sum = 0 
# i = 1
# while i<=n:
    
#     sum = sum + i 
#     i = i+1
#     i<=n
    
# print("the total number of eggs will be used - ",sum)






# n = int(input("enter a palindrome to check-: "))
# prat = n 
# rev = 0 
# while n>0:
#     rem = n%10
#     rev = rev*10+rem 
#     n = n//10

# if rev==prat:
#     print("TRUE")
# else:
#     print("FALSE")








# mylist = ["break", "case", "continue", "default", "defer", "else", "for"]
# n = input("enter the word-: ")
# if n in mylist:
#     print(f"{n} is a keyword")
# else:
#     print(f"{n} is not a keyword")


# list_of_patients = []
# total_patient = int(input("Total Patients visited in a day-: "))
# for patients_age in range(total_patient):
#     patients_age = int(input("enter age of patient-: "))
#     list_of_patients.append(patients_age)
# print(list_of_patients)






# def loan(how_much):
#     x = how_much*(10/100)
#     y = how_much - x
#     z = y*(10/100)
#     u = y-z
#     v = u*(10/100)
#     w = u-v 
#     left = how_much+x+z+v
#     return left




# how_much = int(input("how much money you want:?\n"))
# pratham = loan(how_much)
# print("You Owe Your Friend after 3 month (interest+loan)-: ",pratham)



# lst=[]
# n = int(input("enter total number of height-: "))
# for i in range(1,n+1):
#     student_height=int(input("enter your height-: "))
#     lst.append(student_height)
# x = sum(lst)/n
# y = round(x)
# print("the average height is -",y)




# a = input("enter the string = ")
# if 'a' in a:
#     h = a.count
#     print(h)
# if 'b' in a:
#     i = a.count
#     print(i)

# if i>h:
#     print('positive')
# elif h>i:
#     print('negative')
# else:
#     print('0')





# a = int(input("Enter the no of liters to fill the tank: "))
# b = int(input("Enter the distance covered: "))
# if a and b == 0 or a and b <=0:
#     print('invalid,put something positive')
# elif a and b >0:
#     cal = (a/b)*100
#     x = round(cal,2)
#     print('liters/100km',x)
#     miles = b*0.6214
#     gallon = a*0.2642
#     calc = miles/gallon
#     y = round(calc,2)
#     print('miles per gallon',y)


# a = int(input("Enter the no of pizzas bought :"))
# b = int(input("Enter the no of puffs bought :"))
# c = int(input("Enter the no of cool drinks bought :"))

# d = a*100
# e = b*20
# f = c*10
# bill = d+e+f
# print("total bill",bill)
# print("enjoy the show")

# list=[]
# for i in range(4):
#     n = int(input("enter the digits: "))
#     list.append(n)
# a = {
#     list[0]:"P",
#     list[1]:"Q",
#     list[2]:"R",
#     list[3]:"S",

# }
# print(a)


# list = []
# a = int(input("total no in array: "))
# for i in range(a):
#     n = int(input("type your number: "))
#     list.append(n)
    
# b = int(input("the number you want to searched= "))
# if b in list:
#     print("yes")
# else:
#     print("no")



# a = int(input("Enter the no of students placed in CSE :"))
# b = int(input("Enter the no of students placed in ECE :"))
# c = int(input("Enter the no of students placed in MECH :"))

# if a and b and c <0:
#     print("input is invalid")
# elif a==b==c:
#     print("None of the department has got the highest placement")
# elif a>b:
#     print("CSE got the highest")
# elif a>c:
#     print("CSE got the highest")
# elif b>c:
#     print("ECE got the highest")
# elif b>a:
#     print("ECE got the Highest")
# elif c>a:
#     print("Mech got the Highest")
# elif c>b:
#     print("Mech got the Highest")




# a = int(input("enter the number of tickets = "))
# if a<5 and a>40:
#     print("minimum of 5 and maximum of 40 tickets")
# else:
#     circle = input("enter the circle: ")
#     if circle == "k":
#         n = 75*a 
#     elif circle =="q":
#         n = 150*a
#     cost = n

# c = input("do you want to use the coupon code: ")
# if c=="y":
#     cost2 = cost*0.1
#     cost3 = cost-cost2
# else:
#     cost3 = cost

# r = input("do you want the refreshment: ")
# if r=="y":
#     cost4 = cost3+50

# else:
#     cost4 = cost3

# z = round(cost4,2)
# print("your total bill", z)



# a = {
#     12: "winter",
#     1 : "winter",
#     2 : "winter",
#     3: "spring",
#     4: "spring",
#     5: "spring",
#     6: "summer",
#     7: "summer",
#     8: "summer",
#     9: "autumn",
#     10: "autumn",
#     11: "autumn"
# }

# n = int(input("enter the month: "))
# if n>=1 and n<=12:
#     print(a.get(n))
# else:
#     print("invalid input")



#prime number in an interval
# a = int(input("enter the lower value: ")) 
# b = int(input("enter the upper value: "))

# if a>b or a<0 or b<0:
#     print("invalid input")

# else:
#     for number in range(a,b+1):
#         if number>1:
#             for i in range(2,number):
#                 if number%i==0:
#                     break
#                 else:
#                     print(number,end=" ") 






# #prime number
# number = int(input("Enter any number: "))

# # prime number is always greater than 1
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")

# # if the entered number is less than or equal to 1
# # then it is not prime number
# else:
#     print(number, "is not a prime number")








# salary =int(input("enter the salary= "))
# app = int(input("enter the appraisal ratings= "))
# if app>=1 and app <=3:
#     z = salary*0.1
#     print(z+salary)
# elif app>=3.1 and app <=4:
#     z = salary*0.25
#     print(z+salary)
    
# elif app>=4.1 and app <=5:
#     z = salary*0.3
#     print(z+salary)
# else:
#     print("invalid input")




# count = 0
# a = int(input("enter the lucky number = "))
# while a>0:
#     a = a//10
#     count = count+1
# z = count
# if z==4:

    
    
#     x  = a //1000
#     x1 = (a - x*1000)//100
#     x2 = (a - x*1000 - x1*100)//10
#     x3 = a - x*1000 - x1*100 - x2*10
#     b = x+x1+x2+x3
#     if b%3==0 or b%5==0 or b%7==0:
#         print("lucky number")
#     else:
#         print("not a lucky number")
# else:
#     print("invalid input")






# lst = []
# n = int(input("enter the number of courses = "))
# if n>0 and n<=20:
    
#     for i in range(n):
#         a = input("enter the course: ")
       
#         lst.append(a)
#     c = input("which course you want to search: ")
#     if c in lst:
#         print(c,"is available")
#     else:
#         print("not available")

# else:
#     print("not valid")




# z=[]
# a = int(input("enter the number= "))
# if a==0:
#     print("invalid")
# else:
#     for i in range(1,a+1):
#         if a%i==0:
#             print(i)


# lst=['a','e','i','o','u']
# a = input('enter the word= ')
# o = a.replace(' ','')
# b = list(o)
# c = len(b)
# d = c-1
# if b[0] and b[d] in lst:
#     print('present')
# else:
#     print('not present')


# n = int(input(" "))
# q = int(input(" "))
# if q==1:
#     a = n*(n+1)/2
#     print(a)
# elif q==2:
#     i=0
#     prod=1
#     while i<n:
#         i=i+1
#         prod=prod*i
#     print(prod)



















