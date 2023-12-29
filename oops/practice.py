# class phone:
#     x = "i want apple"

# samsung = phone()
# print(samsung.x)



# class car:
#     e = "bugatti"
#     def nfs(self):
#         print("expensive")

# santro = car()
# santro.nfs()




# a = input("enter your name : ")
# class Reservation:
#     def info(self):
#         print(f"name is {self.name}")
#         print(f"train is {self.train}")
# travelling = Reservation()
# travelling.name = a 
# travelling.train = "shatabdi"
# travelling.info()



# class Reservation:
#     def info(self,name,train):
#         print(f"name is {name},train name is {train}")
        
# travelling = Reservation()
# travelling.info("pratham","shatabdi")












# class hello:
#     def function(self,a):
#         print("greetings from india.",a)
# p1 = hello()
# p1.function("pratham")









# a = input("enter name: ")
# b = input("enter name: ")
# class Programmer:
#     def info(self,name,b):
#         print(f"{name},is working on windows 12")
#         print(f"{b},is the PA of CEO")

# investigation = Programmer()
# investigation.info(a,b)





# class Programmer:
#     def info(self):
#         print(f"{self.name},is working on {self.b}")
       
# investigation = Programmer()
# investigation.name = "james"
# investigation.b = "windows11"
# investigation.info()











# a = int(input("how many episode you have seen until now? : "))
# class lost:
#     salary = 5000
#     role = "big"

#     def paid(self):
#         print("they got a lot.")
    
#     def amount(self):
#         print(f"the money he got for acting in lost is {self.salary} for a {self.role} role ")
    
#     @staticmethod
#     def watch(a):
#         print(f"you have watched {a} episodes.")
# actor = lost()
# actor.paid()
# jack = lost()
# jack.salary = 10000
# john = lost()
# john.salary = 8000
# kate = lost()
# jack.amount()
# john.amount()
# kate.amount()
# #actor.watch(a)
# jack.watch(a)






# class calc:
#     def square(self,a):
#         print(f"the square is : {a*a}")
#     def cube(self,b):
#         print(f"the cube is : {b*b*b}")
# pratham = calc()
# pratham.square(2)
# pratham.cube(2)







# class Calc:
#     def __init__(self,number):
#         self.number = number
    
#     def square(self):
#         print(f"the square of your given number {self.number} is - {self.number**2}")
    
#     def cube(self):
#         print(f"the cube of your number{self.number} is - {self.number**3}")
    
# find = Calc(2)
# find.square()
# find.cube()






# a = int(input("how many seat you want to book ? -  "))
# class Train:
#     total = 10
#     def __init__(self,name,train_name,seat,pay,left_seat):
#         self.name = name 
#         self.train_name = train_name
#         self.seat = seat
#         self.pay = pay
#         self.left_seat  = left_seat
        
    
#     def first(self):
#         print(f"the passenger name is - {self.name}\n the train name is - {self.train_name}")

#     def second(self):
#         print(f"your ticket has been confirmed your seat number is - {self.seat} \n and total amount of your journey is  -  Rs.{self.pay}")
    
#     def third(self):
#         self.left_seat = self.total - self.a
#         print(f"and the remaining seats available in the train are - {self.left_seat}")
#         if self.a>self.total:
#             print("go for tatkal")
#     @staticmethod
#     def greet():
#         print("have a great journey!!!")

# journey = Train("pratham","Intercity Express","D-4,S-5","720",10)
# journey.first()
# journey.second()
# journey.a = a
# journey.third()
# journey.greet()



# lst = []
# n = int(input("book"))
# for i in range(n):
#     a = input("names: ")
#     lst.append(a)
# print(lst)


# n = int(input("how many seat: "))
# l = 10-n
# for i in range(10,l,-1):
#     print(i,end=",")




#print(50*"*","dsf",50*"*")






# list = []
# class IRCTC:
#     total = 10
#     def __init__(self,train_name,left_seat,pay):
        
#         self.train_name = train_name
#         self.left_seat = left_seat
#         self.pay = pay 
#         print(30*"*","RAILWAYS",30*"*")
    
#     def info(self):
#         for i in range(n):
#             nm = input("enter name of the passenger:  ")
#             list.append(nm)
#         print("the passenger names are -  ",list)

#     def book(self):
#         self.left_seat = self.total - n
#         if self.left_seat > 0:
#            print(f"remaining seats are {self.left_seat}")
#         else:
#             print(f"Sorry,no seat left kindly try in tatkal.")
            
#     def fair(self):
#         print(f"the total fair for your ride is Rs.{n*self.pay} (Rs.200 per person)")
    
    
#     def tranam(self):
#         print(f"Your Train Name is {self.train_name} and your train number is - 270101")
    
