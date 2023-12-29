# n = int(input("enter:- "))
# if n%2==0:
#     if n in range(2,6):
#         print("not wierd")
#     elif n in range(6,21):
#         print("wierd")
#     elif n>20:
#         print("not wierd")

# elif n%2!=0:
#     print("wierd")



# n = int(input("enter-: "))
# for i in range(0,n):
#     print(i*i)



# def is_leap(year):
#     x = year%400==0 or year%100!=0 and year%4==0
#     return x
    


# year = int(input())
# print(is_leap(year))   



# n = int(input("enter:- "))
# for i in range(1,n+1):
#     print(i,end=" ")




# dict = {
#     "amar":[98,97,93],
#     "akbar": [80,81,82],
#     "anthony":[50,51,52]
# }
# n = int(input("PRESS 1- for amar\nPRESS 2- for akbar\nPRESS 3-for anthony\n"))
# if n==1:
#     print((98+97+93)/3)
# elif n==2:
#     print((80+81+82)/3)
# elif n==3:
#     print((50+51+52)/3)



# em_id = input("enter your id-: ")
# if len(em_id)==10 and em_id.upper()>=2 and 





# total = 10
# mydict = {
#     2:50,
#     4:60,
#     5:70,
#     6:80,
#     7:90,
#     8:40,
#     9:30,
#     12:20,
#     15:50,
#     18:60
# }
# print(f"total number of shoes are-: 10")
# print("the sizes of the shoes are-",mydict.keys())
# cust = int(input("total number of customers-: "))
# sum = 0
# for i in range(cust):

#     buy = int(input("which size you want to buy:- "))
#     x = mydict.get(buy)
#     sum = sum + x 

# print("the total amount earned by the shopkeeper is",sum)

    


# first = input("enter your first name- \n")
# last = input("enter your last name- \n")

# if len(first) and len(last) <=10:
#     print(f"hello {first} {last} ! You just delved into python")
# else:
#     print("invalid input,first and last name must be less then 10 words")
    









# lst = []
# n = int(input("enter total of scores:- "))
# for i in range(n):
#     x = int(input("enter your score:- \n"))
#     lst.append(x)

# lst.sort()
# set(lst)
# x = lst[-2]
# print("the second largest value is",x)


# lst3 = []
# lst2 = []
# lst = []
# arr = int(input("total number of elements in list -  "))
# for i in range(arr):
#     n = int(input(" type elements for list-   "))
#     lst.append(n)

# a_b = int(input("total number of elements in set a and set b -  "))
# for i in range(a_b):
#     n2 = int(input("enter elements for set a-   "))
#     lst2.append(n2)

# for i in range(a_b):
#     n2 = int(input("enter elements for set b-  "))
#     lst3.append(n2)

# x = set((lst2))
# y = set((lst3))

# sum = 0
# for i in lst:
#     if i in lst2:
#         sum += 1
#     elif i in lst3:
#         sum -= 1

# print(sum)







# def changes(string,position,character):
#     x = list(string)
#     x[position] = "K"
#     listToStr = ''.join(map(str, x))
#     return listToStr

# print(changes("abracadabra",5,"K"))
    



# lst = []
# n = int(input(" enter total number elements of list- : "))
# for i in range(n):
#     elem = int(input(" enter elements of list-:  "))
#     lst.append(elem)

#     if all(lst) > 0:
#         print("true")
#         numb=any(lst)
#         temp=numb
#         rev=0
#     while(numb>0):

#         dig=numb%10
#         rev=rev*10+dig
#         numb=numb//10
#     if(temp==rev):
#        print("a number is palindrome!")
#     else:
#        print("No number is a palindrome!")





# a = input(" enter string- : ")
# b = a.split(" ")
# b = "-".join(a)
# print(b)



# lst = []
# n = int(input(" enter the total stamps-:  "))
# for i in range(n):
#     coun_name = input(" enter country name:- ")
#     lst.append(coun_name)
# y = set(lst)
# z = len(y)
# print(" the distinct countries are -: ",z)






# lst2 = []
# lst = []
# n = int(input("the number of students who have subscribed to the English newspaper -  "))
# for i in range(n):
#     roll = int(input("enter the roll number- "))
#     lst.append(roll)

# n2 = int(input("the number of students who have subscribed to the French newspaper -  "))
# for i in range(n2):
#     roll2 = int(input("enter the roll number- "))
#     lst.append(roll2)


# x = lst+lst2
# y = set(x)
# print("the total number of students who have at least one subscription.- ",len(y))






# def cap(userin):

    
#     x = userin.count("#")
#     y = userin.replace("#","")
#     z = "#"*x,y
#     return(z)
    

# userin = input("enter your word:- ")
# print(cap(userin))







# numbers =input("enter numbers -:  ")
# for n in numbers:
#     if numbers.count(n)>1:
#         print("repeat",n)







# print duplicates from a list of integers

#function
# def duplicate(li):
#     n=len(li)
#     dup=[]
#     for i in range(n):
#         k = i + 1
#         for j in range(k,n):
#             if li[i] == li[j] and li[i] not in dup:
#                 dup.append(li[i])
#     return dup

# #test
# li=[ 10, 20, 30, -10, -20, 10, 80, -10, -20, 30]
# print("Duplicate integeres: ",duplicate(li))




