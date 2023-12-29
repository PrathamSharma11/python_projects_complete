# a = int(input("enter the price"))
# b = int(input("enter the quantity"))
# c = int(input("enter the itemno."))
# print("i want to pay",a,"dollars for",b,"pieces of item",c)



# a = int(input("Enter Your Percentage - "))
# print("Your Percentage  Is ",a)
# if a>=90:
#     print("Very Well,You Are Promoted!")
# elif a>=50 and a<=90:
#     print("No Worries,You are Going To Repeat This Course")
# elif a>=30 and a<=50:
#     print("I Am Sorry You Are Demoted")
# else:
#     print("Get The Hell Out Of My Class.")










# option = ["yes","no"]
# a = input("You Got Vaccinated ?\n")
# if a in ["yes"]:
#     print("you can travel,thanks for applying")
# elif a in ["no"]:
#     print("sorry,but you cannot travel for now.")
# else:
#     print("write yes or no in the above question in lower.") 




# for num in 23,45,50,65,76,90:
#     if(num%5==0):
#         continue
#     if(num%10==0):
#         continue
#     if(num%3==0):










# customer = [
#              ["mohit",20,"bhopal",993922356],
#              ["rohit",19,"gwalior",636472829],
#              ["vishal",21,"indore",678993320],
#              ["shresth",22,"amritsar",84348293]
# ]
# print(customer)
# a = ["name","age","city","number"]
# b = input("What Do You Want To Find ? - ")
# if b in ["name"]:
#     print(customer[0][0])
#     print(customer[1][0])
#     print(customer[2][0])
#     print(customer[3][0])
# elif b in ["age"]:
#     print(customer[0][1])
#     print(customer[1][1])
#     print(customer[2][1])
#     print(customer[3][1])
# elif b in ["city"]:
#     print(customer[0][2])
#     print(customer[1][2])
#     print(customer[2][2])
#     print(customer[3][2])
# elif b in ["number"]:
#     print(customer[0][3])
#     print(customer[1][3])
#     print(customer[2][3])
#     print(customer[3][3])
# else:
#     print("sorry, but can't help you.")











# n = int(input("Enter A Number - "))
# print("table is - ")
# for i in range(1,11):
#    # print(n,"X",i,"=",n*i)
#    print(f"{num}X{i}={num*i}") #f string method




# a = int(input("enter a number - "))
# print("Numbers are - ")
# for i in range(1,a+1):
#     print(i)


# a = int(input("enter a number - "))
# sum = 0
# i = 1
# while i<=a:
#     sum = sum+i           
#     i = i+1                 
#     print("sum",sum)



# a = int(input("enter a number - "))
# sum =0
# i =2
#  while i<=a:
#      sum = sum+(i*i)
#      i =i+1
#      print("square",sum)





# a = int(input("enter  number -  "))
# i =2
# for i in range(a+1):
#     if(i%2==0):
#               print(i)





#1 = #b = int(input("Enter A Number - "))
#print("table of",b,"is")
#for i in range(1,11):
    #print(b,"X",i,"=",b*i)
    #print(f"{b}x{i}={b*i}")  #f string method


# i =1
# while i<=10:
#     print(b,"x",i,"=",b*i)
#     i = i+1



#2 = b = int(input("enter a number \n"))
# print("the numbers are - ")
# for i in range(1,b+1):
#     print(i)

# i =1
# while i<=b:
#     print(i)
#     i = i+1





# 3 = # b = int(input("enter a number - "))
# print("numbers are - ")
#for i in range (b,1,-1):
    #print(i)



# i = b
# while i>=1:
#     print(i)
#     i = i-1




#4 b = int(input("enter a number - "))
#print("sum from 1 to your number is - ")
# for i in range(1,b):
#     print(b*(b+1)//2)
#     break


# sum = 0
# i = 1
# while i<=b:
#     sum = sum + i
#     i = i+1
# print(sum)
       
    
# 5 b = int(input("enter a number"))
# print("sum of square from 1 to your number is - ")
# sum = 0
# i =1
# while i<=b:
#     sum = sum + i*i
#     i = i+1
# print(sum)

   


#6 # n =int(input("enter a number - "))
# print("only even numbers from 1 to your digit is - ")
# i = 2
# while i<=n:
#     print(i)
#     i = i+2
    
     

#7 # n = int(input("enter a number -  "))
# print("sum of even numbers from 1 to your number is - ")
# sum = 0
# i = 2
# while i<=n:
#       sum =sum+i
#       i = i+2
# print(sum)
        

#8i = int(input("enter number - "))
# sum = 0
# while i>0:
#     sum = sum + i%10                                #(i%10*i%10)
#     i = i//10
# print("sum of your entered number is - ",sum)



#9 i = int(input("enter a number"))
# p = i
# sum = 0
# while i>0:
#     sum = sum + (i%10)*(i%10)*(i%10)
#     i = i//10
# if p==sum:
#     print("armstrong")
# else:
#     print("not armstrong")




#10 n = int(input("enter a three digit number - "))
# print("multiplication of your given number is - ")
# product = 1
# while n>0:
#     product=product*(n%10)
#     n = n//10
# print(product)






#11 i =int(input("enter number to reverse - "))
# rev = 0
# while(i>0):
#     rev=(rev*10)+i%10
#     i = i//10
# print("reverse is - ",rev)



#12 n = int(input("enter a number - "))
# c = 0
# i = 1
# while(i<=n):
#     if(n%i==0):
#         c = c+1
#     i = i+1
# if(c==2):
#     print("prime")
# else:
#     print("not prime")



