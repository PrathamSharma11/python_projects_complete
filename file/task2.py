# def game():
#     return 1500
# score=game()


# with open("file/highscore.txt",'r') as f:
#     b = int(f.read())

# if score>b:
#     with open("file/highscore.txt",'w') as f:
#         c =f.write(str(score))
#     print(c)




# with open("file/shivam.txt",'r') as f:
#     a=f.read()

# if "donkey" in a:
#     with open("file/shivam.txt",'w') as f:
#         c = f.write(a.replace("donkey","#$%#$"))
#         print(c)





list =["do","epic","Shit"]

with open("file/shivam.txt",'r') as f:                 #not working
    a = f.read()

if a in list:
    with open("file/shivam.txt",'w') as f:
        b = f.write(a.replace(list,"#$%#$%"))
        print(b)






# with open("file/sample.txt",'r') as f:
#     a = f.read()

# with open("file/sample2.txt",'r') as f:
#     b = f.read()

# if a==b:
#     print("yes they are identical")
# else:
#     print("no they're not")




# with open("file/sample2.txt",'w') as f:
#     a = f.write("")
















     


