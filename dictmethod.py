a = {
    "name" : "gwalior",
    "college" : "itm",
    "mark" : [1,2,3,4],
    "education" : {"ram" : "mca"},
}
#print(a.keys())
#print(type(a.keys()))
#print(list(a.keys()))
#print(a.values())
#print(a.items())






#update dictionary
extras ={
    "email" : "1pratham1sharma@gmail.com",
    "mobile" : 6261264410,
    "name" : "pratham"
}
a.update(extras)
print(a)









#  get method

# print(a["name"])      #it will give gwalior
# print(a.get("abc"))  #it will give none in output
# print(a.get("college")) #it will give itm