#     def chair(self):
#         l = 10 - n
#         for i in range(10,l,-1):
#             print(f"Your Ticket Has Been Booked, and your seat numbers are - ",i)
    
#     @staticmethod
#     def greet():
#         print("Thanks For Choosing Us,Have A Nice Journey!!!")

# train = IRCTC("Intercity",10,200)
# n = int(input("How Many Seat You Want To Book ? : "))
# train.book()
# train.info()
# train.fair()
# train.tranam()
# train.chair()
# train.greet()










# list = [1,2]
# list2 = [2]
# list3 = [4]
# class Recharge:
#     total = 1000

#     def __init__(self,name,passw,select):
#         print(30*"*","Welcome To Bharat Pay",30*"*")
#         self.name = name
#         self.passw = passw
#         self.select = select

#     def login(self):
#         name = input("Enter Your Name:- \n")
#         passw = int(input("Enter Your Pin:- \n"))
#         if name==self.name and passw==self.passw:
#             print(f"Welcome {self.name} You Have Rs.{self.total} in your Account.")   
#         else:
#             print("INVALID INPUT")
#     def pp(self):
#         if n in list:
#             print("Choose An Operator-: \n1.Airtel \n2.JIO \n3.Vodafone \n4.Idea")
#         else:
#             print("Sorry, We Are Currently Not  Providing The Service")
    
#     def operator(self):
#         if a in list2:
#             print("1. MRP 98,Validity:14 days,Data:1.5GB,Unlimited Voice Calls")
#             print("2. MRP 127,Validity:15 days,Data:12GB,Unlimited Voice Calls")
#             print("3. MRP 149,Validity:24 days,Data:1GB,Unlimited Voice Calls")
#             print("4. MRP 199,Validity:28 days,Data:1.5GB,Unlimited Voice Calls")
#         else:
#             print("Sorry, We Are Currently Not  Providing The Service")
    
#     def selecting_plan(self):
#         if b in list3:
#             print("you have choosen - MRP 199,Validity:28 days,Data:1.5GB,Unlimited Voice Calls")
#         else:
#             print("Sorry, We Are Currently Not  Providing The Service")
#     def payment(self):
#         self.left = self.total - self.select
#         print(f"RECHARGE SUCCESSFUL!!!\nAccount Balance-: Rs.{self.left}") 
    
#     @staticmethod
#     def greet():
#         print("THANKS, For Choosing US.")

# sim = Recharge("pratham",2001,199)
# sim.login()
# n = int(input("What Do You Want To Choose-: \n1.Prepaid \n2.postpaid \n"))
# sim.pp()
# a = int(input())
# sim.operator()
# b = int(input())
# sim.selecting_plan()
# sim.payment()
# sim.greet()




# back = ["yes","no"]
# class ecom:
#     company = "amazon"
#     total = 10000
#     def __init__(self,cost,left):
#         self.cost = cost
#         self.left = left 
        

    
#     def balance(self):
#         self.left = self.total - self.cost
#         print(f"you have Rs.{self.left} in your account")
    
    
#     @staticmethod
#     def greet():
#         print(30*"*","AMAZON.in",30*"*") 
    
#     def mobile(self):
#         print("1.APPLE\n2.SAMSUNG\n3.OPPO\n4.MI")
    
#     def TypesMobile(self):
#         print("1.iPhone 12 Pro\n2.iPhone 12\n3.iPhone11\n4.iPhone XR")
#     def types(self):
#         print("1.MOBILE\n2.TV\n3.AIRCON\n4.LAPTOP")
#         t = int(input("what do you want to buy? :- "))
#         if t in range(1,2):
#             cust.mobile()
#             m = int(input("which phone do you want? :-"))
#             if m in range(1,2):
#                 cust.TypesMobile()
#                 iphone = int(input("which iPhone Do you want to buy? :- "))
#                 if iphone ==1:
#                     print("SUCCESSFULLY ADDED TO YOUR CART.")
#                     cust.balance()
#                     bac = str(input("do you want to go back-: "))
#                     if bac in ["yes"]:
#                         print("ok")
#                     else:
#                         print("ok")
                        
                        
# cust = ecom(9000,0)
# cust.greet()                       
                     
# i = 1
# while i>0:
#     cust.types()
    
# i = i+1


    





# class vehicle:
#     company = "honda"

# bike = vehicle()
# bike.max_speed = "100km/h"
# bike.milege = 20
# print(bike.max_speed)

#or

#class vehicle:
    # def __milegeinit__(self,max_speed,milege):
    #     self.max_speed = max_speed
    #     self.milege =  milege
    
    #def c(self,a,b):
        #print(f"the speed of your bike is- {self.max_speed} and milege is - {self.milege}")
        #print(f"the speed of your bike is- {a} and milege is - {b}")
        
