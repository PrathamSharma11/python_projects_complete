class Employee:
    company = "google"
    salary = 100

raj = Employee()
ram = Employee()
print(raj.salary)        #class attribute
print(ram.salary)
raj.salary = 200         #object aatribute
ram.salary = 400
print(raj.salary)
print(ram.salary)
#print(ram.address)      #error
