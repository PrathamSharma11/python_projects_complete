a = (1,3,5,7,5,4,2,5,6)

#print(a.count(5))
#print(a.index(3)) # which index value has 3 // 3 ki value kis index par h.

#tuple update -
#a[0] = 12
#print(a) #error tuple object does not support item assignment, but with the help of list it could


# x = ("apple","banana","cherry")
# y = list(x)  #tuple ko list bana diya
# print(y)
# y[1] = "kiwi"
# x = tuple(y) #list ko tuple bana diya
# print(x)



#tuple join - 

# tuple1 = ("a","b") 
# tuple2 = (1,4)
# tuple3 = tuple1 + tuple2
# print(tuple3)


#tuple multiply -

# fruits = (2,4,6)
# y = fruits * 2
# print(y)


# b = (7,0,8,0,9,[1,2,2,2,4,5])
# print(b.count(2))
# print(type(b))



 
oned = ("louis","harry","niall","liam")
reunion = list(oned)
reunion.append("zayn")
oned = tuple(reunion)
print(oned)