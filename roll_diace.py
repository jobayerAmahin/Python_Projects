import random

def roll():
    min_v=1
    max_v=6
    roll_v=random.randint(min_v,max_v)

    return roll_v

val=roll()
print(val)

while True:
    participant=input("Enter the number of players(1 to 4): ")
    if participant.isdigit():
        participant=int(participant)
        if 1<=participant<=4:
            break
        else:
            print("Number of participants must be between 1 and 4")
    else:
        print("Invalid input")

max_score=70
participant_score=[0 for _ in range(participant)]

while max(participant_score)<max_score:
    for par_index in range(participant):
        print("\nThis is your turn, Player number",par_index+1)
        current_score=0

        while True:
            want_diace=input("Would you like to try (y)? ")
            if want_diace.lower()!="y":
                break

            value=roll()
            if value==1:
                print("You turn 1!Now done!")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled a", value)
            
            print("Your score is: ", current_score)

        participant_score[par_index]+=current_score
        print("Your total score is", participant_score[par_index])