#bike = vehicle(200,35)
#bike.c()


# bike = vehicle()
# bike.max_speed = 200
# bike.milege = 30
# bike.c()


# bike = vehicle()
# bike.c(200,30)







mobdict = {
    1 : 100000,
    2 : 80000,
    3 : 10000,
    4 : 30000
}

tvdict = {
    1 : 50000,
    2 : 30000,
    3 : 40000,
    4 : 25000
}

aircondict = {
    1 : 70000,
    2 : 50000,
    3 : 40000,
    4 : 65000
}
laptopdict = {
    1 : 70000,
    2 : 50000,
    3 : 40000,
    4 : 65000
}

lst = []


def again():
    class Ecom:
        
        def __init__(self,total):
            self.total = total
            
            

        @staticmethod
        def header():
            print(30*"*","AMAZON",30*"*")
        
        #def cost(self):
            #bill = sum(lst)
            #self.left = self.total - self.select_mi
            #print(f"your bill is {self.select_mi}, & you have Rs. {self.left} left in your account")
        
        # def cost2(self):
        #     self.left = self.total - self.select_lg
        #     print(f"your bill is {self.select_lg}, & you have Rs. {self.left} left in your account")

        # def cost3(self):
        #     self.left = self.total - self.select_dell
        #     print(f"your bill is {self.select_dell}, & you have Rs. {self.left} left in your account")





        def product(self):
            print("1.MOBILE\n2.TV\n3.AIRCON\n4.LAPTOP")
            product_name =int(input("what do you want to choose ?:- "))
            if product_name in range(1,2):
                print("1.APPLE,Rs.100,000\n2.SAMSUNG,Rs.80,000\n3.MI,Rs.10,000\n4.OPPO,Rs.30,000")
                n = int(input("which mobile do you want to choose ?:- "))
                if n in range(1,5):
                    lst.append(mobdict.get(n))
                    print(f"You Have Successfully Purchased {n} & It Has Been Added To Your Cart.")
                    bac = str(input("Would You Like To Go Back- ? "))
                    if bac == "yes":
                        print("OK")
                        again()
                    else:
                        #cust.cost()
                        bill = sum(lst)
                        print("YOUR TOTAL BILL IS - ",bill)
                        print("Thanks For Shopping With US,Have A Great Day!!!!")
                        exit()
            
            if product_name in range(2,3):
                
                print("1.SONY,Rs.50,000\n2.LG,Rs.30,000\n3.SAMSUNG,Rs.40,000\n4.MI,Rs.25,000")
                n = int(input("what do you want to choose ?:- "))
                if n in range(1,5):
                    lst.append(tvdict.get(n))
                    print(f"You Have Successfully Purchased {n} & It Has Been Added To Your Cart.")
                    bac = str(input("Would You Like To Go Back- ? "))
                    if bac == "yes":
                        print("OK")
                        again()
                    else:
                        #cust.cost2()
                        bill = sum(lst)
                        print("YOUR TOTAL BILL IS - ",bill)
                        print("Thanks For Shopping With US,Have A Great Day!!!!")
                        exit()

            

            if product_name in range(3,4):
                print("1.VOLTAS,Rs.70,000\n2.BLUESTAR,Rs.50,000\n3.HIER,Rs.40,000\n4.LLOYD,Rs.65,000")
                n = int(input("what do you want to choose ?:- "))
                if n in range(1,5):
                    lst.append(aircondict.get(n))
                    print(f"You Have Successfully Purchased {n} & It Has Been Added To Your Cart.")
                    bac = str(input("Would You Like To Go Back- ? "))
                    if bac == "yes":
                        print("OK")
                        again()
                    else:
                        #cust.cost3()
                        bill = sum(lst)
                        print("YOUR TOTAL BILL IS - ",bill)
                        print("Thanks For Shopping With US,Have A Great Day!!!!")
                        exit()
            
            
            
            
            if product_name in range(4,5):
                print("1.DELL,Rs.70,000\n2.HP,Rs.50,000\n3.ACER,Rs.40,000\n4.MICROSOFT,Rs.65,000")
                n = int(input("what do you want to choose ?:- "))
                if n in range(1,5):
                    lst.append(laptopdict.get(n))
                    print(f"You Have Successfully Purchased {n} & It Has Been Added To Your Cart.")
                    bac = str(input("Would You Like To Go Back- ? "))
                    if bac == "yes":
                        print("OK")
                        again()
                    else:
                        #cust.cost3()
                        bill = sum(lst)
                        print("YOUR TOTAL BILL IS - ",bill)
                        print("Thanks For Shopping With US,Have A Great Day!!!!")
                        exit()

    
    
    
    
    cust = Ecom(100000)
    cust.header()
    cust.product()
    
again()
































