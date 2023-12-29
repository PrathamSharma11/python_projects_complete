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
                        
                        bill = sum(lst)
                        print("YOUR TOTAL BILL IS - ",bill)
                        print("Thanks For Shopping With US,Have A Great Day!!!!")
                        exit()

    
    
    
    
    cust = Ecom(100000)
    cust.header()
    cust.product()
    
again()

list = [1,2]
list2 = [2]
list3 = [4]
class Recharge:
    total = 100000

    def __init__(self,name,passw,bill):
        print(30*"*","Welcome To Amazon Pay",30*"*")
        self.name = name
        self.passw = passw
        self.bill = bill

    def login(self):
        name = input("Enter Your Name:- \n")
        passw = int(input("Enter Your Pin:- \n"))
        if name==self.name and passw==self.passw:
            print(f"Welcome {self.name} You Have Rs.{self.total} in your Account.")   
        else:
            print("INVALID INPUT")
    def pp(self):
        if n in list:
            print("Choose A Bank-: \n1.SBI \n2.CBI \n3.AXIS \n4.PNB")
        else:
            print("Sorry, We Are Currently Not  Providing The Service")
    
    def operator(self):
            card_num = int(input("Enter Card Number-: "))
            passwo = int(input("Enter CVV-: "))        
    

    def payment(self):
        self.left = self.total - self.bill
        print(f"PAYMENT SUCCESSFUL!!!\nAccount Balance-: Rs.{self.left}") 
    
    @staticmethod
    def greet():
        print("THANKS, For Choosing US.")

sim = Recharge("pratham",2001,"bill")
sim.login()
n = int(input("What Do You Want To Choose-: \n1.Gpay \n2.NetBanking \n"))
sim.pp()
a = int(input())
sim.operator()
sim.payment()
sim.greet()