import random

def roll():
    min_v=1
    max_v=6
    roll_v=random.randint(min_v,max_v)

    return roll_v

val=roll()
print(val)