# class Employee:
#     company = "pninfosys"
#     ceo = "vikas sir"
    
#     def showDetails(self):
#         print("this is an employee")
    
# class Programmer(Employee):
#     language = "python"
#     ceo2 = "sundar pichai"
#     company = "google"


#     def getLanguage(self):
#         print(f"the language is {self.language}")

#     def showDetails(self):
#         print("this is a programmer")

# e = Employee()
# e.showDetails()
# p = Programmer()
# p.showDetails()            #will check ki object kiska h uske hisaab se print karega.
# print(p.company)
# print(p.ceo)
# print(e.ceo)





# class baap:
#     zameen = "10 acre"

#     def propert(self):
#         print(f" father has property {self.zameen} worth of 10 crore")

# class beta(baap):
#     status =  "unemployed"

#     def please(self):
#         print(f" i am {self.status} but i am also eklota so,,,i am rich bitch!!!!")

# ameer = baap()
# gareeb = beta()
# gareeb.propert()
# gareeb.please()






# class base:
#     def __init__(self,name,surname):
#         self.name = name 
#         self.surname = surname 
    
#     def intro(self):
#         print(f"hello i am {self.name} {self.surname}")

# class derived(base):
#     pass 


# x = base("pratham","sharma")
# x.intro()
# y = derived("james","Bond")
# y.intro()





#multiple inheritance


# class Employee:
#     company = "apple"
#     name = "tim"

# class Freelancer:
#     company = "google"
#     name = "larry"
#     level = 0 

#     def upgradelevel(self):
#         self.level = self.level+1

# class pro(Employee,Freelancer):
#     name = "pratham"

     
# p = pro()
# print(p.company)
# print(p.name)
# p.upgradelevel()
#print(p.level)
#print(p.company)










#multilevel inheritance

# class Person:
#     country = "india"
#     pm = "modi"
    
#     def call(self):
#         print("i am person")

# class alpha(Person):
#     country = "usa"
    
#     def salary(self):
#         print("100k")

#     def call(self):
#         print("i am alpha")


# class gamma(alpha):
#     country = "australia"
    
#     def salary(self):
#         print("no salary")
    
#     def call2(self):
#         print("i am gamma")


# p = Person()
# a = alpha()
# g = gamma()
# g.call()
# print(g.pm)

        








