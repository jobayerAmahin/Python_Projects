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

#Array and loop iteration

browsers=["chrome","firefox","edge","IE","opera"]
browsers.append("unknown")

for browser in browsers:
    print(browser)

#Dictionary and loop iteration

setAut={
    "browser":"edge",
    "os":"windows",
    "device":"pc",
    "type":"sanity"
}

print(setAut.get("os"))

for aut in setAut.values():
    print(aut)

if "device" in setAut:
    print("Pass")

#Function

tx=input()
wd=input()
def searchWord(x,y):
    c=x.split()
    if y in c:
        print("word found")
    else:
        print("word not found")
print(searchWord(tx,wd))
quit()

#Class

class LoginPage:
    def __init__(self, secret):
        self.secret=secret

    def login(self,user,password):
        return user + "---" +password
    
    def loginWithSecret(self,user,password):
        return user +"---" + password+ self.secret
    
cred=LoginPage("#%")
print(cred.login("Mahin","234"))
print(cred.loginWithSecret("Alam","442"))