#Random Number Generator

import random

top_range=input("Type your highest number range")
if top_range.isdigit():
    top_range=int(top_range)

    if top_range<=0:
        print("Please try a number greater than 0")
        quit()
else:
    print("Please Enter a number not a letter")
    quit()

random_num = random.randint(0,top_range)
guesses=0

while True:
    guesses+=1
    userInput=input("Guess a number")
    if userInput.isdigit():
        userInput=int(userInput)
    else:
        print("Please type a number")
        continue
    if userInput==random_num:
        print("You got it!!!")
        break
    
    elif userInput>random_num:
            print("You are above of number")
    else:
            print("You are below number")

print("You got it in", guesses, "guesses")