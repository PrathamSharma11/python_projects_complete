# class Person:
#     country = "india"
    
#     def no(self):
#         print("no no no ")
#     def call(self):
#         print("i am person")

# class alpha(Person):
#     def call(self):
#         super().no()
#         print("i am alpha")


# class gamma(alpha):
#     def call(self):
#         super().call()
#         print("i am gamma")


# p = Person()
# a = alpha()
# g = gamma()
# g.call()







#super with constructor
class Person:
    country = "india"
    
    def no(self):
        print("no no no ")
    def call(self):
        print("i am person")
    def __init__(self):
        super().__init__()
        print("person")

class alpha(Person):
    def call(self):
        super().no()
        print("i am alpha")
    
    def __init__(self):
        super().__init__()
        print("alpha")


class gamma(alpha):
    def call(self):
        print("i am gamma")

    def __init__(self):
        super().__init__()
        print("gamma")


#p = Person()
#a = alpha()
g = gamma()
#g.call()
