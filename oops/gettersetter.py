#getter = this method is used to read and access the data of variable.this method do not modify the data of variable.

class Mobile:
    def __init__(self,model):
        self.model = model
    
    def get_model(self):
        return self.model 

m = Mobile("promax")
g =m.get_model()
print(g)







#setter = this method is uded to read,access and modify the data of variable.
# class Mobile:
#     def __init__(self):
#         self.model = "12max"

#     def set_model(self):
#         self.model = "12maxpro"

# m = Mobile()
# print(m.model)
# m.set_model()
# print(m.model)





#with passing parameter.
# class Mobile:
#     def set_model(self,a):
#         self.model = a 

# m = Mobile()
# m.set_model("infinity")
# print(m.model)





