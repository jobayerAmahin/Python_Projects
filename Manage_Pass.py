master_pass=input("What is the master password? ")

def add():
    account=input("Provide Account name: ")
    gen_pass=input("Provide General Password: ")

    with open("new_pass.txt","a") as f:
        f.write(account+"-"+gen_pass+"\n")

def view():
    with open("new_pass.txt","r") as f:
        for line in f.readlines():
            data= (line.rstrip())
            user,pwd=data.split("-")
            print("User",user,"Password",pwd)


while True:
    mode=input("What is your preference? Add/View/Quit->")
    if mode == "Quit":
        break
    elif mode=="Add":
        add()
    elif mode=="View":
        view()
    else:
        print("Invalid Preference")
        continue
quit()