# n = int(input("enter a number = "))
# pro = 1
# while n>=1:
#     pro = pro*n
#     n = n-1
# print("factorial is - ",pro)















# n = int(input("how many  candies do you want? \n"))
# r = 10-n
# t = 10
# if n<=5:
#     print("total number of candies sold",n)
#     print("remaining candies left in the jar",r)
# elif n>5:
#     print("invalid input")
#     print("remaining candies left in the jar are",t)









# n = int(input("enter the weight of the clothes - "))
# if n>0 and n<=2000:
#     print("the time estimate is 25 minutes")
# elif n>=2001 and n<=4000:
#     print("the time estimate is 35 minutes")
# elif n>=4001 and n<=7000:
#     print("the time estimate is 45 minutes")
# elif n>=7001:
#     print("overloaded")
# else:
#     print("invalid input")






# n =int(input("enter number - "))          #fibnocci series
# x = 0
# y = 1
# z = 0
# while(z<=n):
#     print(z)
#     x = y
#     y = z
#     z = x+y
    








# n = int(input("enter a year to find out it is a leap year or not - "))
# if n%4==0 and n%100==0 and n%400==0:
#     print("it is a leap year")
# else:
#     print("not a leap year")
    







# a = int(input("enter oxygen level of 1st candidate after round 1: \n"))
# b = int(input("enter oxygen level of 2nd candidate after round 1: \n"))
# c = int(input("enter oxygen level of 3rd candidate after round 1: \n"))
# d = int(input("enter oxygen level of 1st candidate after round 2: \n"))
# e = int(input("enter oxygen level of 2nd candidate after round 2: \n"))
# f = int(input("enter oxygen level of 3rd candidate after round 2: \n"))
# g = int(input("enter oxygen level of 1st candidate after round 3: \n"))
# h = int(input("enter oxygen level of 2nd candidate after round 3: \n"))
# i = int(input("enter oxygen level of 3rd candidate after round 3: \n"))
# avg1 = (a+d+g)/3
# avg2 = (b+e+h)/3
# avg3 = (c+f+i)/3
# if avg1>avg2 and avg1>avg3:
#     print("candidate 1st has the highest average oxygen level")
# elif avg2>avg1 and avg2>avg3:
#     print("candidate 2nd has the highest average oxygen level")
# elif avg3>avg1 and avg3>avg2:
#     print("candidate 3rd has the highest average oxygen level")
# elif avg1==avg2:
#     print("both of them 1st and 2nd have highest oxygen level")
# elif avg1==avg3:
#     print("both of them 1st and 3rd have highest oxygen level")
# elif avg2==avg3:
#     print("both of them 2nd and 3rd have highest oxygen level")
# else:
#     print("nobody selected")










# a = int(input("enter no. of interior walls - "))
# b = int(input("enter no. of exterior walls - "))
# total = (a*18)+(b*12)
# a1 = a*18
# b1 = b*12
# if a <= 0 and b<=0:
#     print("you do not want any wall to be printed.") 
# elif a>=1 and b>=1:
#     print("total cost is - ",total)
# elif a>=1 and b<=0:
#     print("you don't want the outer walls to be printed.So you're total is -",a1)
# elif a<=0 and b>=1:
#     print("you do not want the inner walls to be printed.So you're total is -",b1)


















# print("Welcome To SBI")
# balance = 10000
# bk = [1,2]
# a = str(input("Enter Your PIN - "))
# if len(a)>4:
#     print("INVALID PIN")
# if len(a)<=4:
#     print("Yoh Have Entered.")
#     print("press 1 to balance enquiry")
#     print("press 2 to cash withdrawl")
#     print("press 3 to balace pay in")
#     print("press 4 to return card")
# choose = int(input("what would you like to press - "))
# if choose in range (1,2):
#     print("You Have Rs.10000 in your Ac")


        



    
# print("WELCOME TO SBI")
# bal = 10000

# bk = ["yes","no"]
# pin = str(input("ENTER YOUR 4 DIGIT PIN \n"))
# if len(pin)>4:
#     print("INVALID PIN")
    
# elif len(pin)==4:
#     print("YOU HAVE ENTERED")
# i = 1
# while i>0:
#     options = print(" PRESS 1 FOR BALANCE ENQUIRY \n PRESS 2 TO CASH WITHDRAWL \n PRESS 3 TO BALANCE PAY IN \n PRESS 4 TO RETURN CARD")
#     press = int(input("WHAT WOULD YOU LIKE TO PRESS-\n"))
#     if press in range(1,2):
#         print("YOU're BALANCE IS - ",bal)
#         back = (input("WOULD YOU LIKE TO GO BACK - "))
#     if press in range(2,3):
#         wd = int(input("HOW MUCH MONEY YOU WANT TO WITHDRAWL - \n 1000  2000 4000 6000 \n"))
#         left = bal - wd
#         if wd in range(1000,9000):
#             print("MONEY YOU HAVE LEFT IN YOUR ACCOUNT - ",left)
#         back = (input("WOULD YOU LIKE TO GO BACK - "))
#     if press in range(3,4):
#         add = int(input("HOW MUCH MONEY YOU WANT TO ADD \n"))
#         new = bal + add 
#         print("MONEY YOU HAVE IN YOUR ACCOUNT -  ",new)
#         back = (input("WOULD YOU LIKE TO GO BACK - "))
#     if press in range(4,5):
#         print("CARD IS RETURNED")
#         back = (input("WOULD YOU LIKE TO GO BACK - "))
#     if back in ["yes"]:
#          print("ok")
         
#     elif back in ["no"]:
#          print("THANKS,FOR CHOOSING SBI")
#          break
#     i = i+1







