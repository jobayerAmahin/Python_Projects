name=input("Enter your name")
print("Welcome to Finland," + name)

categ=input("Please write your visa category;A/B")
if categ=="A":
    purA=input("Please write your purpose;Student/Spouse")
    if purA=="Student":
        print("Good Luck for your study!")
    elif purA=="Spouse":
        tar=input("Are you a job seeker?Y/N")
        if tar=="Y":
            print("Immediately contact to TE office")
            train=input("What are you planing to learn? 1. Language. 2.Professional Traing? Please type 1 or 2")
            if train=="1":
                print("You have to wait a few months as the queue is long")
            else:
                print("We will send you some link of Work Trial through your email")
        else:
            print("We hope a good plan from you about your reason of residency")
    else:
        print("Invalid purpose! Try again")
elif categ=="B":
    purB=input("Please write your purpose;Work/Others")
else:
    print("Invalid Category")

