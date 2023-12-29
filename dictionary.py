# dictionaries are used to store value in form of key and value
# dictionaries are collection of key value pairs
a = { 
    "name": "pninfosys gwalior",
    "c" : [2,4,6,7],
      4 : ("mits","itm"),
    "college" : "rjit",
    "education" : { "ram" : "mca"}, 
    "college" : "liberty" #i.e. duplicacy not allowed it will overwrite 
   
}
#print(a["education"][2]) #error
#print(a["education"]["ram"][1]) #very important
#print(a["c"][2])
#print(a["college"])
# print(a[4])
# print(a["name"])
# print(type(a))
# print(type(a[4]))
# print(type(a["education"]))


#change dictionary items
print(a["c"])
print(type(a["c"]))
a["c"] = [5,5,5,5]
print(a["c"])
print(type(a["c"]))