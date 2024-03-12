import random

user_win=0
computer_win=0

carts=['rock','paper','scissors']

while True:
    userI = input("Type rock/paper/scissors or 'q' to quit the game: ").lower()
    if userI=='q':
        break

    if userI not in carts:
        continue

    randNum=random.randint(0,2)
    pcPick=carts[randNum]
    print("Computer Picked "+pcPick+".")

    if userI== "rock" and pcPick=="scissors":
        print("You Won!")
        user_win+=1
    elif userI== "paper" and pcPick=="rock":
        print("You Won!")
        user_win+=1
    elif userI== "scissors" and pcPick=="paper":
        print("You Won!")
        user_win+=1
    else:
        print("Computer won!")
        computer_win+=1

print("You won",user_win,"times")
print("PC won",computer_win,"times")