# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary 


#     def getDetails(self,a):
#         print(f"{a}")
#         print(f"the name of the employee is {self.name}")
#         print(f"the name of the employyee is {self.salary}")

# rohit = Employee("raj","1222")
# rohit.getDetails(100)





# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# a = Person("james",56)
# print(a.name)
# print(a.age)




# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"hello {self.name}")
# a = Person("james",56)
# a.greet()












# c = input("enter name : - ")
# d = input("enter his work: - ")

# class Programmer:
#     def __init__(self):
#         print("the man you are looking for is - ")
#     def info(self):
#         print(f"{self.name},is working on {self.b}")
#     def max(self,a):
#         print(f"he is {a} years old  ")
       
# investigation = Programmer()
# investigation.name = c
# investigation.b = d
# investigation.info()
# investigation.max(20)



a = input("enter your name: ")
b = int(input("enter your ticket number: "))
class Theater:
    movie = "bond"
    def __init__(self,name,number):
        self.name = name
        self.number= number
    

    def seat(self):
        print(f"{self.name} your ticket  number is {self.number} and the your screen is - 5th")

film = Theater("pratham",2701)
film.seat()
film2 = Theater("sharma",111)
film2.seat()








        