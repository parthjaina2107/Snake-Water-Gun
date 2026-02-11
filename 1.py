import random
choice = random.choice([-1, 0, 1])
user=int(input())
dict1={-1:"Snake",0:"water",1:"Gun"}
if(user>1 or user < -1):
    print("invalid input")

print(f"Computer's input {choice}")
print(f"user's input {user}")
if(user == choice):
    print("Draw")
    