#for range function in python is to 
#generate a sequence of numbers we can also specify the start,stop and step-size.


#for b in range(10):   #by default starts with 0,never take last digit
 #   print(b)

#for b in range(1,5):  #starts with 1
    #print(b)

#for b in range(1,5,2): #starts with 1 upto 4 with difference of 2
 #   print(b)


#for b in range(8,1,-1):
#    print(b)


adj = ["red","orange","pink"]
fruits = ["apple","banana","cherry"]
c = ["ap","ba","ch"]
for x in adj:
    for y in fruits:
        for z in c:
            print(x,y,z)