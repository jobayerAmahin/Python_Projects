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
            print("Immediately contact with TE service")
        else:
            print("We hope a good plan from you about your reason of residency")
    else:
        print("Invalid purpose! Try again")
elif categ=="B":
    purB=input("Please write your purpose;Work/Others")
else:
    print("Invalid Category")

