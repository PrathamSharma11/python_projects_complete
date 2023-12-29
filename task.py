# name = input("Enter Your Name - \n")

# date = input("Enter Date - \n")

# print("Dear - ",name)
# print("you are selected \n have a great day \n thank you \n \n Date-",date)

#or

letter = '''Dear, NAME
You Are Selected
Have A Great Day
Thank You

Date, DATE'''
name = input("Enter Your Name - ")
date = input("Enter Date - ")
letter = letter.replace("NAME",name)
letter = letter.replace("DATE",date)

print(letter)