# n = input("enter # or * = ")
# a = list((n))
# if a.count("#") > a.count("*"):
#     print("positive")
# elif a.count("*") > a.count("#"):
#     print("negative")
# elif a.count("#") == a.count("*"):
#     print("0")








# Python3 Program to implement
# the above approach

# Function to return the count
# of array elements with all
# elements to its left smaller
# than it


# def count_elements(arr):

# 	# Stores the count
# 	count = 1

# 	# Stores the maximum
# 	max = arr[0]

# 	# Iterate over the array
# 	for i in range(1, len(arr)):

# 		# If an element greater
# 		# than maximum is obtained
# 		if arr[i] > max:

# 			# Increase count
# 			count += 1

# 			# Update maximum
# 			max = arr[i]
# 	return count


# # Driver Code
# arr = [2, 1, 4, 6, 3]
# print(count_elements(arr))








# lstc = []
# lste = []
# n = int(input("how many book you want to buy = "))
# for i in range(n):
#     e = int(input("how much earned for the book = "))
#     lste.append(e)
# for j in range(n):
#     c = int(input("how much cost for the book = "))
#     lstc.append(c)

# z = sum(lstc) - sum(lste)
# print(f"person has to take RS.{z} from his parents.")





# lst = []
# baseprice = 5
# weight = 15
# totalbags = int(input("enter total number of bags = "))
# for i in range(totalbags):
#     wb = int(input("enter weights of the bags = "))
#     lst.append(wb)

# x = [num for num in lst if num >15]
# y = [num for num in lst if num <=15]
# z = len(x)
# b = len(y)
# a = len(x)*10
# total = a+b
# print(total)





# litre = int(input("Enter the no of liters to fill the tank = "))
# distance = int(input("Enter the distance covered = "))
# if litre>0 and distance>0:
#     z = (litre/distance)*100
#     r = round(z,2)
#     print("litres per 100 km is",r)
#     m = (distance*0.6214)
#     l = (litre*0.2642)
#     x = (m/l)
#     r2 = round(x,2)
#     print("miles per gallon is",r2)
# else:
#     print("invalid input")




# pi = int(input("Enter the no of pizzas bought = "))
# pu = int(input("Enter the no of puffs bought = "))
# cd = int(input("Enter the no of cool drinks bought = "))
# total = (pi*100) + (pu*20) + (cd*10)
# print("total is",total)





# a = int(input("enter the digits = "))
# b = int(input("enter the digits = "))
# c = int(input("enter the digits = "))
# d = int(input("enter the digits = "))
# print(a,"w")
# print(b,"x")
# print(c,"y")
# print(d,"z")





# cse = int(input("Enter the no of students placed in CSE = "))
# ece = int(input("Enter the no of students placed in ECE = "))
# mech = int(input("Enter the no of students placed in MECH = "))

# if cse<0 or ece<0 or mech<0:
#     print("invalid input")
# elif cse==ece or cse==mech or ece==mech:
#     print("None of the department has got the highest placement")
# elif cse>0 and ece>0 and mech>0:
#     if cse>ece and cse>mech:
#         print("highest placement cse ")
#     elif ece>mech and ece>cse:
#         print("highest placement ece")
#     elif mech>cse and mech>ece:
#         print("highest placement mech")




# t = int(input("Enter the no of ticket = "))
# r = input("Do you want refreshment = ")
# c = input("Do you have coupon code = ")
# c2 = input("Enter the circle = ")
# circle = {
#     "k":75,
#     "q":150,
# }

# lst = ["yes"]
# lst2 = ["no"]
# if t>=5 and t<=40:
#     if t>=20 and r in lst and c in lst:
#         x = (t*(circle.get(c2)))+ ((t*12*(circle.get(c2)))/100) + (t*(circle.get(c2))*50)
#         a = round(x,2)
#         print("Total Cost:",a)
#     elif t>=20 and r in lst2 and c in lst:
#         y = (t*(circle.get(c2))) + ((t*12*(circle.get(c2)))/100)
#         b = round(y,2)
#         print("Total Cost:",b)
#     elif t>=20 and r in lst and c in lst2:
#         z = (t*(circle.get(c2))) + (t*(circle.get(c2))*50) + ((t*10*(circle.get(c2)))/100)
#         c = round(z,2)
#         print("Total Cost:",c)
#     elif t>=20 and r in lst2 and c in lst2:
#         w = (t*(circle.get(c2))) + ((t*10*(circle.get(c2)))/100)
#         d = round(w,2)
#         print("Total Cost:",d)
# else:
#     print("Minimum of 5 and Maximum of 40 Tickets") 




# a = {
#     1:"winter",
#     2:"winter",
#     3:"spring",
#     4:"spring",
#     5:"spring",
#     6:"summer",
#     7:"summer",
#     8:"summer",
#     9:"autmn",
#     10:"autmn",
#     11:"autmn",
#     12:"winter"
# }

# n = int(input("enter the month = "))
# if n>=1 and n<=12:
#     print(a.get(n))
# else:
#     print("invalid input")





# s=input()
# x=s.count("#")
# s=s.replace("#","")
# print("#"*x+s)










    










        







    



    











    







        

    










