#This coding file is for necessary areas of python required for automation testing

#Variables

employee=str(input())
salary=int(input())
eligible=str(input("True/False ? "))

print(employee + "with" ,salary, "is " + eligible +" for pension")

#Conditional Statements

if type(salary)==int:
    if (salary>1000):
        print("Considerable")
    elif(100<salary<1000):
        print("Can be cut from pension")
    else:
        print("Not considerable")
else:
    print("Please use correct format for input")
    quit()