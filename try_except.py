# a={
#     "name":"pratham",
#     "gender":"male",
#     "city":"gwalior"
# }
# # print(a.get("name"))
# print(a["name"])
# try:
#     print(a.get("college"))
#     #print(a["college"])
# except Exception as e:            #it will convert the error into string
#     print(e)                       #it will print the error
    
# print(a["gender"])








a=input("enter a number - ")
b=input("enter another number - ")
try:
    print("the addition is - ",int(a)+int(b))
except Exception as e:
     print(e)

print("if you don't get the answer make sure to enter integers.THANKS,otherwise ignore it")







# try:
#     number=int(input("enter a number - "))
#     print(number)
# except:
#     print("invalid input")